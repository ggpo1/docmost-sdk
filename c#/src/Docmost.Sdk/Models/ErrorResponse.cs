namespace Docmost.Sdk.Models;

public sealed class ErrorResponse
{
    [System.Text.Json.Serialization.JsonPropertyName("statusCode")]
    public int StatusCode { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("message")]
    public System.Text.Json.JsonElement? Message { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("error")]
    public string? Error { get; set; }
}
