/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { FileTaskIdDto, PaginationOptions } from '../models/index.js';


export class FileTasksApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getFileTasks(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`file-tasks`, request);
  }

  async getFileTask(request: FileTaskIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`file-tasks/info`, request);
  }

}
