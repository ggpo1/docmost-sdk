/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { AddGroupUserDto, CreateGroupDto, GroupIdDto, PaginationOptions, RemoveGroupUserDto, UpdateGroupDto } from '../models/index.js';


export class GroupsApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getWorkspaceGroups(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups`, request);
  }

  async getGroupInfo(request: GroupIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/info`, request);
  }

  async createGroup(request: CreateGroupDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/create`, request);
  }

  async updateGroup(request: UpdateGroupDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/update`, request);
  }

  async getGroupMembers(): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/members`, undefined);
  }

  async addGroupMembers(request: AddGroupUserDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/members/add`, request);
  }

  async removeGroupMember(request: RemoveGroupUserDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/members/remove`, request);
  }

  async deleteGroup(request: GroupIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`groups/delete`, request);
  }

}
