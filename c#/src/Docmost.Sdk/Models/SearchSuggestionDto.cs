namespace Docmost.Sdk.Models;

public class SearchSuggestionDto
{
    [System.Text.Json.Serialization.JsonPropertyName("query")]
    public string Query { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeUsers")]
    public bool? IncludeUsers { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeGroups")]
    public bool? IncludeGroups { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includePages")]
    public bool? IncludePages { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("limit")]
    public int? Limit { get; set; }

}
