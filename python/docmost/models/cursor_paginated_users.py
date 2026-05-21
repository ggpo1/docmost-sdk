"""Generated from OpenAPI schema CursorPaginatedUsers."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CursorPaginatedUsers(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    items: Optional[list[User]] = Field(default=None, alias="items")
    meta: Optional[CursorPaginationMeta] = Field(default=None, alias="meta")
