using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class SharesApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetSharesAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetSharedPageInfoAsync(ShareInfoDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/page-info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetShareAsync(ShareIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetShareForPageAsync(SharePageIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/for-page", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CreateShareAsync(CreateShareDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateShareAsync(UpdateShareDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeleteShareAsync(ShareIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/delete", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetSharePageTreeAsync(ShareIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("shares/tree", request, cancellationToken).ConfigureAwait(false);
    }

}
