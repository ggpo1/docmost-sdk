namespace Docmost.Sdk.Models;

public class SpaceSummary
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slug")]
    public string? Slug { get; set; }

}
