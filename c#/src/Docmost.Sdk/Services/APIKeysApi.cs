using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class APIKeysApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetApiKeysAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("api-keys", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CreateApiKeyAsync(CreateApiKeyDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("api-keys/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateApiKeyAsync(UpdateApiKeyDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("api-keys/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RevokeApiKeyAsync(RevokeApiKeyDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("api-keys/revoke", request, cancellationToken).ConfigureAwait(false);
    }

}
