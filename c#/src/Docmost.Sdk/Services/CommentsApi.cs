using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class CommentsApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> CreateCommentAsync(CreateCommentDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("comments/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> FindPageCommentsAsync(FindPageCommentsRequest request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("comments", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetCommentAsync(CommentIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("comments/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateCommentAsync(UpdateCommentDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("comments/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeleteCommentAsync(CommentIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("comments/delete", request, cancellationToken).ConfigureAwait(false);
    }

}
