namespace Docmost.Sdk.Models;

public class CursorPaginatedUsers
{
    [System.Text.Json.Serialization.JsonPropertyName("items")]
    public List<User>? Items { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("meta")]
    public CursorPaginationMeta? Meta { get; set; }

}
