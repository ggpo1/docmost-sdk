"""Generated from OpenAPI schema CreateGroupDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateGroupDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    user_ids: Optional[list[str]] = Field(default=None, alias="userIds")
