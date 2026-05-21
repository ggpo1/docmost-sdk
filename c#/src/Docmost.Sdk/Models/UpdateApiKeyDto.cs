namespace Docmost.Sdk.Models;

public class UpdateApiKeyDto
{
    [System.Text.Json.Serialization.JsonPropertyName("apiKeyId")]
    public string ApiKeyId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

}
