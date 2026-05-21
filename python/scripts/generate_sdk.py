#!/usr/bin/env python3
"""Generate docmost Python package from OpenAPI spec."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = ROOT / "api-1.json"
PKG = Path(__file__).resolve().parents[1] / "docmost"
MODELS_DIR = PKG / "models"
SERVICES_DIR = PKG / "services"

RESERVED = {"class", "def", "if", "return", "type"}


def pascal(s: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", s)
    name = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if not name:
        return "Item"
    if name[0].isdigit():
        name = "Item" + name
    if name.lower() in RESERVED:
        name += "_"
    return name


def snake(s: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.replace("-", "_").lower()


def is_nullable_union(schema: dict) -> bool:
    t = schema.get("type")
    return isinstance(t, list) and "null" in t


def python_type(schema: dict, schemas: dict, *, required: bool) -> str:
    if "$ref" in schema:
        base = schema["$ref"].split("/")[-1]
    elif "oneOf" in schema or "allOf" in schema:
        for part in schema.get("allOf", schema.get("oneOf", [])):
            if isinstance(part, dict) and "$ref" in part:
                base = part["$ref"].split("/")[-1]
                break
        else:
            base = "dict[str, object]"
    elif "enum" in schema:
        base = "str"
    elif schema.get("type") == "array":
        item = python_type(schema["items"], schemas, required=True)
        item = item.replace("Optional[", "").replace("]", "") if item.startswith("Optional[") else item
        base = f"list[{item}]"
    elif schema.get("type") == "object":
        if "additionalProperties" in schema:
            val = python_type(schema["additionalProperties"], schemas, required=True)
            val = val.replace("Optional[", "").rstrip("]") if val.startswith("Optional[") else val
            base = f"dict[str, {val}]"
        else:
            base = "dict[str, object]"
    elif schema.get("type") == "integer":
        base = "int"
    elif schema.get("type") == "number":
        base = "float"
    elif schema.get("type") == "boolean":
        base = "bool"
    elif schema.get("type") == "string" and schema.get("format") == "binary":
        base = "bytes"
    else:
        base = "str"

    if not required:
        return f"Optional[{base}]"
    return base


def gen_model(name: str, schema: dict, schemas: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    fields = []
    for prop_name, prop_schema in props.items():
        is_req = prop_name in required and not is_nullable_union(prop_schema)
        py_name = snake(prop_name)
        py_type = python_type(prop_schema, schemas, required=is_req)
        fields.append(
            f'    {py_name}: {py_type} = Field(default=None, alias="{prop_name}")'
            if not is_req
            else f'    {py_name}: {py_type} = Field(alias="{prop_name}")'
        )
    body = "\n".join(fields) if fields else "    pass"
    return f'''"""Generated from OpenAPI schema {name}."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class {name}(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

{body}
'''


def gen_inline_request(name: str, schema: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    fields = []
    for prop_name, prop_schema in props.items():
        is_req = prop_name in required
        py_name = snake(prop_name)
        if prop_schema.get("format") == "binary":
            py_type = "Union[bytes, BinaryIO]"
        else:
            py_type = python_type(prop_schema, {}, required=is_req)
        if is_req:
            fields.append(f'    {py_name}: {py_type} = Field(alias="{prop_name}")')
        else:
            fields.append(f'    {py_name}: {py_type} = Field(default=None, alias="{prop_name}")')
    return f'''"""Generated multipart request {name}."""
from __future__ import annotations

