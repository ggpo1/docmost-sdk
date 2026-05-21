using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class HealthApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> HealthCheckAsync(CancellationToken cancellationToken = default)
    {
        return await _http.GetAsync<JsonElement?>("health", cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> LivenessAsync(CancellationToken cancellationToken = default)
    {
        return await _http.GetAsync<JsonElement?>("health/live", cancellationToken).ConfigureAwait(false);
    }

}
