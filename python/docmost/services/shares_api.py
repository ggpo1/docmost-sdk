"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import CreateShareDto, PaginationOptions, ShareIdDto, ShareInfoDto, SharePageIdDto, UpdateShareDto


class SharesApi:
    """Shares API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_shares(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("shares", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_shared_page_info(self, request: ShareInfoDto) -> ApiResponse[Any]:
        return self._http.post("shares/page-info", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_share(self, request: ShareIdDto) -> ApiResponse[Any]:
        return self._http.post("shares/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_share_for_page(self, request: SharePageIdDto) -> ApiResponse[Any]:
        return self._http.post("shares/for-page", body=request.model_dump(by_alias=True, exclude_none=True))

    def create_share(self, request: CreateShareDto) -> ApiResponse[Any]:
        return self._http.post("shares/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_share(self, request: UpdateShareDto) -> ApiResponse[Any]:
        return self._http.post("shares/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def delete_share(self, request: ShareIdDto) -> ApiResponse[Any]:
        return self._http.post("shares/delete", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_share_page_tree(self, request: ShareIdDto) -> ApiResponse[Any]:
        return self._http.post("shares/tree", body=request.model_dump(by_alias=True, exclude_none=True))

