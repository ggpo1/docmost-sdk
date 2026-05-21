using Docmost.Sdk.Models;

namespace Docmost.Sdk.Exceptions;

/// <summary>
/// Thrown when the Docmost API returns a non-success HTTP status or <c>success: false</c>.
/// </summary>
public sealed class DocmostApiException : Exception
{
    public DocmostApiException(
        string message,
        int statusCode,
        ErrorResponse? error = null,
        Exception? inner = null)
        : base(message, inner)
    {
        StatusCode = statusCode;
        Error = error;
    }

    public int StatusCode { get; }

    public ErrorResponse? Error { get; }
}
