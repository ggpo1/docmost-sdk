namespace Docmost.Sdk.Models;

public class DeletePageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("permanentlyDelete")]
    public bool? PermanentlyDelete { get; set; }

}
