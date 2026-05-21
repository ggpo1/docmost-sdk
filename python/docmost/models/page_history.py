"""Generated from OpenAPI schema PageHistory."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PageHistory(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    page_id: Optional[str] = Field(default=None, alias="pageId")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
    slug_id: Optional[str] = Field(default=None, alias="slugId")
    slug: Optional[str] = Field(default=None, alias="slug")
    content: Optional[dict[str, object]] = Field(default=None, alias="content")
    version: Optional[str] = Field(default=None, alias="version")
    last_updated_by_id: Optional[str] = Field(default=None, alias="lastUpdatedById")
    contributor_ids: Optional[str] = Field(default=None, alias="contributorIds")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
