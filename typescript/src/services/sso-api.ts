/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { CreateSsoProviderDto, LdapLoginDto, PaginationOptions, SsoProviderIdDto, UpdateSsoProviderDto } from '../models/index.js';


export class SSOApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async getSsoProviders(request: PaginationOptions): Promise<ApiResponse<unknown>> {
    return this.http.post(`sso/providers`, request);
  }

  async getSsoProvider(request: SsoProviderIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`sso/info`, request);
  }

  async createSsoProvider(request: CreateSsoProviderDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`sso/create`, request);
  }

  async updateSsoProvider(request: UpdateSsoProviderDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`sso/update`, request);
  }

  async deleteSsoProvider(request: SsoProviderIdDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`sso/delete`, request);
  }

  async ldapLogin(request: LdapLoginDto, providerId: string): Promise<ApiResponse<unknown>> {
    return this.http.post(`sso/ldap/${encodeURIComponent(providerId)}/login`, request);
  }

}
