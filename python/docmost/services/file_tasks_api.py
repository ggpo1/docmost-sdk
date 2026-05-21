"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import FileTaskIdDto, PaginationOptions


class FileTasksApi:
    """File Tasks API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_file_tasks(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("file-tasks", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_file_task(self, request: FileTaskIdDto) -> ApiResponse[Any]:
        return self._http.post("file-tasks/info", body=request.model_dump(by_alias=True, exclude_none=True))

