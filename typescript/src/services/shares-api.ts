/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { CreateShareDto, PaginationOptions, ShareIdDto, ShareInfoDto, SharePageIdDto, UpdateShareDto } from '../models/index.js';


export class SharesApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getShares(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares`, request);
  }

  async getSharedPageInfo(request: ShareInfoDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/page-info`, request);
  }

  async getShare(request: ShareIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/info`, request);
  }

  async getShareForPage(request: SharePageIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/for-page`, request);
  }

  async createShare(request: CreateShareDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/create`, request);
  }

  async updateShare(request: UpdateShareDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/update`, request);
  }

  async deleteShare(request: ShareIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/delete`, request);
  }

  async getSharePageTree(request: ShareIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`shares/tree`, request);
  }

}
