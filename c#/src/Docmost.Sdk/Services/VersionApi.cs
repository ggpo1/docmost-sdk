using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class VersionApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetVersionAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("version", null, cancellationToken).ConfigureAwait(false);
    }

}
