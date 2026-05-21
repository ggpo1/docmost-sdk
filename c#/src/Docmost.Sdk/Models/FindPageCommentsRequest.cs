namespace Docmost.Sdk.Models;

public class FindPageCommentsRequest
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("limit")]
    public int? Limit { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("cursor")]
    public string? Cursor { get; set; } = default!;

}
