"""Generated from OpenAPI schema EnableMfaDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class EnableMfaDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    secret: str = Field(alias="secret")
    verification_code: str = Field(alias="verificationCode")
