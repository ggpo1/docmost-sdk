"""Generated from OpenAPI schema RemoveSpaceMemberDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RemoveSpaceMemberDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
    user_id: Optional[str] = Field(default=None, alias="userId")
    group_id: Optional[str] = Field(default=None, alias="groupId")
