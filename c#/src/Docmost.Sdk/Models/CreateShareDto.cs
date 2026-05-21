namespace Docmost.Sdk.Models;

public class CreateShareDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeSubPages")]
    public bool? IncludeSubPages { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("searchIndexing")]
    public bool? SearchIndexing { get; set; }

}
