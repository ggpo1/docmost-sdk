/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { ImportPageRequest, ImportZipRequest } from '../models/index.js';


export class ImportApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async importPage(request: ImportPageRequest): Promise<ApiResponse<unknown>> {
    return this.http.postMultipart(`pages/import`, request as unknown as Record<string, unknown>);
  }

  async importZip(request: ImportZipRequest): Promise<ApiResponse<unknown>> {
    return this.http.postMultipart(`pages/import-zip`, request as unknown as Record<string, unknown>);
  }

}
