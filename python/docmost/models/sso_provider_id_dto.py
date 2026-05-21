"""Generated from OpenAPI schema SsoProviderIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SsoProviderIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    provider_id: str = Field(alias="providerId")
