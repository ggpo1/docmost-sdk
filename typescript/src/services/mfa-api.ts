/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { DisableMfaDto, EnableMfaDto, MfaDto, RegenerateBackupCodesDto } from '../models/index.js';


export class MFAApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async mfaSetup(): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/setup`, undefined);
  }

  async mfaEnable(request: EnableMfaDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/enable`, request);
  }

  async mfaDisable(request: DisableMfaDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/disable`, request);
  }

  async mfaStatus(): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/status`, undefined);
  }

  async mfaRegenerateBackupCodes(request: RegenerateBackupCodesDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/generate-backup-codes`, request);
  }

  async mfaVerify(request: MfaDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/verify`, request);
  }

  async mfaValidateAccess(): Promise<ApiResponse<unknown>> {
    return this.http.post(`mfa/validate-access`, undefined);
  }

}
