/** Generated from OpenAPI schema `SearchSuggestionDto`. */
export interface SearchSuggestionDto {
  query: string;
  includeUsers?: boolean | null | undefined;
  includeGroups?: boolean | null | undefined;
  includePages?: boolean | null | undefined;
  spaceId?: string | null | undefined;
  limit?: number | null | undefined;
}
