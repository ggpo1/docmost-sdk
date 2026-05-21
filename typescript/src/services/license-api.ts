/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { ActivateLicenseDto } from '../models/index.js';


export class LicenseApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getLicenseInfo(): Promise<ApiResponse<unknown>> {
    return this.http.post(`license/info`, undefined);
  }

  async activateLicense(request: ActivateLicenseDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`license/activate`, request);
  }

  async removeLicense(): Promise<ApiResponse<unknown>> {
    return this.http.post(`license/remove`, undefined);
  }

}
