"""Generated from OpenAPI schema ExportPageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ExportPageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    format: str = Field(alias="format")
    include_children: Optional[bool] = Field(default=None, alias="includeChildren")
    include_attachments: Optional[bool] = Field(default=None, alias="includeAttachments")
