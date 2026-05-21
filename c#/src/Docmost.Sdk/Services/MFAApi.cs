using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class MFAApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> MfaSetupAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/setup", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MfaEnableAsync(EnableMfaDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/enable", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MfaDisableAsync(DisableMfaDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/disable", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MfaStatusAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/status", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MfaRegenerateBackupCodesAsync(RegenerateBackupCodesDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/generate-backup-codes", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MfaVerifyAsync(MfaDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/verify", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> MfaValidateAccessAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("mfa/validate-access", null, cancellationToken).ConfigureAwait(false);
    }

}
