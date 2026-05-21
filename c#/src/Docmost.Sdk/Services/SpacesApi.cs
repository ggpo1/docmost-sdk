using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class SpacesApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetWorkspaceSpacesAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetSpaceInfoAsync(SpaceIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CreateSpaceAsync(CreateSpaceDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateSpaceAsync(UpdateSpaceDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeleteSpaceAsync(SpaceIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/delete", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetSpaceMembersAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/members", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> AddSpaceMembersAsync(AddSpaceMembersDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/members/add", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RemoveSpaceMemberAsync(RemoveSpaceMemberDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/members/remove", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateSpaceMemberRoleAsync(UpdateSpaceMemberRoleDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("spaces/members/change-role", request, cancellationToken).ConfigureAwait(false);
    }

}
