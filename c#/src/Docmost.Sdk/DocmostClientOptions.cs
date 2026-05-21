namespace Docmost.Sdk;

/// <summary>
/// Configuration for <see cref="DocmostClient"/>.
/// </summary>
public sealed class DocmostClientOptions
{
    /// <summary>
    /// Base URL of the Docmost instance (e.g. https://docs.example.com).
    /// The client appends <c>/api</c> automatically.
    /// </summary>
    public required Uri BaseUrl { get; init; }

    /// <summary>
    /// API key passed as <c>Authorization: Bearer &lt;token&gt;</c>.
    /// Mutually exclusive with <see cref="Email"/> / <see cref="Password"/>.
    /// </summary>
    public string? ApiToken { get; init; }

    /// <summary>
    /// Account email for cookie-based login.
    /// </summary>
    public string? Email { get; init; }

    /// <summary>
    /// Account password for cookie-based login.
    /// </summary>
    public string? Password { get; init; }

    /// <summary>
    /// When using email/password, log in immediately on client construction.
    /// Default: <c>true</c>.
    /// </summary>
    public bool LoginOnStartup { get; init; } = true;

    /// <summary>
    /// Optional custom <see cref="HttpMessageHandler"/> (e.g. for proxies or tests).
    /// </summary>
    public HttpMessageHandler? HttpMessageHandler { get; init; }

    /// <summary>
    /// Per-request timeout. Default: 100 seconds.
    /// </summary>
    public TimeSpan Timeout { get; init; } = TimeSpan.FromSeconds(100);
}
