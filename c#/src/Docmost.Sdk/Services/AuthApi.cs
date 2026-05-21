using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class AuthApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> LoginAsync(LoginDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/login", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> SetupWorkspaceAsync(CreateAdminUserDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/setup", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> ChangePasswordAsync(ChangePasswordDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/change-password", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> ForgotPasswordAsync(ForgotPasswordDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/forgot-password", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> PasswordResetAsync(PasswordResetDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/password-reset", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> VerifyResetTokenAsync(VerifyUserTokenDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/verify-token", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CollabTokenAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/collab-token", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> LogoutAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("auth/logout", null, cancellationToken).ConfigureAwait(false);
    }

}
