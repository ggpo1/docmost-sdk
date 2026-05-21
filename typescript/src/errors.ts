/** Docmost API errors. */
import type { ErrorResponse } from './types.js';

export class DocmostApiError extends Error {
  readonly statusCode: number;
  readonly errorBody?: ErrorResponse;

  constructor(message: string, statusCode: number, errorBody?: ErrorResponse) {
    super(message);
    this.name = 'DocmostApiError';
    this.statusCode = statusCode;
    this.errorBody = errorBody;
  }
}
