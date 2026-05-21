namespace Docmost.Sdk.Models;

public class SidebarPageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string? PageId { get; set; }

}
