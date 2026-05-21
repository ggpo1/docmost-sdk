namespace Docmost.Sdk.Models;

public class UpdateCommentDto
{
    [System.Text.Json.Serialization.JsonPropertyName("commentId")]
    public string CommentId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public string Content { get; set; }

}
