"""Generated from OpenAPI schema DuplicatePageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DuplicatePageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
