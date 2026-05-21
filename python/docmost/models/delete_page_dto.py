"""Generated from OpenAPI schema DeletePageDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DeletePageDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    page_id: str = Field(alias="pageId")
    permanently_delete: Optional[bool] = Field(default=None, alias="permanentlyDelete")
