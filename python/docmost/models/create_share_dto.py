"""Generated from OpenAPI schema CreateShareDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateShareDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    include_sub_pages: Optional[bool] = Field(default=None, alias="includeSubPages")
    search_indexing: Optional[bool] = Field(default=None, alias="searchIndexing")
