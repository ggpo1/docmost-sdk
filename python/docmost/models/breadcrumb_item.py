"""Generated from OpenAPI schema BreadcrumbItem."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class BreadcrumbItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    slug_id: Optional[str] = Field(default=None, alias="slugId")
    title: Optional[str] = Field(default=None, alias="title")
    icon: Optional[str] = Field(default=None, alias="icon")
