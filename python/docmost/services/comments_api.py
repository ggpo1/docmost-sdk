"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import CommentIdDto, CreateCommentDto, FindPageCommentsRequest, UpdateCommentDto


class CommentsApi:
    """Comments API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def create_comment(self, request: CreateCommentDto) -> ApiResponse[Any]:
        return self._http.post("comments/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def find_page_comments(self, request: FindPageCommentsRequest) -> ApiResponse[Any]:
        return self._http.post("comments", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_comment(self, request: CommentIdDto) -> ApiResponse[Any]:
        return self._http.post("comments/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_comment(self, request: UpdateCommentDto) -> ApiResponse[Any]:
        return self._http.post("comments/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def delete_comment(self, request: CommentIdDto) -> ApiResponse[Any]:
        return self._http.post("comments/delete", body=request.model_dump(by_alias=True, exclude_none=True))

