namespace Docmost.Sdk.Models;

public class CreateApiKeyDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("expiresAt")]
    public string? ExpiresAt { get; set; }

}
