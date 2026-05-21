"""Generated from OpenAPI schema AddGroupUserDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AddGroupUserDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    group_id: str = Field(alias="groupId")
    user_ids: list[str] = Field(alias="userIds")
