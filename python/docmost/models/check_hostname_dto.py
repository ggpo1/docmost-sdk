"""Generated from OpenAPI schema CheckHostnameDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CheckHostnameDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    hostname: str = Field(alias="hostname")
