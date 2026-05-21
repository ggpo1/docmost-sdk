"""Generated from OpenAPI schema CreateSsoProviderDto."""
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CreateSsoProviderDto(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="allow")

    name: str = Field(alias="name")
    type: str = Field(alias="type")
    saml_url: Optional[str] = Field(default=None, alias="samlUrl")
    saml_certificate: Optional[str] = Field(default=None, alias="samlCertificate")
    oidc_issuer: Optional[str] = Field(default=None, alias="oidcIssuer")
    oidc_client_id: Optional[str] = Field(default=None, alias="oidcClientId")
    oidc_client_secret: Optional[str] = Field(default=None, alias="oidcClientSecret")
    ldap_url: Optional[str] = Field(default=None, alias="ldapUrl")
    ldap_bind_dn: Optional[str] = Field(default=None, alias="ldapBindDn")
    ldap_bind_password: Optional[str] = Field(default=None, alias="ldapBindPassword")
    ldap_base_dn: Optional[str] = Field(default=None, alias="ldapBaseDn")
    ldap_user_search_filter: Optional[str] = Field(default=None, alias="ldapUserSearchFilter")
    ldap_user_attributes: Optional[dict[str, object]] = Field(default=None, alias="ldapUserAttributes")
    ldap_tls_enabled: Optional[bool] = Field(default=None, alias="ldapTlsEnabled")
    ldap_tls_ca_cert: Optional[str] = Field(default=None, alias="ldapTlsCaCert")
    allow_signup: Optional[bool] = Field(default=None, alias="allowSignup")
    is_enabled: Optional[bool] = Field(default=None, alias="isEnabled")
    group_sync: Optional[bool] = Field(default=None, alias="groupSync")
