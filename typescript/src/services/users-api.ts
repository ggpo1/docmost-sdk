/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { UpdateUserDto } from '../models/index.js';


export class UsersApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getUserInfo(): Promise<ApiResponse<unknown>> {
    return this.http.post(`users/me`, undefined);
  }

  async updateUser(request: UpdateUserDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`users/update`, request);
  }

}
