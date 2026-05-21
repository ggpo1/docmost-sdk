/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { AcceptInviteDto, CheckHostnameDto, InvitationIdDto, InviteUserDto, PaginationOptions, RemoveWorkspaceUserDto, UpdateWorkspaceDto, UpdateWorkspaceUserRoleDto } from '../models/index.js';


export class WorkspaceApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getWorkspacePublicInfo(): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/public`, undefined);
  }

  async getWorkspaceInfo(): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/info`, undefined);
  }

  async updateWorkspace(request: UpdateWorkspaceDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/update`, request);
  }

  async getWorkspaceMembers(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/members`, request);
  }

  async deactivateWorkspaceMember(): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/members/deactivate`, undefined);
  }

  async deleteWorkspaceMember(request: RemoveWorkspaceUserDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/members/delete`, request);
  }

  async updateWorkspaceMemberRole(request: UpdateWorkspaceUserRoleDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/members/change-role`, request);
  }

  async getInvitations(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites`, request);
  }

  async getInvitationById(request: InvitationIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites/info`, request);
  }

  async inviteUser(request: InviteUserDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites/create`, request);
  }

  async resendInvite(request: InvitationIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites/resend`, request);
  }

  async revokeInvite(request: InvitationIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites/revoke`, request);
  }

  async acceptInvite(request: AcceptInviteDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites/accept`, request);
  }

  async getInviteLink(request: InvitationIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/invites/link`, request);
  }

  async checkHostname(request: CheckHostnameDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/check-hostname`, request);
  }

}
