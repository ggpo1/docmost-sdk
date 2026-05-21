namespace Docmost.Sdk.Models;

public class Comment
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string? PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public System.Text.Json.JsonElement? Content { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("selection")]
    public string? Selection { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string? Type { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentCommentId")]
    public string? ParentCommentId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("creatorId")]
    public string? CreatorId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("lastEditedById")]
    public string? LastEditedById { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("editedAt")]
    public string? EditedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("resolvedAt")]
    public string? ResolvedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("resolvedById")]
    public string? ResolvedById { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
