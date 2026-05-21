namespace Docmost.Sdk.Models;

public class ResolveCommentDto
{
    [System.Text.Json.Serialization.JsonPropertyName("commentId")]
    public string CommentId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("resolved")]
    public bool Resolved { get; set; }

}
