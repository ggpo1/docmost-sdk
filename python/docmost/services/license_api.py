"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import ActivateLicenseDto


class LicenseApi:
    """License API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_license_info(self) -> ApiResponse[Any]:
        return self._http.post("license/info", body=None)

    def activate_license(self, request: ActivateLicenseDto) -> ApiResponse[Any]:
        return self._http.post("license/activate", body=request.model_dump(by_alias=True, exclude_none=True))

    def remove_license(self) -> ApiResponse[Any]:
        return self._http.post("license/remove", body=None)

