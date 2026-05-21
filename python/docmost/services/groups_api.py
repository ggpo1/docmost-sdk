"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import AddGroupUserDto, CreateGroupDto, GroupIdDto, PaginationOptions, RemoveGroupUserDto, UpdateGroupDto


class GroupsApi:
    """Groups API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_workspace_groups(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("groups", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_group_info(self, request: GroupIdDto) -> ApiResponse[Any]:
        return self._http.post("groups/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def create_group(self, request: CreateGroupDto) -> ApiResponse[Any]:
        return self._http.post("groups/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_group(self, request: UpdateGroupDto) -> ApiResponse[Any]:
        return self._http.post("groups/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_group_members(self) -> ApiResponse[Any]:
        return self._http.post("groups/members", body=None)

    def add_group_members(self, request: AddGroupUserDto) -> ApiResponse[Any]:
        return self._http.post("groups/members/add", body=request.model_dump(by_alias=True, exclude_none=True))

    def remove_group_member(self, request: RemoveGroupUserDto) -> ApiResponse[Any]:
        return self._http.post("groups/members/remove", body=request.model_dump(by_alias=True, exclude_none=True))

    def delete_group(self, request: GroupIdDto) -> ApiResponse[Any]:
        return self._http.post("groups/delete", body=request.model_dump(by_alias=True, exclude_none=True))

