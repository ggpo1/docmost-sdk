namespace Docmost.Sdk.Models;

public class SearchDto
{
    [System.Text.Json.Serialization.JsonPropertyName("query")]
    public string Query { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("creatorId")]
    public string? CreatorId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("limit")]
    public int? Limit { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("offset")]
    public int? Offset { get; set; }

}
