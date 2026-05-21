"""Generated from OpenAPI schema Space."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Space(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    slug: Optional[str] = Field(default=None, alias="slug")
    description: Optional[str] = Field(default=None, alias="description")
    logo: Optional[str] = Field(default=None, alias="logo")
    default_role: Optional[str] = Field(default=None, alias="defaultRole")
    visibility: Optional[str] = Field(default=None, alias="visibility")
    settings: Optional[str] = Field(default=None, alias="settings")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
