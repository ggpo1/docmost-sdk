"""Generated from OpenAPI schema CursorPaginationMeta."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CursorPaginationMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    limit: Optional[int] = Field(default=None, alias="limit")
    has_next_page: Optional[bool] = Field(default=None, alias="hasNextPage")
    has_prev_page: Optional[bool] = Field(default=None, alias="hasPrevPage")
    next_cursor: Optional[str] = Field(default=None, alias="nextCursor")
    prev_cursor: Optional[str] = Field(default=None, alias="prevCursor")
