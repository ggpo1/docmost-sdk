/** Generated from OpenAPI schema `UpdateWorkspaceDto`. */
export interface UpdateWorkspaceDto {
  name?: string | null | undefined;
  hostname?: string | null | undefined;
  description?: string | null | undefined;
  logo?: string | null | undefined;
  emailDomains?: string[] | null | undefined;
  enforceSso?: boolean | null | undefined;
  enforceMfa?: boolean | null | undefined;
  restrictApiToAdmins?: boolean | null | undefined;
  aiSearch?: boolean | null | undefined;
  generativeAi?: boolean | null | undefined;
  disablePublicSharing?: boolean | null | undefined;
}
