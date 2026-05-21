using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class CloudApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> CreateCloudWorkspaceAsync(CreateCloudWorkspaceDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetJoinedWorkspacesAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/joined", null, cancellationToken).ConfigureAwait(false);
    }

}
