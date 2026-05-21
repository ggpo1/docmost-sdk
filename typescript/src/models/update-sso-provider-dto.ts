/** Generated from OpenAPI schema `UpdateSsoProviderDto`. */
export interface UpdateSsoProviderDto {
  providerId: string;
  name?: string | null | undefined;
  samlUrl?: string | null | undefined;
  samlCertificate?: string | null | undefined;
  oidcIssuer?: string | null | undefined;
  oidcClientId?: string | null | undefined;
  oidcClientSecret?: string | null | undefined;
  ldapUrl?: string | null | undefined;
  ldapBindDn?: string | null | undefined;
  ldapBindPassword?: string | null | undefined;
  ldapBaseDn?: string | null | undefined;
  ldapUserSearchFilter?: string | null | undefined;
  ldapUserAttributes?: Record<string, unknown> | null | undefined;
  ldapTlsEnabled?: boolean | null | undefined;
  ldapTlsCaCert?: string | null | undefined;
  allowSignup?: boolean | null | undefined;
  isEnabled?: boolean | null | undefined;
  groupSync?: boolean | null | undefined;
}
