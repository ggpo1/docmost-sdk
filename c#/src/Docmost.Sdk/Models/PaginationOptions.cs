namespace Docmost.Sdk.Models;

public class PaginationOptions
{
    [System.Text.Json.Serialization.JsonPropertyName("limit")]
    public int? Limit { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("cursor")]
    public string? Cursor { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("query")]
    public string? Query { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("adminView")]
    public bool? AdminView { get; set; }

}
