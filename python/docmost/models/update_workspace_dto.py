"""Generated from OpenAPI schema UpdateWorkspaceDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UpdateWorkspaceDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: Optional[str] = Field(default=None, alias="name")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    description: Optional[str] = Field(default=None, alias="description")
    logo: Optional[str] = Field(default=None, alias="logo")
    email_domains: Optional[list[str]] = Field(default=None, alias="emailDomains")
    enforce_sso: Optional[bool] = Field(default=None, alias="enforceSso")
    enforce_mfa: Optional[bool] = Field(default=None, alias="enforceMfa")
    restrict_api_to_admins: Optional[bool] = Field(default=None, alias="restrictApiToAdmins")
    ai_search: Optional[bool] = Field(default=None, alias="aiSearch")
    generative_ai: Optional[bool] = Field(default=None, alias="generativeAi")
    disable_public_sharing: Optional[bool] = Field(default=None, alias="disablePublicSharing")
