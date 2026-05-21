"""Generated from OpenAPI schema CreateCloudWorkspaceDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateCloudWorkspaceDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(alias="name")
    email: str = Field(alias="email")
    password: str = Field(alias="password")
