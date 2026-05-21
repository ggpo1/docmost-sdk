/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';


export class VersionApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getVersion(): Promise<ApiResponse<unknown>> {
    return this.http.post(`version`, undefined);
  }

}
