"""Generated from OpenAPI schema Workspace."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class Workspace(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    description: Optional[str] = Field(default=None, alias="description")
    logo: Optional[str] = Field(default=None, alias="logo")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    custom_domain: Optional[str] = Field(default=None, alias="customDomain")
    default_role: Optional[str] = Field(default=None, alias="defaultRole")
    default_space_id: Optional[str] = Field(default=None, alias="defaultSpaceId")
    email_domains: Optional[str] = Field(default=None, alias="emailDomains")
    enforce_sso: Optional[bool] = Field(default=None, alias="enforceSso")
    enforce_mfa: Optional[str] = Field(default=None, alias="enforceMfa")
    settings: Optional[str] = Field(default=None, alias="settings")
    plan: Optional[str] = Field(default=None, alias="plan")
    status: Optional[str] = Field(default=None, alias="status")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
