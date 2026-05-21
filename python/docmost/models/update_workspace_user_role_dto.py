"""Generated from OpenAPI schema UpdateWorkspaceUserRoleDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateWorkspaceUserRoleDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    user_id: str = Field(alias="userId")
    role: str = Field(alias="role")
