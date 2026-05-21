"""Generated from OpenAPI schema LdapLoginDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LdapLoginDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    username: str = Field(alias="username")
    password: str = Field(alias="password")
