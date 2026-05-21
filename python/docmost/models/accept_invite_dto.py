"""Generated from OpenAPI schema AcceptInviteDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AcceptInviteDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    invitation_id: str = Field(alias="invitationId")
    name: str = Field(alias="name")
    password: str = Field(alias="password")
    token: str = Field(alias="token")
