namespace Docmost.Sdk.Models;

public class OffsetPaginationMeta
{
    [System.Text.Json.Serialization.JsonPropertyName("limit")]
    public int? Limit { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("page")]
    public int? Page { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasNextPage")]
    public bool? HasNextPage { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasPrevPage")]
    public bool? HasPrevPage { get; set; }

}
