/** Helpers for typed API response data. */
import type { ApiResponse } from './types.js';

export function parseData<T>(response: ApiResponse<unknown>, guard: (data: unknown) => data is T): T | null {
  if (response.data === undefined || response.data === null) {
    return null;
  }
  return guard(response.data) ? response.data : (response.data as T);
}

export function parseDataAs<T>(response: ApiResponse<unknown>): T | null {
  if (response.data === undefined || response.data === null) {
    return null;
  }
  return response.data as T;
}
