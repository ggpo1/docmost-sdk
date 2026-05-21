"""Generated from OpenAPI schema RegenerateBackupCodesDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class RegenerateBackupCodesDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    confirm_password: Optional[str] = Field(default=None, alias="confirmPassword")
