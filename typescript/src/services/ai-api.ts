/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { SearchDto } from '../models/index.js';


export class AIApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async aiAnswers(request: SearchDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`ai/answers`, request);
  }

}
