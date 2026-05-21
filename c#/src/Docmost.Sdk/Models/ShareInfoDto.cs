namespace Docmost.Sdk.Models;

public class ShareInfoDto
{
    [System.Text.Json.Serialization.JsonPropertyName("shareId")]
    public string? ShareId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string? PageId { get; set; }

}
