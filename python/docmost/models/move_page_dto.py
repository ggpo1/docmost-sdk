"""Generated from OpenAPI schema MovePageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class MovePageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    position: str = Field(alias="position")
    parent_page_id: Optional[str] = Field(default=None, alias="parentPageId")
