"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import CreateApiKeyDto, PaginationOptions, RevokeApiKeyDto, UpdateApiKeyDto


class APIKeysApi:
    """API Keys API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_api_keys(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("api-keys", body=request.model_dump(by_alias=True, exclude_none=True))

    def create_api_key(self, request: CreateApiKeyDto) -> ApiResponse[Any]:
        return self._http.post("api-keys/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_api_key(self, request: UpdateApiKeyDto) -> ApiResponse[Any]:
        return self._http.post("api-keys/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def revoke_api_key(self, request: RevokeApiKeyDto) -> ApiResponse[Any]:
        return self._http.post("api-keys/revoke", body=request.model_dump(by_alias=True, exclude_none=True))

