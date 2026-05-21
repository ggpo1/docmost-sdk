using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class SearchApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> PageSearchAsync(SearchDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("search", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> SearchSuggestionsAsync(SearchSuggestionDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("search/suggest", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> SearchShareAsync(SearchShareDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("search/share-search", request, cancellationToken).ConfigureAwait(false);
    }

}
