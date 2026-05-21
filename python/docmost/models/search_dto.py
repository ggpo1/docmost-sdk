"""Generated from OpenAPI schema SearchDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SearchDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(alias="query")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    limit: Optional[int] = Field(default=None, alias="limit")
    offset: Optional[int] = Field(default=None, alias="offset")
