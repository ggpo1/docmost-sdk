namespace Docmost.Sdk.Models;

public sealed class ApiResponse<T>
{
    [System.Text.Json.Serialization.JsonPropertyName("data")]
    public T? Data { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("success")]
    public bool Success { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("status")]
    public int Status { get; set; }
}
