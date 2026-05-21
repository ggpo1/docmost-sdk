"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import ExportPageDto, ExportSpaceDto


class ExportApi:
    """Export API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def export_page(self, request: ExportPageDto) -> ApiResponse[Any]:
        return self._http.post("pages/export", body=request.model_dump(by_alias=True, exclude_none=True))

    def export_space(self, request: ExportSpaceDto) -> ApiResponse[Any]:
        return self._http.post("spaces/export", body=request.model_dump(by_alias=True, exclude_none=True))

