"""Generated from OpenAPI schema SharePageIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SharePageIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
