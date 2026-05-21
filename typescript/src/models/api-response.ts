/** API envelope types. */
export interface ApiResponse<T = unknown> {
  data?: T | null;
  success: boolean;
  status: number;
}

export interface ErrorResponse {
  statusCode?: number;
  message?: string | string[];
  error?: string;
}
