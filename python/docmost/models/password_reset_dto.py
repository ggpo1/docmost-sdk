"""Generated from OpenAPI schema PasswordResetDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PasswordResetDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    token: str = Field(alias="token")
    new_password: str = Field(alias="newPassword")
