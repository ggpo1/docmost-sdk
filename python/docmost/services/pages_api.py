"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import CreatePageDto, DeletePageDto, DuplicatePageDto, MovePageDto, MovePageToSpaceDto, PageHistoryIdDto, PageIdDto, PageInfoDto, UpdatePageDto


class PagesApi:
    """Pages API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_page(self, request: PageInfoDto) -> ApiResponse[Any]:
        return self._http.post("pages/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def create_page(self, request: CreatePageDto) -> ApiResponse[Any]:
        return self._http.post("pages/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_page(self, request: UpdatePageDto) -> ApiResponse[Any]:
        return self._http.post("pages/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def delete_page(self, request: DeletePageDto) -> ApiResponse[Any]:
        return self._http.post("pages/delete", body=request.model_dump(by_alias=True, exclude_none=True))

    def restore_page(self, request: PageIdDto) -> ApiResponse[Any]:
        return self._http.post("pages/restore", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_recent_pages(self) -> ApiResponse[Any]:
        return self._http.post("pages/recent", body=None)

    def get_deleted_pages(self) -> ApiResponse[Any]:
        return self._http.post("pages/trash", body=None)

    def get_page_history(self) -> ApiResponse[Any]:
        return self._http.post("pages/history", body=None)

    def get_page_history_info(self, request: PageHistoryIdDto) -> ApiResponse[Any]:
        return self._http.post("pages/history/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_sidebar_pages(self) -> ApiResponse[Any]:
        return self._http.post("pages/sidebar-pages", body=None)

    def move_page_to_space(self, request: MovePageToSpaceDto) -> ApiResponse[Any]:
        return self._http.post("pages/move-to-space", body=request.model_dump(by_alias=True, exclude_none=True))

    def duplicate_page(self, request: DuplicatePageDto) -> ApiResponse[Any]:
        return self._http.post("pages/duplicate", body=request.model_dump(by_alias=True, exclude_none=True))

    def move_page(self, request: MovePageDto) -> ApiResponse[Any]:
        return self._http.post("pages/move", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_page_breadcrumbs(self, request: PageIdDto) -> ApiResponse[Any]:
        return self._http.post("pages/breadcrumbs", body=request.model_dump(by_alias=True, exclude_none=True))

