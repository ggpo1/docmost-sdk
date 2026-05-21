/** Generated from OpenAPI schema `SearchResult`. */
import type { SpaceSummary } from './space-summary.js';

export interface SearchResult {
  id?: string | null | undefined;
  title?: string | null | undefined;
  icon?: string | null | undefined;
  parentPageId?: string | null | undefined;
  creatorId?: string | null | undefined;
  rank?: number | null | undefined;
  highlight?: string | null | undefined;
  createdAt?: string | null | undefined;
  updatedAt?: string | null | undefined;
  space?: SpaceSummary | null | undefined;
}
