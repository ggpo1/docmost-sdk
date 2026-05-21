namespace Docmost.Sdk.Models;

public class CreateSpaceDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slug")]
    public string Slug { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("description")]
    public string? Description { get; set; }

}
