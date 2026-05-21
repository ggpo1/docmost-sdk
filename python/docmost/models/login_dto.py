"""Generated from OpenAPI schema LoginDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LoginDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    email: str = Field(alias="email")
    password: str = Field(alias="password")
