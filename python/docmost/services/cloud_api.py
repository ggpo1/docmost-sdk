"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import CreateCloudWorkspaceDto


class CloudApi:
    """Cloud API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def create_cloud_workspace(self, request: CreateCloudWorkspaceDto) -> ApiResponse[Any]:
        return self._http.post("workspace/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_joined_workspaces(self) -> ApiResponse[Any]:
        return self._http.post("workspace/joined", body=None)

