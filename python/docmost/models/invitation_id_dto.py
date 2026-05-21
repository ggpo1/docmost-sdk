"""Generated from OpenAPI schema InvitationIdDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class InvitationIdDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    invitation_id: str = Field(alias="invitationId")
