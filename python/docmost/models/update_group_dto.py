"""Generated from OpenAPI schema UpdateGroupDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateGroupDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    group_id: str = Field(alias="groupId")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
