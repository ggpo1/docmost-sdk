"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import SearchDto


class AttachmentSearchApi:
    """Attachment Search API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def search_attachments(self, request: SearchDto) -> ApiResponse[Any]:
        return self._http.post("search-attachments", body=request.model_dump(by_alias=True, exclude_none=True))

    def trigger_attachment_indexing(self) -> ApiResponse[Any]:
        return self._http.post("search-attachments/indexing", body=None)

