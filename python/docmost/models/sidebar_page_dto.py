"""Generated from OpenAPI schema SidebarPageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SidebarPageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: Optional[str] = Field(default=None, alias="spaceId")
    page_id: Optional[str] = Field(default=None, alias="pageId")
