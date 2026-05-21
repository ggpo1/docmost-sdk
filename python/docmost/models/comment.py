"""Generated from OpenAPI schema Comment."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Comment(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    page_id: Optional[str] = Field(default=None, alias="pageId")
    content: Optional[dict[str, object]] = Field(default=None, alias="content")
    selection: Optional[str] = Field(default=None, alias="selection")
    type: Optional[str] = Field(default=None, alias="type")
    parent_comment_id: Optional[str] = Field(default=None, alias="parentCommentId")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    last_edited_by_id: Optional[str] = Field(default=None, alias="lastEditedById")
    edited_at: Optional[str] = Field(default=None, alias="editedAt")
    resolved_at: Optional[str] = Field(default=None, alias="resolvedAt")
    resolved_by_id: Optional[str] = Field(default=None, alias="resolvedById")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
