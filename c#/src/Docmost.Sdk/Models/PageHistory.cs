namespace Docmost.Sdk.Models;

public class PageHistory
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string? PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("title")]
    public string? Title { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("icon")]
    public string? Icon { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slugId")]
    public string? SlugId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slug")]
    public string? Slug { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public System.Text.Json.JsonElement? Content { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("version")]
    public string? Version { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("lastUpdatedById")]
    public string? LastUpdatedById { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("contributorIds")]
    public string? ContributorIds { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
