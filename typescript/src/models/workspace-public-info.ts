/** Generated from OpenAPI schema `WorkspacePublicInfo`. */
export interface WorkspacePublicInfo {
  id?: string | null | undefined;
  name?: string | null | undefined;
  logo?: string | null | undefined;
  hostname?: string | null | undefined;
  enforceSso?: boolean | null | undefined;
  hasLicenseKey?: boolean | null | undefined;
  authProviders?: Record<string, unknown>[] | null | undefined;
}
