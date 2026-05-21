"""Generated from OpenAPI schema AddSpaceMembersDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AddSpaceMembersDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
    role: str = Field(alias="role")
    user_ids: Optional[list[str]] = Field(default=None, alias="userIds")
    group_ids: Optional[list[str]] = Field(default=None, alias="groupIds")
