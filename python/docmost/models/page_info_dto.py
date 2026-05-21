"""Generated from OpenAPI schema PageInfoDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PageInfoDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    include_space: Optional[bool] = Field(default=None, alias="includeSpace")
    include_content: Optional[bool] = Field(default=None, alias="includeContent")
    format: Optional[str] = Field(default=None, alias="format")
