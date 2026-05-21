#!/usr/bin/env python3
"""Generate @docmost/sdk TypeScript sources from OpenAPI spec."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = ROOT / "api-1.json"
SRC = Path(__file__).resolve().parents[1] / "src"
MODELS_DIR = SRC / "models"
SERVICES_DIR = SRC / "services"

TS_RESERVED = {"break", "case", "catch", "class", "const", "continue", "default", "delete", "do", "else", "enum", "export", "extends", "false", "finally", "for", "function", "if", "import", "in", "instanceof", "new", "null", "return", "super", "switch", "this", "throw", "true", "try", "typeof", "var", "void", "while", "with", "implements", "interface", "let", "package", "private", "protected", "public", "static", "yield"}


def pascal(s: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", s)
    name = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if not name:
        return "Item"
    if name[0].isdigit():
        name = "Item" + name
    return name


def camel(s: str) -> str:
    p = pascal(s)
    return p[0].lower() + p[1:] if p else s


def is_nullable_union(schema: dict) -> bool:
    t = schema.get("type")
    return isinstance(t, list) and "null" in t


def ts_type(schema: dict, schemas: dict, *, required: bool) -> str:
    if "$ref" in schema:
        base = schema["$ref"].split("/")[-1]
    elif "oneOf" in schema or "allOf" in schema:
        for part in schema.get("allOf", schema.get("oneOf", [])):
            if isinstance(part, dict) and "$ref" in part:
                base = part["$ref"].split("/")[-1]
                break
        else:
            base = "Record<string, unknown>"
    elif "enum" in schema:
        base = "string"
    elif schema.get("type") == "array":
        item = ts_type(schema["items"], schemas, required=True).replace(" | null", "").replace(" | undefined", "")
        base = f"{item}[]"
    elif schema.get("type") == "object":
        if "additionalProperties" in schema:
            val = ts_type(schema["additionalProperties"], schemas, required=True)
            val = val.replace(" | null", "").replace(" | undefined", "")
            base = f"Record<string, {val}>"
        else:
            base = "Record<string, unknown>"
    elif schema.get("type") == "integer" or schema.get("type") == "number":
        base = "number"
    elif schema.get("type") == "boolean":
        base = "boolean"
    elif schema.get("type") == "string" and schema.get("format") == "binary":
        base = "Blob | Buffer | ReadableStream"
    else:
        base = "string"

    if not required or is_nullable_union(schema):
        return f"{base} | null | undefined"
    return base


def schema_file_key(name: str) -> str:
    return re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name).lower()


def service_file_key(class_name: str) -> str:
    stem = re.sub(r"Api$", "", class_name)
    stem = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", stem)
    stem = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", stem)
    return stem.lower() + "-api.ts"


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


def gen_interface(name: str, schema: dict, schemas: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    refs: set[str] = set()
    for prop_schema in props.values():
        collect_refs(prop_schema, refs)
    refs.discard(name)

    lines = [f"/** Generated from OpenAPI schema `{name}`. */"]
    for r in sorted(refs):
        lines.append(f"import type {{ {r} }} from './{schema_file_key(r)}.js';")
    if refs:
        lines.append("")
    lines.append(f"export interface {name} {{")

    for prop_name, prop_schema in props.items():
        is_req = prop_name in required and not is_nullable_union(prop_schema)
        ts_name = prop_name if prop_name.isidentifier() else f'"{prop_name}"'
        if not prop_name.isidentifier():
            continue  # skip weird keys
        opt = "" if is_req else "?"
        t = ts_type(prop_schema, schemas, required=is_req)
        lines.append(f"  {prop_name}{opt}: {t};")
    if len(lines) == 2:
        lines.append("  [key: string]: unknown;")
    lines.append("}")
    return "\n".join(lines) + "\n"


def gen_inline_request(name: str, schema: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    lines = [f"/** Multipart request `{name}`. */", f"export interface {name} {{"]
    for prop_name, prop_schema in props.items():
        is_req = prop_name in required
        opt = "" if is_req else "?"
        if prop_schema.get("format") == "binary":
            t = "Blob | Buffer | ReadableStream"
        else:
            t = ts_type(prop_schema, {}, required=is_req)
        lines.append(f"  {prop_name}{opt}: {t};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def ts_path_expr(path: str, path_params: list[str]) -> str:
    rel = path.lstrip("/")
    if not path_params:
        return f"`{rel}`"
    segments = re.split(r"(\{[^}]+\})", rel)
    parts = ["`"]
    for seg in segments:
        if seg.startswith("{") and seg.endswith("}"):
            pname = seg[1:-1]
            parts.append("${encodeURIComponent(" + pname + ")}")
        else:
            parts.append(seg.replace("`", "\\`"))
    parts.append("`")
    return "".join(parts)


def gen_service(tag: str, ops: list) -> str:
    class_name = pascal(tag.replace(" ", "")) + "Api"
    imports: set[str] = set()
    for op in ops:
        dto = op.get("dto")
        if dto and dto != "inline":
            imports.add(dto)
        elif op.get("inline_schema"):
            imports.add(op["inline_schema"]["name"])

    model_import = ""
    if imports:
        model_import = "import type { " + ", ".join(sorted(imports)) + " } from '../models/index.js';\n"

    lines = [
        "/** Generated API client. */",
        "import type { ApiResponse } from '../types.js';",
        "import type { DocmostHttpClient } from '../http-client.js';",
        model_import,
        "",
        f"export class {class_name} {{",
        "  constructor(private readonly http: DocmostHttpClient) {}",
        "",
    ]

    for op in ops:
        method_name = camel(op["operationId"])
        if method_name in TS_RESERVED or method_name == "import":
            method_name = method_name + "_"
        path = op["path"]
        http_method = op["method"]
        dto = op.get("dto")
        path_params = op.get("path_params", [])
        query_params = op.get("query_params", [])
        content = op.get("content")
        inline = op.get("inline_schema")

        params = []
        if dto and dto != "inline":
            params.append(f"request: {dto}")
        elif inline:
            params.append(f"request: {inline['name']}")
        for pp in path_params:
            params.append(f"{pp}: string")
        for qp in query_params:
            params.append(f"{qp}?: string")
        sig = ", ".join(params)

        is_raw_get = http_method == "GET" and ("/files/" in path or "/attachments/img/" in path)
        ret = "Promise<Response>" if is_raw_get else "Promise<ApiResponse<unknown>>"

        lines.append(f"  async {method_name}({sig}): {ret} {{")
        path_expr = ts_path_expr(path, path_params)

        if http_method == "GET":
            if query_params:
                lines.append(f"    const path = {path_expr};")
                lines.append("    const params: Record<string, string> = {};")
                for qp in query_params:
                    lines.append(f"    if ({qp} !== undefined) params['{qp}'] = {qp};")
                if is_raw_get:
                    lines.append("    return this.http.getRaw(path, Object.keys(params).length ? params : undefined);")
                else:
                    lines.append("    return this.http.get(path, Object.keys(params).length ? params : undefined);")
            elif is_raw_get:
                lines.append(f"    return this.http.getRaw({path_expr});")
            else:
                lines.append(f"    return this.http.get({path_expr});")
        elif content == "multipart/form-data":
            lines.append(
                f"    return this.http.postMultipart({path_expr}, request as unknown as Record<string, unknown>);"
            )
        else:
            body = "undefined"
            if dto and dto != "inline":
                body = "request"
            elif inline:
                body = "request"
            lines.append(f"    return this.http.post({path_expr}, {body});")
        lines.append("  }")
        lines.append("")

    lines.append("}")
    return "\n".join(lines) + "\n"


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    schemas = spec["components"]["schemas"]
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    SERVICES_DIR.mkdir(parents=True, exist_ok=True)

    model_names: list[str] = []
    for name, schema in schemas.items():
        if name in ("ApiResponse", "ErrorResponse"):
            continue
        file_key = schema_file_key(name) + ".ts"
        (MODELS_DIR / file_key).write_text(gen_interface(name, schema, schemas))
        model_names.append(name)

    (MODELS_DIR / "api-response.ts").write_text(
        """/** API envelope types. */
