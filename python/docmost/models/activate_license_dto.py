"""Generated from OpenAPI schema ActivateLicenseDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ActivateLicenseDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    license_key: str = Field(alias="licenseKey")
