namespace Docmost.Sdk.Models;

public class SearchSuggestions
{
    [System.Text.Json.Serialization.JsonPropertyName("users")]
    public List<Dictionary<string, object?>>? Users { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groups")]
    public List<Dictionary<string, object?>>? Groups { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pages")]
    public List<Dictionary<string, object?>>? Pages { get; set; }

}