from typing import BinaryIO, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class {name}(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

{chr(10).join(fields)}
'''


def py_path_expr(path: str, path_params: list[str]) -> str:
    rel = path.lstrip("/")
    if not path_params:
        return f'"{rel}"'
    segments = re.split(r"(\{[^}]+\})", rel)
    out = 'f"'
    for seg in segments:
        if seg.startswith("{") and seg.endswith("}"):
            pname = seg[1:-1]
            out += f"{{DocmostHttpClient.escape_path_segment({pname})}}"
        else:
            out += seg
    out += '"'
    return out


def gen_service(tag: str, ops: list) -> str:
    class_name = pascal(tag.replace(" ", "")) + "Api"
    lines = [
        '"""Generated API client."""',
        "from __future__ import annotations",
        "",
        "from typing import Any, Optional",
        "",
        "import httpx",
        "",
        "from docmost.http_client import DocmostHttpClient",
        "from docmost.types import ApiResponse",
    ]
    model_imports = set()
    for op in ops:
        dto = op.get("dto")
        if dto and dto != "inline":
            model_imports.add(dto)
        elif op.get("inline_schema"):
            model_imports.add(op["inline_schema"]["name"])
    if model_imports:
        lines.append("from docmost.models import " + ", ".join(sorted(model_imports)))

    lines.extend(["", "", f"class {class_name}:", '    """' + tag + ' API."""', "", "    def __init__(self, http: DocmostHttpClient) -> None:", "        self._http = http", ""])

    for op in ops:
        op_id = op["operationId"]
        method_name = snake(op_id)
        path = op["path"]
        http_method = op["method"]
        dto = op.get("dto")
        path_params = op.get("path_params", [])
        query_params = op.get("query_params", [])
        content = op.get("content")
        inline = op.get("inline_schema")

        params = ["self"]
        if dto and dto != "inline":
            params.append(f"request: {dto}")
        elif inline:
            params.append(f"request: {inline['name']}")
        for pp in path_params:
            params.append(f"{pp}: str")
        for qp in query_params:
            params.append(f"{qp}: Optional[str] = None")
        sig = ", ".join(params)

        is_raw_get = http_method == "GET" and (
            "/files/" in path or "/attachments/img/" in path
        )
        ret = "httpx.Response" if is_raw_get else "ApiResponse[Any]"

        lines.append(f"    def {method_name}({sig}) -> {ret}:")
        path_expr = py_path_expr(path, path_params)

        if http_method == "GET":
            if query_params:
                lines.append(f"        path = {path_expr}")
                lines.append("        params: dict[str, str] = {}")
                for qp in query_params:
                    lines.append(f"        if {qp} is not None:")
                    lines.append(f"            params['{qp}'] = {qp}")
                if is_raw_get:
                    lines.append("        return self._http.get_raw(path, params=params or None)")
                else:
                    lines.append("        return self._http.get(path, params=params or None)")
            elif is_raw_get:
                lines.append(f"        return self._http.get_raw({path_expr})")
            else:
                lines.append(f"        return self._http.get({path_expr})")
        elif content == "multipart/form-data":
            lines.append(f"        path = {path_expr}")
            lines.append("        files: dict[str, tuple[str, bytes | Any, str]] = {}")
            lines.append("        data: dict[str, str] = {}")
            if inline:
                for prop_name, prop_schema in inline.get("properties", {}).items():
                    pn = snake(prop_name)
                    if prop_schema.get("format") == "binary":
                        lines.append(f"        raw = request.{pn}")
                        lines.append("        content = raw.read() if hasattr(raw, 'read') else raw")
                        lines.append(
                            f'        files["{prop_name}"] = ("upload.bin", content, "application/octet-stream")'
                        )
                    else:
                        lines.append(
                            f'        if request.{pn} is not None: data["{prop_name}"] = str(request.{pn})'
                        )
            lines.append(
                "        return self._http.post_multipart(path, data=data or None, files=files or None)"
            )
        else:
            body = "None"
            if dto and dto != "inline":
                body = "request.model_dump(by_alias=True, exclude_none=True)"
            elif inline:
                body = "request.model_dump(by_alias=True, exclude_none=True)"
            lines.append(f"        return self._http.post({path_expr}, body={body})")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    schemas = spec["components"]["schemas"]
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    SERVICES_DIR.mkdir(parents=True, exist_ok=True)

    model_names: list[str] = []
    for name, schema in schemas.items():
        if name == "ApiResponse":
            continue
        (MODELS_DIR / f"{snake(name)}.py").write_text(gen_model(name, schema, schemas))
        model_names.append(name)

    (MODELS_DIR / "api_response.py").write_text(
        '''"""API envelope types."""
from __future__ import annotations

from typing import Generic, Optional, TypeVar, Union

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    model_config = ConfigDict(populate_by_name=True)

    data: Optional[T] = Field(default=None, alias="data")
    success: bool = Field(alias="success")
    status: int = Field(alias="status")


class ErrorResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    status_code: Optional[int] = Field(default=None, alias="statusCode")
    message: Optional[Union[str, list[str]]] = Field(default=None, alias="message")
    error: Optional[str] = Field(default=None, alias="error")
'''
    )

    ops_by_tag: dict[str, list] = defaultdict(list)
    for path, methods in spec["paths"].items():
        for method, op in methods.items():
            if method == "parameters":
                continue
            rb = op.get("requestBody", {})
            dto = None
            content = None
            inline_schema = None
            if rb:
                for ct, body in rb.get("content", {}).items():
                    content = ct
                    s = body.get("schema", {})
                    if "$ref" in s:
                        dto = s["$ref"].split("/")[-1]
                    elif s.get("type") == "object":
                        inline_name = pascal(op["operationId"]) + "Request"
                        (MODELS_DIR / f"{snake(inline_name)}.py").write_text(
                            gen_inline_request(inline_name, s)
                        )
                        model_names.append(inline_name)
                        dto = "inline"
                        inline_schema = dict(s)
                        inline_schema["name"] = inline_name
                    break
            params = op.get("parameters", [])
            ops_by_tag[op.get("tags", ["Other"])[0]].append({
                "path": path,
                "method": method.upper(),
                "operationId": op["operationId"],
                "dto": dto,
                "content": content,
                "path_params": [p["name"] for p in params if p.get("in") == "path"],
                "query_params": [p["name"] for p in params if p.get("in") == "query"],
                "inline_schema": inline_schema if dto == "inline" else None,
            })

    service_exports: list[tuple[str, str]] = []
    for tag, ops in sorted(ops_by_tag.items()):
        class_name = pascal(tag.replace(" ", "")) + "Api"
        mod = snake(class_name)
        (SERVICES_DIR / f"{mod}.py").write_text(gen_service(tag, ops))
        service_exports.append((mod, class_name))

    init_exports = ["from docmost.models.api_response import ApiResponse, ErrorResponse"]
    for name in sorted(set(model_names)):
        mod = snake(name)
        init_exports.append(f"from docmost.models.{mod} import {name}")
    (MODELS_DIR / "__init__.py").write_text(
        '"""Pydantic models from OpenAPI."""\n' + "\n".join(init_exports) + "\n\n__all__ = [\n"
        + ",\n".join(f'    "{n}"' for n in ["ApiResponse", "ErrorResponse", *sorted(set(model_names))])
        + ",\n]\n"
    )

    svc_init = ["from docmost.http_client import DocmostHttpClient"]
    for mod, cls in service_exports:
        svc_init.append(f"from docmost.services.{mod} import {cls}")
    (SERVICES_DIR / "__init__.py").write_text("\n".join(svc_init) + "\n")

    print(
        f"Generated {len(list(MODELS_DIR.glob('*.py')))} model modules, "
        f"{len(list(SERVICES_DIR.glob('*.py')))} service modules"
    )


if __name__ == "__main__":
    main()
