"""Generated from OpenAPI schema RevokeApiKeyDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RevokeApiKeyDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key_id: str = Field(alias="apiKeyId")
