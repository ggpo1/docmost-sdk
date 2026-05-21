"""Generated from OpenAPI schema SidebarPage."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SidebarPage(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    slug_id: Optional[str] = Field(default=None, alias="slugId")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
    position: Optional[str] = Field(default=None, alias="position")
    parent_page_id: Optional[str] = Field(default=None, alias="parentPageId")
    has_children: Optional[bool] = Field(default=None, alias="hasChildren")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
