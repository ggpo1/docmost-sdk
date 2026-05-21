"""Generated from OpenAPI schema SearchShareDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SearchShareDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(alias="query")
    share_id: str = Field(alias="shareId")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    limit: Optional[int] = Field(default=None, alias="limit")
    offset: Optional[int] = Field(default=None, alias="offset")
