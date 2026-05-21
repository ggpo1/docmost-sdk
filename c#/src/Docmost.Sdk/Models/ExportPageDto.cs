namespace Docmost.Sdk.Models;

public class ExportPageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("format")]
    public string Format { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeChildren")]
    public bool? IncludeChildren { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeAttachments")]
    public bool? IncludeAttachments { get; set; }

}
