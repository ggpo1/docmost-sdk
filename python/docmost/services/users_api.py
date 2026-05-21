"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import UpdateUserDto


class UsersApi:
    """Users API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_user_info(self) -> ApiResponse[Any]:
        return self._http.post("users/me", body=None)

    def update_user(self, request: UpdateUserDto) -> ApiResponse[Any]:
        return self._http.post("users/update", body=request.model_dump(by_alias=True, exclude_none=True))

