"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import SearchDto, SearchShareDto, SearchSuggestionDto


class SearchApi:
    """Search API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def page_search(self, request: SearchDto) -> ApiResponse[Any]:
        return self._http.post("search", body=request.model_dump(by_alias=True, exclude_none=True))

    def search_suggestions(self, request: SearchSuggestionDto) -> ApiResponse[Any]:
        return self._http.post("search/suggest", body=request.model_dump(by_alias=True, exclude_none=True))

    def search_share(self, request: SearchShareDto) -> ApiResponse[Any]:
        return self._http.post("search/share-search", body=request.model_dump(by_alias=True, exclude_none=True))

