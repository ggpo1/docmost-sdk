namespace Docmost.Sdk.Models;

public class CursorPaginationMeta
{
    [System.Text.Json.Serialization.JsonPropertyName("limit")]
    public int? Limit { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasNextPage")]
    public bool? HasNextPage { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasPrevPage")]
    public bool? HasPrevPage { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("nextCursor")]
    public string? NextCursor { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("prevCursor")]
    public string? PrevCursor { get; set; }

}
