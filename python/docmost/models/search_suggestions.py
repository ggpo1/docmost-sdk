"""Generated from OpenAPI schema SearchSuggestions."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SearchSuggestions(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    users: Optional[list[dict[str, object]]] = Field(default=None, alias="users")
    groups: Optional[list[dict[str, object]]] = Field(default=None, alias="groups")
    pages: Optional[list[dict[str, object]]] = Field(default=None, alias="pages")
