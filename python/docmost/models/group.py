"""Generated from OpenAPI schema Group."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Group(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    is_default: Optional[bool] = Field(default=None, alias="isDefault")
    member_count: Optional[int] = Field(default=None, alias="memberCount")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
