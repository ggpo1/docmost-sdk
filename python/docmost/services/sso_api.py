"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import CreateSsoProviderDto, LdapLoginDto, PaginationOptions, SsoProviderIdDto, UpdateSsoProviderDto


class SSOApi:
    """SSO API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_sso_providers(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("sso/providers", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_sso_provider(self, request: SsoProviderIdDto) -> ApiResponse[Any]:
        return self._http.post("sso/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def create_sso_provider(self, request: CreateSsoProviderDto) -> ApiResponse[Any]:
        return self._http.post("sso/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_sso_provider(self, request: UpdateSsoProviderDto) -> ApiResponse[Any]:
        return self._http.post("sso/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def delete_sso_provider(self, request: SsoProviderIdDto) -> ApiResponse[Any]:
        return self._http.post("sso/delete", body=request.model_dump(by_alias=True, exclude_none=True))

    def ldap_login(self, request: LdapLoginDto, providerId: str) -> ApiResponse[Any]:
        return self._http.post(f"sso/ldap/{DocmostHttpClient.escape_path_segment(providerId)}/login", body=request.model_dump(by_alias=True, exclude_none=True))

