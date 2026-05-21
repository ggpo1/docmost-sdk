"""Generated from OpenAPI schema CreateAdminUserDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateAdminUserDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(alias="name")
    email: str = Field(alias="email")
    password: str = Field(alias="password")
    workspace_name: Optional[str] = Field(default=None, alias="workspaceName")
    hostname: Optional[str] = Field(default=None, alias="hostname")
