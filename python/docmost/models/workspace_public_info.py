"""Generated from OpenAPI schema WorkspacePublicInfo."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class WorkspacePublicInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    logo: Optional[str] = Field(default=None, alias="logo")
    hostname: Optional[str] = Field(default=None, alias="hostname")
    enforce_sso: Optional[bool] = Field(default=None, alias="enforceSso")
    has_license_key: Optional[bool] = Field(default=None, alias="hasLicenseKey")
    auth_providers: Optional[list[dict[str, object]]] = Field(default=None, alias="authProviders")
