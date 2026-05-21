"""Generated from OpenAPI schema ShareInfoDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ShareInfoDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    share_id: Optional[str] = Field(default=None, alias="shareId")
    page_id: Optional[str] = Field(default=None, alias="pageId")
