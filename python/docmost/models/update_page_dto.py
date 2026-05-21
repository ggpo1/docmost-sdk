"""Generated from OpenAPI schema UpdatePageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdatePageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
    content: Optional[str] = Field(default=None, alias="content")
    format: Optional[str] = Field(default=None, alias="format")
    operation: Optional[str] = Field(default=None, alias="operation")
