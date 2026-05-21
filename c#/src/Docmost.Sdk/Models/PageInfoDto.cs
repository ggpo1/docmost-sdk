namespace Docmost.Sdk.Models;

public class PageInfoDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeSpace")]
    public bool? IncludeSpace { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeContent")]
    public bool? IncludeContent { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("format")]
    public string Format { get; set; }

}
