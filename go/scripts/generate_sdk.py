#!/usr/bin/env python3
"""Generate Go docmost SDK from OpenAPI spec."""
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

GO_RESERVED = {
    "break", "case", "chan", "const", "continue", "default", "defer", "else",
    "fallthrough", "for", "func", "go", "goto", "if", "import", "interface",
    "map", "package", "range", "return", "select", "struct", "switch",
    "type", "var",
}


def pascal(s: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", s)
    name = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if not name:
        return "Item"
    if name[0].isdigit():
        name = "Item" + name
    return name


def snake(s: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    return s.replace("-", "_").lower()


def is_nullable_union(schema: dict) -> bool:
    t = schema.get("type")
    return isinstance(t, list) and "null" in t


def go_type(schema: dict, schemas: dict, *, required: bool) -> str:
    if "$ref" in schema:
        base = schema["$ref"].split("/")[-1]
    elif "oneOf" in schema or "allOf" in schema:
        for part in schema.get("allOf", schema.get("oneOf", [])):
            if isinstance(part, dict) and "$ref" in part:
                base = part["$ref"].split("/")[-1]
                break
        else:
            base = "map[string]any"
    elif "enum" in schema:
        base = "string"
    elif schema.get("type") == "array":
        item = go_type(schema["items"], schemas, required=True)
        item = item.removeprefix("*") if item.startswith("*") else item
        base = f"[]{item}"
    elif schema.get("type") == "object":
        if "additionalProperties" in schema:
            val = go_type(schema["additionalProperties"], schemas, required=True)
            base = f"map[string]{val}"
        else:
            base = "map[string]any"
    elif schema.get("type") == "integer":
        base = "int"
    elif schema.get("type") == "number":
        base = "float64"
    elif schema.get("type") == "boolean":
        base = "bool"
    elif schema.get("type") == "string" and schema.get("format") == "binary":
        base = "io.Reader"
    else:
        base = "string"

    if not required or is_nullable_union(schema):
        if base.startswith("[]") or base.startswith("map["):
            return base
        return f"*{base}"
    return base


def collect_refs(schema: dict, out: set[str]) -> None:
    if "$ref" in schema:
        out.add(schema["$ref"].split("/")[-1])
        return
    if "items" in schema:
        collect_refs(schema["items"], out)
    for key in ("allOf", "oneOf", "anyOf"):
        for part in schema.get(key, []):
            if isinstance(part, dict):
                collect_refs(part, out)
    if schema.get("type") == "object":
        for prop in schema.get("properties", {}).values():
            collect_refs(prop, out)


def gen_struct(name: str, schema: dict, schemas: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    refs: set[str] = set()
    for prop_schema in props.values():
        collect_refs(prop_schema, refs)
    refs.discard(name)

    lines = [f"// {name} from OpenAPI.", f"type {name} struct {{"]
    for prop_name, prop_schema in props.items():
        if not prop_name.replace("_", "").isalnum():
            continue
        is_req = prop_name in required and not is_nullable_union(prop_schema)
        field = pascal(prop_name)
        if field.lower() in GO_RESERVED:
            field = field + "_"
        t = go_type(prop_schema, schemas, required=is_req)
        json_tag = prop_name
        omitempty = "" if is_req else ",omitempty"
        lines.append(f"\t{field} {t} `json:\"{json_tag}{omitempty}\"`")
    lines.append("}")
    return "\n".join(lines) + "\n"


def gen_inline_request(name: str, schema: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    has_binary = any(p.get("format") == "binary" for p in props.values())
    header = "package models\n\n"
    if has_binary:
        header += "import \"io\"\n\n"
    lines = [header + f"// {name} request.", f"type {name} struct {{"]
    for prop_name, prop_schema in props.items():
        is_req = prop_name in required
        field = pascal(prop_name)
        if prop_schema.get("format") == "binary":
            t = "io.Reader"
        else:
            t = go_type(prop_schema, {}, required=is_req)
        omitempty = "" if is_req else ",omitempty"
        lines.append(f"\t{field} {t} `json:\"{prop_name}{omitempty}\"`")
    lines.append("}")
    return "\n".join(lines) + "\n"


def go_path_expr(path: str, path_params: list[str]) -> str:
    rel = path.lstrip("/")
    if not path_params:
        return f'"{rel}"'
    fmt_parts: list[str] = []
    args: list[str] = []
    for seg in re.split(r"(\{[^}]+\})", rel):
        if seg.startswith("{") and seg.endswith("}"):
            pname = seg[1:-1]
            fmt_parts.append("%s")
            args.append(f"url.PathEscape({pname})")
        else:
            fmt_parts.append(seg.replace("%", "%%"))
    fmt = "".join(fmt_parts)
    return f'fmt.Sprintf("{fmt}", {", ".join(args)})'


def gen_service(tag: str, ops: list) -> str:
    class_name = pascal(tag.replace(" ", "")) + "API"
    model_imports = set()
    needs_fmt = False
    needs_url = False
    needs_http = False
    for op in ops:
        dto = op.get("dto")
        if dto and dto != "inline":
            model_imports.add(dto)
        elif op.get("inline_schema"):
            model_imports.add(op["inline_schema"]["name"])
        if op.get("path_params"):
            needs_fmt = True
            needs_url = True
        if op.get("query_params"):
            needs_url = True
        if op["method"] == "GET" and ("/files/" in op["path"] or "/attachments/img/" in op["path"]):
            needs_http = True

    import_lines = ['\t"context"', ""]
    if needs_url:
        import_lines.append('\t"net/url"')
    import_lines.append('\t"github.com/ggpo1/docmost-sdk/go/internal/httpclient"')
    if model_imports:
        import_lines.append('\t"github.com/ggpo1/docmost-sdk/go/docmost/models"')
    if needs_fmt:
        import_lines.insert(0, '\t"fmt"')
    if needs_http:
        import_lines.insert(0, '\t"net/http"')

    lines = ["package services", "", "import (", *import_lines, ")", ""]

    lines.extend([
        f"// {class_name} implements {tag} API.",
        f"type {class_name} struct {{",
        "\thttp *httpclient.HTTPClient",
        "}",
        "",
        f"func New{class_name}(http *httpclient.HTTPClient) *{class_name} {{",
        f"\treturn &{class_name}{{http: http}}",
        "}",
        "",
    ])

    for op in ops:
        method_name = pascal(op["operationId"])
        path = op["path"]
        http_method = op["method"]
        dto = op.get("dto")
        path_params = op.get("path_params", [])
        query_params = op.get("query_params", [])
        content = op.get("content")
        inline = op.get("inline_schema")

        params = ["ctx context.Context"]
        if dto and dto != "inline":
            params.append(f"request *models.{dto}")
        elif inline:
            params.append(f"request *models.{inline['name']}")
        for pp in path_params:
            params.append(f"{pp} string")
        for qp in query_params:
            params.append(f"{qp} *string")
        sig = ", ".join(params)

        is_raw_get = http_method == "GET" and (
            "/files/" in path or "/attachments/img/" in path
        )
        ret = "(*http.Response, error)" if is_raw_get else "(*httpclient.ApiResponse, error)"

        lines.append(f"func (a *{class_name}) {method_name}({sig}) {ret} {{")
        path_expr = go_path_expr(path, path_params)

        if http_method == "GET":
            if query_params:
                lines.append(f"\tpath := {path_expr}")
                lines.append("\tparams := url.Values{}")
                for qp in query_params:
                    lines.append(f"\tif {qp} != nil {{")
                    lines.append(f"\t\tparams.Set(\"{qp}\", *{qp})")
                    lines.append("\t}")
                if is_raw_get:
                    lines.append("\treturn a.http.GetRaw(ctx, path, params)")
                else:
                    lines.append("\treturn a.http.Get(ctx, path, params)")
            elif is_raw_get:
                lines.append(f"\treturn a.http.GetRaw(ctx, {path_expr}, nil)")
            else:
                lines.append(f"\treturn a.http.Get(ctx, {path_expr}, nil)")
        elif content == "multipart/form-data":
            lines.append(f"\treturn a.http.PostMultipart(ctx, {path_expr}, request)")
        else:
            body = "nil"
            if dto and dto != "inline":
                body = "request"
            elif inline:
                body = "request"
            lines.append(f"\treturn a.http.Post(ctx, {path_expr}, {body})")
        lines.append("}")
        lines.append("")

    return "\n".join(lines) + "\n"


def service_file_key(class_name: str) -> str:
    stem = re.sub(r"API$", "", class_name)
    stem = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", stem)
    stem = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", stem)
    return snake(stem) + "_api.go"


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    schemas = spec["components"]["schemas"]
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    SERVICES_DIR.mkdir(parents=True, exist_ok=True)

    model_names: list[str] = []
    for name, schema in schemas.items():
        if name in ("ApiResponse", "ErrorResponse"):
            continue
        file_key = snake(name) + ".go"
        (MODELS_DIR / file_key).write_text(
            "package models\n\n" + gen_struct(name, schema, schemas)
        )
        model_names.append(name)

    (MODELS_DIR / "api_response.go").write_text(
        """package models

// ApiResponse is the standard API envelope.
type ApiResponse struct {
\tData    any  `json:"data,omitempty"`
\tSuccess bool `json:"success"`
\tStatus  int  `json:"status"`
}

// ErrorResponse is returned on HTTP errors.
type ErrorResponse struct {
\tStatusCode int      `json:"statusCode,omitempty"`
\tMessage    any      `json:"message,omitempty"`
\tError      string   `json:"error,omitempty"`
}
"""
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
                        (MODELS_DIR / (snake(inline_name) + ".go")).write_text(
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

    for tag, ops in sorted(ops_by_tag.items()):
        class_name = pascal(tag.replace(" ", "")) + "API"
        file_key = service_file_key(class_name)
        (SERVICES_DIR / file_key).write_text(gen_service(tag, ops))

    print(f"Generated {len(list(MODELS_DIR.glob('*.go')))} models, {len(list(SERVICES_DIR.glob('*.go')))} services")


if __name__ == "__main__":
    main()
