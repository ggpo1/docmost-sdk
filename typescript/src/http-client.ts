/** HTTP transport with Bearer and cookie session auth. */
import axios, { type AxiosInstance, type AxiosResponse, isAxiosError } from 'axios';
import { wrapper } from 'axios-cookiejar-support';
import { CookieJar } from 'tough-cookie';

import { DocmostApiError } from './errors.js';
import type { ApiResponse, ErrorResponse } from './types.js';
import type { LoginDto } from './models/login-dto.js';

export class DocmostHttpClient {
  private readonly apiToken?: string;
  private readonly email?: string;
  private readonly password?: string;
  private loggedIn = false;
  private readonly axios: AxiosInstance;

  constructor(
    baseUrl: string,
    options: {
      apiToken?: string;
      email?: string;
      password?: string;
      timeoutMs?: number;
    } = {},
  ) {
    if (options.apiToken && (options.email || options.password)) {
      throw new Error('Use either apiToken or email/password, not both.');
    }

    this.apiToken = options.apiToken;
    this.email = options.email;
    this.password = options.password;

    const jar = new CookieJar();
    const apiBase = baseUrl.replace(/\/$/, '') + '/api/';

    this.axios = wrapper(
      axios.create({
        baseURL: apiBase,
        timeout: options.timeoutMs ?? 100_000,
        jar,
        withCredentials: true,
        headers: { Accept: 'application/json' },
      } as Parameters<typeof axios.create>[0]),
    );
  }

  async ensureAuthenticated(): Promise<void> {
    if (this.apiToken) return;
    if (!this.email || !this.password) {
      throw new Error('Provide apiToken or email and password.');
    }
    if (this.loggedIn) return;
    await this.login();
    this.loggedIn = true;
  }

  async login(): Promise<void> {
    if (this.apiToken) return;
    const payload: LoginDto = { email: this.email!, password: this.password! };
    const response = await this.request(() =>
      this.axios.post<ApiResponse<unknown>>('auth/login', payload, {
        headers: { 'Content-Type': 'application/json' },
      }),
    );
    this.parseEnvelope(response);
    this.loggedIn = true;
  }

  async logout(): Promise<ApiResponse<unknown>> {
    const result = await this.post('auth/logout', undefined);
    this.loggedIn = false;
    return result;
  }

  async post<T = unknown>(path: string, body?: unknown): Promise<ApiResponse<T>> {
    await this.ensureAuthenticated();
    const response = await this.request(() =>
      this.axios.post<ApiResponse<T>>(path.replace(/^\//, ''), body, {
        headers: { ...this.authHeaders(), 'Content-Type': 'application/json' },
      }),
    );
    return this.parseEnvelope(response);
  }

  async get<T = unknown>(
    path: string,
    params?: Record<string, string>,
  ): Promise<ApiResponse<T>> {
    await this.ensureAuthenticated();
    const response = await this.request(() =>
      this.axios.get<ApiResponse<T>>(path.replace(/^\//, ''), {
        params,
        headers: this.authHeaders(),
      }),
    );
    return this.parseEnvelope(response);
  }

  async getRaw(path: string, params?: Record<string, string>): Promise<Response> {
    await this.ensureAuthenticated();
    const base = this.axios.defaults.baseURL ?? '';
    const url = new URL(path.replace(/^\//, ''), base);
    if (params) {
      for (const [k, v] of Object.entries(params)) {
        url.searchParams.set(k, v);
      }
    }
    const headers: Record<string, string> = { ...this.authHeaders() };
    const res = await fetch(url.toString(), { method: 'GET', headers });
    if (!res.ok) {
      await this.throwFromFetch(res);
    }
    return res;
  }

  async postMultipart<T = unknown>(
    path: string,
    request: Record<string, unknown>,
  ): Promise<ApiResponse<T>> {
    await this.ensureAuthenticated();
    const form = new FormData();
    for (const [key, value] of Object.entries(request)) {
      if (value === undefined || value === null) continue;
      if (
        typeof Blob !== 'undefined' &&
        (value instanceof Blob || (typeof Buffer !== 'undefined' && Buffer.isBuffer(value)))
      ) {
        const blob =
          value instanceof Blob ? value : new Blob([new Uint8Array(value as Buffer)]);
        form.append(key, blob, 'upload.bin');
      } else {
        form.append(key, String(value));
      }
    }
    const response = await this.request(() =>
      this.axios.post<ApiResponse<T>>(path.replace(/^\//, ''), form, {
        headers: { ...this.authHeaders(), 'Content-Type': 'multipart/form-data' },
      }),
    );
    return this.parseEnvelope(response);
  }

  private authHeaders(): Record<string, string> {
    if (this.apiToken) {
      return { Authorization: `Bearer ${this.apiToken}` };
    }
    return {};
  }

  private async request<T>(fn: () => Promise<AxiosResponse<T>>): Promise<AxiosResponse<T>> {
    try {
      return await fn();
    } catch (err) {
      if (isAxiosError(err) && err.response) {
        const data = err.response.data as ErrorResponse | undefined;
        const message =
          data?.error ??
          (typeof data?.message === 'string' ? data.message : undefined) ??
          err.message;
        throw new DocmostApiError(message, err.response.status, data);
      }
      throw err;
    }
  }

  private parseEnvelope<T>(response: AxiosResponse<ApiResponse<T>>): ApiResponse<T> {
    const envelope = response.data;
    if (!envelope) {
      throw new DocmostApiError('Empty response body.', response.status);
    }
    if (!envelope.success) {
      throw new DocmostApiError(
        `API returned success=false (status ${envelope.status}).`,
        envelope.status,
      );
    }
    return envelope;
  }

  private async throwFromFetch(res: Response): Promise<never> {
    let errorBody: ErrorResponse | undefined;
    try {
      errorBody = (await res.json()) as ErrorResponse;
    } catch {
      /* ignore */
    }
    const message =
      errorBody?.error ??
      (typeof errorBody?.message === 'string' ? errorBody.message : undefined) ??
      res.statusText ??
      'Request failed.';
    throw new DocmostApiError(message, res.status, errorBody);
  }
}
