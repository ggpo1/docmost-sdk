"""Generated from OpenAPI schema CreateSpaceDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateSpaceDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(alias="name")
    slug: str = Field(alias="slug")
    description: Optional[str] = Field(default=None, alias="description")
