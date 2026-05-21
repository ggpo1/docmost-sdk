/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { CreateApiKeyDto, PaginationOptions, RevokeApiKeyDto, UpdateApiKeyDto } from '../models/index.js';


export class APIKeysApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getApiKeys(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`api-keys`, request);
  }

  async createApiKey(request: CreateApiKeyDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`api-keys/create`, request);
  }

  async updateApiKey(request: UpdateApiKeyDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`api-keys/update`, request);
  }

  async revokeApiKey(request: RevokeApiKeyDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`api-keys/revoke`, request);
  }

}
