using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class UsersApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> GetUserInfoAsync(CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("users/me", null, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UpdateUserAsync(UpdateUserDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("users/update", request, cancellationToken).ConfigureAwait(false);
    }

}
