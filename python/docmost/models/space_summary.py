"""Generated from OpenAPI schema SpaceSummary."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SpaceSummary(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    slug: Optional[str] = Field(default=None, alias="slug")
