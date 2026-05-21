"""Generated from OpenAPI schema ShareWithRelations."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ShareWithRelations(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    pass
