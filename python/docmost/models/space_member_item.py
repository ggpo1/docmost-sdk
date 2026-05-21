"""Generated from OpenAPI schema SpaceMemberItem."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SpaceMemberItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")
    email: Optional[str] = Field(default=None, alias="email")
    avatar_url: Optional[str] = Field(default=None, alias="avatarUrl")
    member_count: Optional[int] = Field(default=None, alias="memberCount")
    is_default: Optional[bool] = Field(default=None, alias="isDefault")
    role: Optional[str] = Field(default=None, alias="role")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
