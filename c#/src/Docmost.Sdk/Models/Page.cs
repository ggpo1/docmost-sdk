namespace Docmost.Sdk.Models;

public class Page
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slugId")]
    public string? SlugId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("title")]
    public string? Title { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("icon")]
    public string? Icon { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("coverPhoto")]
    public string? CoverPhoto { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public System.Text.Json.JsonElement? Content { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("position")]
    public string? Position { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentPageId")]
    public string? ParentPageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("creatorId")]
    public string? CreatorId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("lastUpdatedById")]
    public string? LastUpdatedById { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("isLocked")]
    public bool? IsLocked { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("contributorIds")]
    public string? ContributorIds { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("deletedAt")]
    public string? DeletedAt { get; set; }

}
