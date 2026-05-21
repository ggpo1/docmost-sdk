/** Generated from OpenAPI schema `AuthProvider`. */
export interface AuthProvider {
  id?: string | null | undefined;
  name?: string | null | undefined;
  type?: string | null | undefined;
  isEnabled?: boolean | null | undefined;
  allowSignup?: boolean | null | undefined;
  groupSync?: boolean | null | undefined;
  samlUrl?: string | null | undefined;
  samlCertificate?: string | null | undefined;
  oidcIssuer?: string | null | undefined;
  oidcClientId?: string | null | undefined;
  oidcClientSecret?: string | null | undefined;
  ldapUrl?: string | null | undefined;
  ldapBindDn?: string | null | undefined;
  ldapBaseDn?: string | null | undefined;
  ldapUserSearchFilter?: string | null | undefined;
  ldapUserAttributes?: Record<string, unknown> | null | undefined;
  ldapTlsEnabled?: string | null | undefined;
  ldapTlsCaCert?: string | null | undefined;
  creatorId?: string | null | undefined;
  workspaceId?: string | null | undefined;
  createdAt?: string | null | undefined;
  updatedAt?: string | null | undefined;
}
