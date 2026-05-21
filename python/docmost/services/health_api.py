"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse


class HealthApi:
    """Health API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def health_check(self) -> ApiResponse[Any]:
        return self._http.get("health")

    def liveness(self) -> ApiResponse[Any]:
        return self._http.get("health/live")

