/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { ChangePasswordDto, CreateAdminUserDto, ForgotPasswordDto, LoginDto, PasswordResetDto, VerifyUserTokenDto } from '../models/index.js';


export class AuthApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async login(request: LoginDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/login`, request);
  }

  async setupWorkspace(request: CreateAdminUserDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/setup`, request);
  }

  async changePassword(request: ChangePasswordDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/change-password`, request);
  }

  async forgotPassword(request: ForgotPasswordDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/forgot-password`, request);
  }

  async passwordReset(request: PasswordResetDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/password-reset`, request);
  }

  async verifyResetToken(request: VerifyUserTokenDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/verify-token`, request);
  }

  async collabToken(): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/collab-token`, undefined);
  }

  async logout(): Promise<ApiResponse<unknown>> {
    return this.http.post(`auth/logout`, undefined);
  }

}
