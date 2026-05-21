"""Generated from OpenAPI schema MfaDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MfaDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    code: str = Field(alias="code")
