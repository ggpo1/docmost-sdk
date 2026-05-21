namespace Docmost.Sdk.Models;

public class Space
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slug")]
    public string? Slug { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("description")]
    public string? Description { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("logo")]
    public string? Logo { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("defaultRole")]
    public string? DefaultRole { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("visibility")]
    public string? Visibility { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("settings")]
    public string? Settings { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("creatorId")]
    public string? CreatorId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
