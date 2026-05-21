"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import AddSpaceMembersDto, CreateSpaceDto, PaginationOptions, RemoveSpaceMemberDto, SpaceIdDto, UpdateSpaceDto, UpdateSpaceMemberRoleDto


class SpacesApi:
    """Spaces API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_workspace_spaces(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("spaces", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_space_info(self, request: SpaceIdDto) -> ApiResponse[Any]:
        return self._http.post("spaces/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def create_space(self, request: CreateSpaceDto) -> ApiResponse[Any]:
        return self._http.post("spaces/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_space(self, request: UpdateSpaceDto) -> ApiResponse[Any]:
        return self._http.post("spaces/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def delete_space(self, request: SpaceIdDto) -> ApiResponse[Any]:
        return self._http.post("spaces/delete", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_space_members(self) -> ApiResponse[Any]:
        return self._http.post("spaces/members", body=None)

    def add_space_members(self, request: AddSpaceMembersDto) -> ApiResponse[Any]:
        return self._http.post("spaces/members/add", body=request.model_dump(by_alias=True, exclude_none=True))

    def remove_space_member(self, request: RemoveSpaceMemberDto) -> ApiResponse[Any]:
        return self._http.post("spaces/members/remove", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_space_member_role(self, request: UpdateSpaceMemberRoleDto) -> ApiResponse[Any]:
        return self._http.post("spaces/members/change-role", body=request.model_dump(by_alias=True, exclude_none=True))

