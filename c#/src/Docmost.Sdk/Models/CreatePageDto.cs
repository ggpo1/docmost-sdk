namespace Docmost.Sdk.Models;

public class CreatePageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("title")]
    public string? Title { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("icon")]
    public string? Icon { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentPageId")]
    public string? ParentPageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public string? Content { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("format")]
    public string Format { get; set; }

}
