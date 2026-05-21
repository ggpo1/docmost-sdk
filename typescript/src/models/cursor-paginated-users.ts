/** Generated from OpenAPI schema `CursorPaginatedUsers`. */
import type { CursorPaginationMeta } from './cursor-pagination-meta.js';
import type { User } from './user.js';

export interface CursorPaginatedUsers {
  items?: User[] | null | undefined;
  meta?: CursorPaginationMeta | null | undefined;
}
