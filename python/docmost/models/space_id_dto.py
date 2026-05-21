"""Generated from OpenAPI schema SpaceIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SpaceIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
