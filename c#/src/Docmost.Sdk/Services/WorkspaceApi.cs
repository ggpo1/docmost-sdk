using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class WorkspaceApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetWorkspacePublicInfoAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/public", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetWorkspaceInfoAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/info", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateWorkspaceAsync(UpdateWorkspaceDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetWorkspaceMembersAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/members", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeactivateWorkspaceMemberAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/members/deactivate", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeleteWorkspaceMemberAsync(RemoveWorkspaceUserDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/members/delete", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateWorkspaceMemberRoleAsync(UpdateWorkspaceUserRoleDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/members/change-role", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetInvitationsAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetInvitationByIdAsync(InvitationIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> InviteUserAsync(InviteUserDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> ResendInviteAsync(InvitationIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites/resend", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RevokeInviteAsync(InvitationIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites/revoke", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> AcceptInviteAsync(AcceptInviteDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites/accept", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetInviteLinkAsync(InvitationIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/invites/link", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CheckHostnameAsync(CheckHostnameDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("workspace/check-hostname", request, cancellationToken).ConfigureAwait(false);
    }

}
