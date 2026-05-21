"""Generated from OpenAPI schema ApiKey."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ApiKey(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    expires_at: Optional[str] = Field(default=None, alias="expiresAt")
    last_used_at: Optional[str] = Field(default=None, alias="lastUsedAt")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
