using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class AttachmentSearchApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> SearchAttachmentsAsync(SearchDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("search-attachments", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> TriggerAttachmentIndexingAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("search-attachments/indexing", null, cancellationToken).ConfigureAwait(false);
    }

}
