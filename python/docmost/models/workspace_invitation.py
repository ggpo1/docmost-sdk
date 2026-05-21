"""Generated from OpenAPI schema WorkspaceInvitation."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class WorkspaceInvitation(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    email: Optional[str] = Field(default=None, alias="email")
    role: Optional[str] = Field(default=None, alias="role")
    token: Optional[str] = Field(default=None, alias="token")
    group_ids: Optional[str] = Field(default=None, alias="groupIds")
    invited_by_id: Optional[str] = Field(default=None, alias="invitedById")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
