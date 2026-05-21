"""Generated from OpenAPI schema VerifyUserTokenDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class VerifyUserTokenDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    token: str = Field(alias="token")
    type: str = Field(alias="type")
