"""Generated from OpenAPI schema UpdateSpaceDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateSpaceDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    space_id: str = Field(alias="spaceId")
    name: Optional[str] = Field(default=None, alias="name")
    slug: Optional[str] = Field(default=None, alias="slug")
    description: Optional[str] = Field(default=None, alias="description")
    disable_public_sharing: Optional[bool] = Field(default=None, alias="disablePublicSharing")
