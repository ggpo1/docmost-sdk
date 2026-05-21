using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class LicenseApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetLicenseInfoAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("license/info", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> ActivateLicenseAsync(ActivateLicenseDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("license/activate", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RemoveLicenseAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("license/remove", null, cancellationToken).ConfigureAwait(false);
    }

}
