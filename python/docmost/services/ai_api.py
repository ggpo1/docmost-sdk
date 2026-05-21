"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import SearchDto


class AIApi:
    """AI API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def ai_answers(self, request: SearchDto) -> ApiResponse[Any]:
        return self._http.post("ai/answers", body=request.model_dump(by_alias=True, exclude_none=True))

