"""Generated from OpenAPI schema UpdateSpaceMemberRoleDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateSpaceMemberRoleDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
    user_id: Optional[str] = Field(default=None, alias="userId")
    group_id: Optional[str] = Field(default=None, alias="groupId")
    role: str = Field(alias="role")
