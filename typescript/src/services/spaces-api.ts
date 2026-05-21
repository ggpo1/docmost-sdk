/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { AddSpaceMembersDto, CreateSpaceDto, PaginationOptions, RemoveSpaceMemberDto, SpaceIdDto, UpdateSpaceDto, UpdateSpaceMemberRoleDto } from '../models/index.js';


export class SpacesApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getWorkspaceSpaces(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces`, request);
  }

  async getSpaceInfo(request: SpaceIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/info`, request);
  }

  async createSpace(request: CreateSpaceDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/create`, request);
  }

  async updateSpace(request: UpdateSpaceDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/update`, request);
  }

  async deleteSpace(request: SpaceIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/delete`, request);
  }

  async getSpaceMembers(): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/members`, undefined);
  }

  async addSpaceMembers(request: AddSpaceMembersDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/members/add`, request);
  }

  async removeSpaceMember(request: RemoveSpaceMemberDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/members/remove`, request);
  }

  async updateSpaceMemberRole(request: UpdateSpaceMemberRoleDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/members/change-role`, request);
  }

}
