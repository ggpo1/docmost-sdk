"""Generated from OpenAPI schema UpdateApiKeyDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateApiKeyDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    api_key_id: str = Field(alias="apiKeyId")
    name: str = Field(alias="name")
