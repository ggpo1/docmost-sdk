namespace Docmost.Sdk.Models;

public class Share
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("key")]
    public string? Key { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string? PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeSubPages")]
    public string? IncludeSubPages { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("searchIndexing")]
    public string? SearchIndexing { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("creatorId")]
    public string? CreatorId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
