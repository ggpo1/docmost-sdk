#!/usr/bin/env python3
"""Generate Docmost.Sdk C# sources from OpenAPI spec."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = ROOT / "api-1.json"
OUT_DIR = Path(__file__).resolve().parents[1] / "src" / "Docmost.Sdk"

RESERVED = {
    "object", "string", "event", "delegate", "params", "ref", "out", "in",
    "base", "lock", "checked", "fixed", "internal", "operator", "namespace",
}


def pascal(s: str) -> str:
    parts = re.split(r"[^a-zA-Z0-9]+", s)
    name = "".join(p[:1].upper() + p[1:] for p in parts if p)
    if not name:
        return "Item"
    if name[0].isdigit():
        name = "Item" + name
    if name.lower() in RESERVED:
        name += "Value"
    return name


def csharp_type(schema: dict, schemas: dict, nullable: bool = False) -> str:
    if "$ref" in schema:
        ref = schema["$ref"].split("/")[-1]
        t = ref
    elif "oneOf" in schema:
        return "System.Text.Json.JsonElement?"
    elif "allOf" in schema:
        for part in schema["allOf"]:
            if "$ref" in part:
                return part["$ref"].split("/")[-1]
        return "System.Text.Json.JsonElement?"
    elif "enum" in schema:
        return "string"
    elif schema.get("type") == "array":
        item = csharp_type(schema["items"], schemas)
        t = f"List<{item}>"
    elif schema.get("type") == "object":
        if "additionalProperties" in schema:
            val = csharp_type(schema["additionalProperties"], schemas)
            t = f"Dictionary<string, {val}>"
        else:
            t = "Dictionary<string, object?>"
    elif schema.get("type") == "integer":
        t = "int"
    elif schema.get("type") == "number":
        t = "double"
    elif schema.get("type") == "boolean":
        t = "bool"
    else:
        fmt = schema.get("format")
        if fmt in ("uuid", "email", "date-time", "uri", "base64"):
            t = "string"
        else:
            t = "string"

    if nullable or schema.get("nullable") or is_nullable_union(schema):
        if t.endswith("?"):
            return t
        if t.startswith("List<") or t.startswith("Dictionary<"):
            return t + "?"
        return t + "?"
    return t


def is_nullable_union(schema: dict) -> bool:
    t = schema.get("type")
    return isinstance(t, list) and "null" in t


def resolve_schema(name: str, schemas: dict) -> dict:
    return schemas[name]


def gen_property(prop_name: str, prop_schema: dict, schemas: dict, required: set) -> str:
    nullable = prop_name not in required or is_nullable_union(prop_schema)
    if prop_schema.get("type") == "array" or "$ref" in prop_schema:
        nullable = nullable or is_nullable_union(prop_schema)
    cs_type = csharp_type(prop_schema, schemas, nullable=nullable)
    attr = "public"
    json_name = prop_name
    return (
        f'    [System.Text.Json.Serialization.JsonPropertyName("{json_name}")]\n'
        f"    {attr} {cs_type} {pascal(prop_name)} {{ get; set; }}"
    )


def gen_model(name: str, schema: dict, schemas: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    lines = [
        "namespace Docmost.Sdk.Models;",
        "",
        f"public class {name}",
        "{",
    ]
    for prop_name, prop_schema in props.items():
        lines.append(gen_property(prop_name, prop_schema, schemas, required) + "\n")
    lines.append("}")
    return "\n".join(lines) + "\n"


def gen_inline_request(name: str, schema: dict) -> str:
    props = schema.get("properties", {})
    required = set(schema.get("required", []))
    lines = [
        "namespace Docmost.Sdk.Models;",
        "",
        f"public class {name}",
        "{",
    ]
    for prop_name, prop_schema in props.items():
        nullable = prop_name not in required
        cs_type = csharp_type(prop_schema, {}, nullable=nullable)
        if prop_schema.get("type") == "string" and prop_schema.get("format") == "binary":
            cs_type = "System.IO.Stream"
        lines.append(
            f'    [System.Text.Json.Serialization.JsonPropertyName("{prop_name}")]\n'
            f"    public {cs_type} {pascal(prop_name)} {{ get; set; }} = default!;\n"
        )
    lines.append("}")
    return "\n".join(lines) + "\n"


def csharp_path_expr(path: str, path_params: list[str]) -> str:
    rel = path.lstrip("/")
    if not path_params:
        return f'"{rel}"'
    for pp in path_params:
        rel = rel.replace("{" + pp + "}", '" + Uri.EscapeDataString(' + pp + ') + "')
    return '"' + rel + '"'


def gen_service(tag: str, ops: list, schemas: dict) -> str:
    class_name = pascal(tag.replace(" ", "")) + "Api"
    lines = [
        "using Docmost.Sdk.Http;",
        "using Docmost.Sdk.Models;",
        "using System.Net.Http.Headers;",
        "using System.Net.Http.Json;",
        "using System.Text.Json;",
        "",
        "namespace Docmost.Sdk.Services;",
        "",
        f"public sealed class {class_name}(DocmostHttpClient http)",
        "{",
        f"    private readonly DocmostHttpClient _http = http;",
        "",
    ]

    for op in ops:
        method_name = op["operationId"]
        path = op["path"]
        http_method = op["method"]
        dto = op.get("dto")
        path_params = op.get("path_params", [])
        query_params = op.get("query_params", [])
        content = op.get("content")
        inline = op.get("inline_schema")

        # Build signature
        params = []
        if dto and dto != "inline":
            params.append(f"{dto} request")
        elif inline:
            params.append(f"{inline['name']} request")
        for pp in path_params:
            params.append(f"string {pp}")
        for qp in query_params:
            params.append(f"string? {qp} = null")
        params.append("CancellationToken cancellationToken = default")
        sig = ", ".join(params)

        is_raw_get = http_method == "GET" and (
            "/files/" in path or "/attachments/img/" in path
        )
        return_type = "Task<HttpResponseMessage>" if is_raw_get else "Task<ApiResponse<JsonElement?>>"

        lines.append(f"    public async {return_type} {pascal(method_name)}Async({sig})")
        lines.append("    {")
        path_expr = csharp_path_expr(path, path_params)

        if http_method == "GET":
            if query_params:
                lines.append(f"        var rel = {path_expr};")
                lines.append("        var query = new List<string>();")
                for qp in query_params:
                    lines.append(
                        f'        if ({qp} is not null) query.Add("{qp}=" + Uri.EscapeDataString({qp}));'
                    )
                lines.append(
                    '        var finalPath = query.Count > 0 ? rel + "?" + string.Join("&", query) : rel;'
                )
                path_expr = "finalPath"
            if is_raw_get:
                lines.append(
                    f"        return await _http.GetRawAsync({path_expr}, cancellationToken).ConfigureAwait(false);"
                )
            else:
                lines.append(
                    f"        return await _http.GetAsync<JsonElement?>({path_expr}, cancellationToken).ConfigureAwait(false);"
                )
        elif content == "multipart/form-data":
            inline_name = inline["name"] if inline else None
            lines.append("        using var form = new MultipartFormDataContent();")
            if inline and inline.get("properties"):
                for prop_name, prop_schema in inline["properties"].items():
                    pn = pascal(prop_name)
                    if prop_schema.get("format") == "binary":
                        lines.append(f"        var fileContent = new StreamContent(request.{pn});")
                        lines.append(
                            '        fileContent.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");'
                        )
                        lines.append(f'        form.Add(fileContent, "{prop_name}", "upload.bin");')
                    else:
                        lines.append(
                            f'        form.Add(new StringContent(request.{pn}?.ToString() ?? string.Empty), "{prop_name}");'
                        )
            lines.append(
                f"        return await _http.PostMultipartAsync<JsonElement?>({path_expr}, form, cancellationToken).ConfigureAwait(false);"
            )
        else:
            body = "null"
            if dto and dto != "inline":
                body = "request"
            elif inline:
                body = "request"
            lines.append(
                f"        return await _http.PostAsync<JsonElement?>({path_expr}, {body}, cancellationToken).ConfigureAwait(false);"
            )

        lines.append("    }\n")

    lines.append("}")
    return "\n".join(lines) + "\n"


def main():
    spec = json.loads(SPEC_PATH.read_text())
    schemas = spec["components"]["schemas"]

    models_dir = OUT_DIR / "Models"
    services_dir = OUT_DIR / "Services"
    models_dir.mkdir(parents=True, exist_ok=True)
    services_dir.mkdir(parents=True, exist_ok=True)

    # Core models not in OpenAPI as standalone request DTOs
    for name, schema in schemas.items():
        if name in ("ApiResponse",):
            continue
        (models_dir / f"{name}.cs").write_text(gen_model(name, schema, schemas))

    # ApiResponse generic wrapper
    (models_dir / "ApiResponse.cs").write_text(
        """namespace Docmost.Sdk.Models;

public sealed class ApiResponse<T>
{
    [System.Text.Json.Serialization.JsonPropertyName("data")]
    public T? Data { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("success")]
    public bool Success { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("status")]
    public int Status { get; set; }
}
"""
    )

    (models_dir / "ErrorResponse.cs").write_text(
        """namespace Docmost.Sdk.Models;

public sealed class ErrorResponse
{
    [System.Text.Json.Serialization.JsonPropertyName("statusCode")]
    public int StatusCode { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("message")]
    public System.Text.Json.JsonElement? Message { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("error")]
    public string? Error { get; set; }
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
                        (models_dir / f"{inline_name}.cs").write_text(gen_inline_request(inline_name, s))
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

    for tag, ops in ops_by_tag.items():
        fname = pascal(tag.replace(" ", "")) + "Api.cs"
        (services_dir / fname).write_text(gen_service(tag, ops, schemas))

    print(f"Generated {len(list(models_dir.glob('*.cs')))} models and {len(list(services_dir.glob('*.cs')))} services")


if __name__ == "__main__":
    main()
