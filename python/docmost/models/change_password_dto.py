"""Generated from OpenAPI schema ChangePasswordDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ChangePasswordDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    old_password: str = Field(alias="oldPassword")
    new_password: str = Field(alias="newPassword")
