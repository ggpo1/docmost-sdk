using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class SSOApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetSsoProvidersAsync(PaginationOptions request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("sso/providers", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> GetSsoProviderAsync(SsoProviderIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("sso/info", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> CreateSsoProviderAsync(CreateSsoProviderDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("sso/create", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateSsoProviderAsync(UpdateSsoProviderDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("sso/update", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> DeleteSsoProviderAsync(SsoProviderIdDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("sso/delete", request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> LdapLoginAsync(LdapLoginDto request, string providerId, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("sso/ldap/" + Uri.EscapeDataString(providerId) + "/login", request, cancellationToken).ConfigureAwait(false);
    }

}
