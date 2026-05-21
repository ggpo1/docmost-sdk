"""Generated from OpenAPI schema SearchSuggestionDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SearchSuggestionDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    query: str = Field(alias="query")
    include_users: Optional[bool] = Field(default=None, alias="includeUsers")
    include_groups: Optional[bool] = Field(default=None, alias="includeGroups")
    include_pages: Optional[bool] = Field(default=None, alias="includePages")
    space_id: Optional[str] = Field(default=None, alias="spaceId")
    limit: Optional[int] = Field(default=None, alias="limit")
