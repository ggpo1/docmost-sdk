using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class GroupsApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetWorkspaceGroupsAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetGroupInfoAsync(GroupIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CreateGroupAsync(CreateGroupDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateGroupAsync(UpdateGroupDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetGroupMembersAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/members", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> AddGroupMembersAsync(AddGroupUserDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/members/add", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RemoveGroupMemberAsync(RemoveGroupUserDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/members/remove", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeleteGroupAsync(GroupIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("groups/delete", request, cancellationToken).ConfigureAwait(false);
    }

}
