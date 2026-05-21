export type { ApiResponse, ErrorResponse } from './models/api-response.js';

export interface DocmostClientOptions {
  /** Base URL of your Docmost instance (e.g. https://docs.example.com). Client appends `/api`. */
  baseUrl: string;
  /** API key as `Authorization: Bearer <token>`. */
  apiToken?: string;
  /** Email for cookie-based login. */
  email?: string;
  /** Password for cookie-based login. */
  password?: string;
  /** Log in on construction when using email/password. Default: true */
  loginOnStartup?: boolean;
  /** Request timeout in milliseconds. Default: 100000 */
  timeoutMs?: number;
}
