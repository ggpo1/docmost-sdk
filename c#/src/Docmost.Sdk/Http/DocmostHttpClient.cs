using System.Net;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;
using Docmost.Sdk.Exceptions;
using Docmost.Sdk.Models;

namespace Docmost.Sdk.Http;

public sealed class DocmostHttpClient : IDisposable
{
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        PropertyNameCaseInsensitive = true,
        DefaultIgnoreCondition = System.Text.Json.Serialization.JsonIgnoreCondition.WhenWritingNull,
    };

    private readonly HttpClient _http;
    private readonly string? _apiToken;
    private readonly string? _email;
    private readonly string? _password;
    private readonly SemaphoreSlim _loginLock = new(1, 1);
    private bool _loggedIn;

    public DocmostHttpClient(DocmostClientOptions options)
    {
        var baseUri = options.BaseUrl.ToString().TrimEnd('/') + "/api";
        var handler = options.HttpMessageHandler ?? new HttpClientHandler
        {
            CookieContainer = new CookieContainer(),
            UseCookies = true,
        };

        _http = new HttpClient(handler, disposeHandler: options.HttpMessageHandler is null)
        {
            BaseAddress = new Uri(baseUri + "/"),
            Timeout = options.Timeout,
        };

        _apiToken = options.ApiToken;
        _email = options.Email;
        _password = options.Password;
    }

    public async Task EnsureAuthenticatedAsync(CancellationToken cancellationToken = default)
    {
        if (!string.IsNullOrEmpty(_apiToken))
            return;

        if (string.IsNullOrEmpty(_email) || string.IsNullOrEmpty(_password))
            throw new InvalidOperationException("Provide ApiToken or Email and Password.");

        if (_loggedIn)
            return;

        await _loginLock.WaitAsync(cancellationToken).ConfigureAwait(false);
        try
        {
            if (_loggedIn)
                return;
            await LoginAsync(cancellationToken).ConfigureAwait(false);
            _loggedIn = true;
        }
        finally
        {
            _loginLock.Release();
        }
    }

    public async Task<ApiResponse<T>> PostAsync<T>(
        string path,
        object? body,
        CancellationToken cancellationToken = default)
    {
        await EnsureAuthenticatedAsync(cancellationToken).ConfigureAwait(false);
        using var request = new HttpRequestMessage(HttpMethod.Post, path.TrimStart('/'));
        ApplyAuth(request);
        if (body is not null)
            request.Content = JsonContent.Create(body, options: JsonOptions);

        return await SendAsync<T>(request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<T>> GetAsync<T>(
        string path,
        CancellationToken cancellationToken = default)
    {
        await EnsureAuthenticatedAsync(cancellationToken).ConfigureAwait(false);
        using var request = new HttpRequestMessage(HttpMethod.Get, path.TrimStart('/'));
        ApplyAuth(request);
        return await SendAsync<T>(request, cancellationToken).ConfigureAwait(false);
    }

    public async Task<HttpResponseMessage> GetRawAsync(
        string path,
        CancellationToken cancellationToken = default)
    {
        await EnsureAuthenticatedAsync(cancellationToken).ConfigureAwait(false);
        using var request = new HttpRequestMessage(HttpMethod.Get, path.TrimStart('/'));
        ApplyAuth(request);
        var response = await _http.SendAsync(
            request,
            HttpCompletionOption.ResponseHeadersRead,
            cancellationToken).ConfigureAwait(false);
        if (!response.IsSuccessStatusCode)
            await ThrowForResponseAsync(response, cancellationToken).ConfigureAwait(false);
        return response;
    }

    public async Task<ApiResponse<T>> PostMultipartAsync<T>(
        string path,
        HttpContent content,
        CancellationToken cancellationToken = default)
    {
        await EnsureAuthenticatedAsync(cancellationToken).ConfigureAwait(false);
        using var request = new HttpRequestMessage(HttpMethod.Post, path.TrimStart('/')) { Content = content };
        ApplyAuth(request);
        return await SendAsync<T>(request, cancellationToken).ConfigureAwait(false);
    }

    public async Task LogoutAsync(CancellationToken cancellationToken = default)
    {
        await PostAsync<JsonElement?>("auth/logout", null, cancellationToken).ConfigureAwait(false);
        _loggedIn = false;
    }

    private async Task LoginAsync(CancellationToken cancellationToken)
    {
        using var request = new HttpRequestMessage(HttpMethod.Post, "auth/login")
        {
            Content = JsonContent.Create(
                new LoginDto { Email = _email!, Password = _password! },
                options: JsonOptions),
        };

        var response = await SendAsync<JsonElement?>(request, cancellationToken).ConfigureAwait(false);
        if (!response.Success)
            throw new DocmostApiException("Login failed.", response.Status);
    }

    private void ApplyAuth(HttpRequestMessage request)
    {
        if (!string.IsNullOrEmpty(_apiToken))
            request.Headers.Authorization = new AuthenticationHeaderValue("Bearer", _apiToken);
    }

    private async Task<ApiResponse<T>> SendAsync<T>(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
    {
        var response = await _http.SendAsync(request, cancellationToken).ConfigureAwait(false);
        if (!response.IsSuccessStatusCode)
            await ThrowForResponseAsync(response, cancellationToken).ConfigureAwait(false);

        var envelope = await response.Content
            .ReadFromJsonAsync<ApiResponse<T>>(JsonOptions, cancellationToken)
            .ConfigureAwait(false);

        if (envelope is null)
            throw new DocmostApiException("Empty response body.", (int)response.StatusCode);

        if (!envelope.Success)
            throw new DocmostApiException(
                $"API returned success=false (status {envelope.Status}).",
                envelope.Status);

        return envelope;
    }

    private static async Task ThrowForResponseAsync(
        HttpResponseMessage response,
        CancellationToken cancellationToken)
    {
        ErrorResponse? error = null;
        try
        {
            error = await response.Content
                .ReadFromJsonAsync<ErrorResponse>(JsonOptions, cancellationToken)
                .ConfigureAwait(false);
        }
        catch
        {
            // ignore parse errors
        }

        var message = error?.Error
            ?? error?.Message?.ToString()
            ?? response.ReasonPhrase
            ?? "Request failed.";

        throw new DocmostApiException(message, (int)response.StatusCode, error);
    }

    public void Dispose() => _http.Dispose();
}
