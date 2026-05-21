using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class PagesApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetPageAsync(PageInfoDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CreatePageAsync(CreatePageDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdatePageAsync(UpdatePageDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeletePageAsync(DeletePageDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/delete", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RestorePageAsync(PageIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/restore", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetRecentPagesAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/recent", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetDeletedPagesAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/trash", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetPageHistoryAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/history", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetPageHistoryInfoAsync(PageHistoryIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/history/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetSidebarPagesAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/sidebar-pages", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MovePageToSpaceAsync(MovePageToSpaceDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/move-to-space", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DuplicatePageAsync(DuplicatePageDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/duplicate", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MovePageAsync(MovePageDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/move", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetPageBreadcrumbsAsync(PageIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("pages/breadcrumbs", request, cancellationToken).ConfigureAwait(false);
    }

}
