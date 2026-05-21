/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { CommentIdDto, CreateCommentDto, FindPageCommentsRequest, UpdateCommentDto } from '../models/index.js';


export class CommentsApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async createComment(request: CreateCommentDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`comments/create`, request);
  }

  async findPageComments(request: FindPageCommentsRequest): Promise<ApiResponse<unknown>> {
    return this.http.post(`comments`, request);
  }

  async getComment(request: CommentIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`comments/info`, request);
  }

  async updateComment(request: UpdateCommentDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`comments/update`, request);
  }

  async deleteComment(request: CommentIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`comments/delete`, request);
  }

}
