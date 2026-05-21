namespace Docmost.Sdk.Models;

public class CreateCommentDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public string Content { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("selection")]
    public string? Selection { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentCommentId")]
    public string? ParentCommentId { get; set; }

}
