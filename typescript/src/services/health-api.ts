/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';


export class HealthApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async healthCheck(): Promise<ApiResponse<unknown>> {
    return this.http.get(`health`);
  }

  async liveness(): Promise<ApiResponse<unknown>> {
    return this.http.get(`health/live`);
  }

}
