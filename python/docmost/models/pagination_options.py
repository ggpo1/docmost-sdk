"""Generated from OpenAPI schema PaginationOptions."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PaginationOptions(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    limit: Optional[int] = Field(default=None, alias="limit")
    cursor: Optional[str] = Field(default=None, alias="cursor")
    query: Optional[str] = Field(default=None, alias="query")
    admin_view: Optional[bool] = Field(default=None, alias="adminView")
