"""Generated from OpenAPI schema Page."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Page(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    slug_id: Optional[str] = Field(default=None, alias="slugId")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
    cover_photo: Optional[str] = Field(default=None, alias="coverPhoto")
    content: Optional[dict[str, object]] = Field(default=None, alias="content")
    position: Optional[str] = Field(default=None, alias="position")
    parent_page_id: Optional[str] = Field(default=None, alias="parentPageId")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    last_updated_by_id: Optional[str] = Field(default=None, alias="lastUpdatedById")
    is_locked: Optional[bool] = Field(default=None, alias="isLocked")
    contributor_ids: Optional[str] = Field(default=None, alias="contributorIds")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
    deleted_at: Optional[str] = Field(default=None, alias="deletedAt")
