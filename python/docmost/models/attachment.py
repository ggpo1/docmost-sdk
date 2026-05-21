"""Generated from OpenAPI schema Attachment."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Attachment(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    file_name: Optional[str] = Field(default=None, alias="fileName")
    file_ext: Optional[str] = Field(default=None, alias="fileExt")
    file_path: Optional[str] = Field(default=None, alias="filePath")
    file_size: Optional[str] = Field(default=None, alias="fileSize")
    mime_type: Optional[str] = Field(default=None, alias="mimeType")
    type: Optional[str] = Field(default=None, alias="type")
    page_id: Optional[str] = Field(default=None, alias="pageId")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
