namespace Docmost.Sdk.Models;

public class DuplicatePageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

}
