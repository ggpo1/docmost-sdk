/** Generated API client. */
import type { ApiResponse } from '../types.js';
import type { DocmostHttpClient } from '../http-client.js';
import type { SearchDto, SearchShareDto, SearchSuggestionDto } from '../models/index.js';


export class SearchApi {
  constructor(private readonly http: DocmostHttpClient) {}

  async pageSearch(request: SearchDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`search`, request);
  }

  async searchSuggestions(request: SearchSuggestionDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`search/suggest`, request);
  }

  async searchShare(request: SearchShareDto): Promise<ApiResponse<unknown>> {
    return this.http.post(`search/share-search`, request);
  }

}
