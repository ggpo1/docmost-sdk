namespace Docmost.Sdk.Models;

public class Attachment
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("fileName")]
    public string? FileName { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("fileExt")]
    public string? FileExt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("filePath")]
    public string? FilePath { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("fileSize")]
    public string? FileSize { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("mimeType")]
    public string? MimeType { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string? Type { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string? PageId { get; set; }

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
