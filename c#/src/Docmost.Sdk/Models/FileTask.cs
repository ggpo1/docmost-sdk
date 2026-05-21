namespace Docmost.Sdk.Models;

public class FileTask
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

    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string? Type { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("source")]
    public string? Source { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("status")]
    public string? Status { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("errorMessage")]
    public string? ErrorMessage { get; set; }

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
