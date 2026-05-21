/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { SearchDto } from '../models/index.js';


export class AttachmentSearchApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async searchAttachments(request: SearchDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`search-attachments`, request);
  }

  async triggerAttachmentIndexing(): Promise<ApiResponse<unknown>> {
    return this.http.post(`search-attachments/indexing`, undefined);
  }

}
