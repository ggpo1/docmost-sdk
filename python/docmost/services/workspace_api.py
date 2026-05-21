"""Generated API client."""
from __future__ import annotations

from typing import Any, Optional

import httpx

from docmost.http_client import DocmostHttpClient
from docmost.types import ApiResponse
from docmost.models import AcceptInviteDto, CheckHostnameDto, InvitationIdDto, InviteUserDto, PaginationOptions, RemoveWorkspaceUserDto, UpdateWorkspaceDto, UpdateWorkspaceUserRoleDto


class WorkspaceApi:
    """Workspace API."""

    def __init__(self, http: DocmostHttpClient) -> None:
        self._http = http

    def get_workspace_public_info(self) -> ApiResponse[Any]:
        return self._http.post("workspace/public", body=None)

    def get_workspace_info(self) -> ApiResponse[Any]:
        return self._http.post("workspace/info", body=None)

    def update_workspace(self, request: UpdateWorkspaceDto) -> ApiResponse[Any]:
        return self._http.post("workspace/update", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_workspace_members(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("workspace/members", body=request.model_dump(by_alias=True, exclude_none=True))

    def deactivate_workspace_member(self) -> ApiResponse[Any]:
        return self._http.post("workspace/members/deactivate", body=None)

    def delete_workspace_member(self, request: RemoveWorkspaceUserDto) -> ApiResponse[Any]:
        return self._http.post("workspace/members/delete", body=request.model_dump(by_alias=True, exclude_none=True))

    def update_workspace_member_role(self, request: UpdateWorkspaceUserRoleDto) -> ApiResponse[Any]:
        return self._http.post("workspace/members/change-role", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_invitations(self, request: PaginationOptions) -> ApiResponse[Any]:
        return self._http.post("workspace/invites", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_invitation_by_id(self, request: InvitationIdDto) -> ApiResponse[Any]:
        return self._http.post("workspace/invites/info", body=request.model_dump(by_alias=True, exclude_none=True))

    def invite_user(self, request: InviteUserDto) -> ApiResponse[Any]:
        return self._http.post("workspace/invites/create", body=request.model_dump(by_alias=True, exclude_none=True))

    def resend_invite(self, request: InvitationIdDto) -> ApiResponse[Any]:
        return self._http.post("workspace/invites/resend", body=request.model_dump(by_alias=True, exclude_none=True))

    def revoke_invite(self, request: InvitationIdDto) -> ApiResponse[Any]:
        return self._http.post("workspace/invites/revoke", body=request.model_dump(by_alias=True, exclude_none=True))

    def accept_invite(self, request: AcceptInviteDto) -> ApiResponse[Any]:
        return self._http.post("workspace/invites/accept", body=request.model_dump(by_alias=True, exclude_none=True))

    def get_invite_link(self, request: InvitationIdDto) -> ApiResponse[Any]:
        return self._http.post("workspace/invites/link", body=request.model_dump(by_alias=True, exclude_none=True))

    def check_hostname(self, request: CheckHostnameDto) -> ApiResponse[Any]:
        return self._http.post("workspace/check-hostname", body=request.model_dump(by_alias=True, exclude_none=True))

