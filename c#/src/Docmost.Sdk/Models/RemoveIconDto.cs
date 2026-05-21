namespace Docmost.Sdk.Models;

public class RemoveIconDto
{
    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string Type { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

}
