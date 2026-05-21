namespace Docmost.Sdk.Models;

public class UpdatePageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("title")]
    public string? Title { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("icon")]
    public string? Icon { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("content")]
    public string? Content { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("format")]
    public string Format { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("operation")]
    public string Operation { get; set; }

}
