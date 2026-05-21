"""Generated from OpenAPI schema UpdateShareDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateShareDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    share_id: str = Field(alias="shareId")
    page_id: Optional[str] = Field(default=None, alias="pageId")
    include_sub_pages: Optional[bool] = Field(default=None, alias="includeSubPages")
    search_indexing: Optional[bool] = Field(default=None, alias="searchIndexing")
