"""Generated from OpenAPI schema UpdateUserDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateUserDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")
    avatar_url: Optional[str] = Field(default=None, alias="avatarUrl")
    full_page_width: Optional[bool] = Field(default=None, alias="fullPageWidth")
    page_edit_mode: Optional[str] = Field(default=None, alias="pageEditMode")
    locale: Optional[str] = Field(default=None, alias="locale")
    confirm_password: Optional[str] = Field(default=None, alias="confirmPassword")
