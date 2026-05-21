"""Generated from OpenAPI schema CreatePageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreatePageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
    parent_page_id: Optional[str] = Field(default=None, alias="parentPageId")
    content: Optional[str] = Field(default=None, alias="content")
    format: Optional[str] = Field(default=None, alias="format")
