"""Generated from OpenAPI schema PageHistoryIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PageHistoryIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    history_id: str = Field(alias="historyId")
