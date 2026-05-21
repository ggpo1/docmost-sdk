"""Generated from OpenAPI schema OffsetPaginationMeta."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class OffsetPaginationMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    limit: Optional[int] = Field(default=None, alias="limit")
    page: Optional[int] = Field(default=None, alias="page")
    has_next_page: Optional[bool] = Field(default=None, alias="hasNextPage")
    has_prev_page: Optional[bool] = Field(default=None, alias="hasPrevPage")
