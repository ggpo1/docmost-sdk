using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class ExportApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> ExportPageAsync(ExportPageDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/export", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> ExportSpaceAsync(ExportSpaceDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/export", request, cancellationToken).ConfigureAwait(false);
    }

}
