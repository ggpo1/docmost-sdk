"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import ImportPageRequest, ImportZipRequest


class ImportApi:
    """Import API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def import_page(self, request: ImportPageRequest) -> ApiResponse[Any]:
        path = "pages/import"
        files: dict[str, tuple[str, bytes | Any, str]] = {}
        data: dict[str, str] = {}
        raw = request.file
        content = raw.read() if hasattr(raw, 'read') else raw
        files["file"] = ("upload.bin", content, "application/octet-stream")
        if request.space_id is not None: data["spaceId"] = str(request.space_id)
        if request.parent_page_id is not None: data["parentPageId"] = str(request.parent_page_id)
        return self._http.post_multipart(path, data=data or None, files=files or None)

    def import_zip(self, request: ImportZipRequest) -> ApiResponse[Any]:
        path = "pages/import-zip"
        files: dict[str, tuple[str, bytes | Any, str]] = {}
        data: dict[str, str] = {}
        raw = request.file
        content = raw.read() if hasattr(raw, 'read') else raw
        files["file"] = ("upload.bin", content, "application/octet-stream")
        if request.space_id is not None: data["spaceId"] = str(request.space_id)
        if request.source is not None: data["source"] = str(request.source)
        if request.parent_page_id is not None: data["parentPageId"] = str(request.parent_page_id)
        return self._http.post_multipart(path, data=data or None, files=files or None)

