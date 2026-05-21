"""Generated from OpenAPI schema SearchResult."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SearchResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
    parent_page_id: Optional[str] = Field(default=None, alias="parentPageId")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    rank: Optional[float] = Field(default=None, alias="rank")
    highlight: Optional[str] = Field(default=None, alias="highlight")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
    space: Optional[SpaceSummary] = Field(default=None, alias="space")