export interface ApiResponse<T = unknown> {
  data?: T | null;
  success: boolean;
  status: number;
}

export interface ErrorResponse {
  statusCode?: number;
  message?: string | string[];
  error?: string;
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
                        file_key = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", inline_name).lower() + ".ts"
                        (MODELS_DIR / file_key).write_text(gen_inline_request(inline_name, s))
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
        file_key = service_file_key(class_name)
        (SERVICES_DIR / file_key).write_text(gen_service(tag, ops))
        service_exports.append((file_key.replace(".ts", ""), class_name))

    model_exports = []
    for name in sorted(set(model_names)):
        model_exports.append(f"export type {{ {name} }} from './{schema_file_key(name)}.js';")

    (MODELS_DIR / "index.ts").write_text(
        "/** Generated models from OpenAPI. */\n"
        + "export type { ApiResponse, ErrorResponse } from './api-response.js';\n"
        + "\n".join(model_exports)
        + "\n"
    )

    svc_lines = ["/** Generated service clients. */"]
    for mod, cls in service_exports:
        svc_lines.append(f"export {{ {cls} }} from './{mod}.js';")
    (SERVICES_DIR / "index.ts").write_text("\n".join(svc_lines) + "\n")

    print(f"Generated {len(list(MODELS_DIR.glob('*.ts')))} models, {len(service_exports)} services")


if __name__ == "__main__":
    main()
