"""Generated from OpenAPI schema ExportSpaceDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ExportSpaceDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
    format: str = Field(alias="format")
    include_attachments: Optional[bool] = Field(default=None, alias="includeAttachments")
