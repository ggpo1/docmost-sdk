/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { ResolveCommentDto } from '../models/index.js';


export class CommentResolutionApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async resolveComment(request: ResolveCommentDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`comments/resolve`, request);
  }

}
