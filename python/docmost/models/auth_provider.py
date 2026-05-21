"""Generated from OpenAPI schema AuthProvider."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AuthProvider(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    id: Optional[str] = Field(default=None, alias="id")
    name: Optional[str] = Field(default=None, alias="name")
    type: Optional[str] = Field(default=None, alias="type")
    is_enabled: Optional[bool] = Field(default=None, alias="isEnabled")
    allow_signup: Optional[bool] = Field(default=None, alias="allowSignup")
    group_sync: Optional[bool] = Field(default=None, alias="groupSync")
    saml_url: Optional[str] = Field(default=None, alias="samlUrl")
    saml_certificate: Optional[str] = Field(default=None, alias="samlCertificate")
    oidc_issuer: Optional[str] = Field(default=None, alias="oidcIssuer")
    oidc_client_id: Optional[str] = Field(default=None, alias="oidcClientId")
    oidc_client_secret: Optional[str] = Field(default=None, alias="oidcClientSecret")
    ldap_url: Optional[str] = Field(default=None, alias="ldapUrl")
    ldap_bind_dn: Optional[str] = Field(default=None, alias="ldapBindDn")
    ldap_base_dn: Optional[str] = Field(default=None, alias="ldapBaseDn")
    ldap_user_search_filter: Optional[str] = Field(default=None, alias="ldapUserSearchFilter")
    ldap_user_attributes: Optional[dict[str, object]] = Field(default=None, alias="ldapUserAttributes")
    ldap_tls_enabled: Optional[str] = Field(default=None, alias="ldapTlsEnabled")
    ldap_tls_ca_cert: Optional[str] = Field(default=None, alias="ldapTlsCaCert")
    creator_id: Optional[str] = Field(default=None, alias="creatorId")
    workspace_id: Optional[str] = Field(default=None, alias="workspaceId")
    created_at: Optional[str] = Field(default=None, alias="createdAt")
    updated_at: Optional[str] = Field(default=None, alias="updatedAt")
