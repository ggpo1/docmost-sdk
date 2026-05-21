"""Generated from OpenAPI schema WorkspaceWithMeta."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class WorkspaceWithMeta(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    pass
