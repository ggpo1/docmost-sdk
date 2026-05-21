"""Generated from OpenAPI schema CreateApiKeyDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateApiKeyDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(alias="name")
    expires_at: Optional[str] = Field(default=None, alias="expiresAt")
