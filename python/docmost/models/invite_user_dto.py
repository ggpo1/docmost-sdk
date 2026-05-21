"""Generated from OpenAPI schema InviteUserDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class InviteUserDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    emails: list[str] = Field(alias="emails")
    group_ids: Optional[list[str]] = Field(default=None, alias="groupIds")
    role: str = Field(alias="role")
