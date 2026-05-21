"""Generated from OpenAPI schema ShareIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ShareIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    share_id: str = Field(alias="shareId")
