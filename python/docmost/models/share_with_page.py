"""Generated from OpenAPI schema ShareWithPage."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ShareWithPage(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    pass
