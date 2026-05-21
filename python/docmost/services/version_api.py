"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse


class VersionApi:
    """Version API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_version(self) -> ApiResponse[Any]:
        return self._http.post("version", body=None)

