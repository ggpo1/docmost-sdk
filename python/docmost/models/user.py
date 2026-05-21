"""Generated from OpenAPI schema User."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    email: Optional[str] = Field(default=None, alias="email")
    email_verified_at: Optional[str] = Field(default=None, alias="emailVerifiedAt")
    avatar_url: Optional[str] = Field(default=None, alias="avatarUrl")
    role: Optional[str] = Field(default=None, alias="role")
    locale: Optional[str] = Field(default=None, alias="locale")
    timezone: Optional[str] = Field(default=None, alias="timezone")
    settings: Optional[str] = Field(default=None, alias="settings")
    has_generated_password: Optional[str] = Field(default=None, alias="hasGeneratedPassword")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    last_login_at: Optional[str] = Field(default=None, alias="lastLoginAt")
    deactivated_at: Optional[str] = Field(default=None, alias="deactivatedAt")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
