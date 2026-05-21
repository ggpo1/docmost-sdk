/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { ExportPageDto, ExportSpaceDto } from '../models/index.js';


export class ExportApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async exportPage(request: ExportPageDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`pages/export`, request);
  }

  async exportSpace(request: ExportSpaceDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`spaces/export`, request);
  }

}
