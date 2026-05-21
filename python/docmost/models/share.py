"""Generated from OpenAPI schema Share."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Share(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    key: Optional[str] = Field(default=None, alias="key")
    page_id: Optional[str] = Field(default=None, alias="pageId")
    include_sub_pages: Optional[str] = Field(default=None, alias="includeSubPages")
    search_indexing: Optional[str] = Field(default=None, alias="searchIndexing")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
