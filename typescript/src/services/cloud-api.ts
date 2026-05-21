/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { CreateCloudWorkspaceDto } from '../models/index.js';


export class CloudApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async createCloudWorkspace(request: CreateCloudWorkspaceDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/create`, request);
  }

  async getJoinedWorkspaces(): Promise<ApiResponse<unknown>> {
    return this.http.post(`workspace/joined`, undefined);
  }

}
