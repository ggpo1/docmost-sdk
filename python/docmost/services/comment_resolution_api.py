"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import ResolveCommentDto


class CommentResolutionApi:
    """Comment Resolution API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def resolve_comment(self, request: ResolveCommentDto) -> ApiResponse[Any]:
        return self._http.post("comments/resolve", body=request.model_dump(by_alias=True, exclude_none=True))

