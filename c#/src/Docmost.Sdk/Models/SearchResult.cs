namespace Docmost.Sdk.Models;

public class SearchResult
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("title")]
    public string? Title { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("icon")]
    public string? Icon { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentPageId")]
    public string? ParentPageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("creatorId")]
    public string? CreatorId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("rank")]
    public double? Rank { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("highlight")]
    public string? Highlight { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("space")]
    public SpaceSummary? Space { get; set; }

}
