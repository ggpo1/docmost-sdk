namespace Docmost.Sdk.Models;

public class MovePageDto
{
    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("position")]
    public string Position { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentPageId")]
    public string? ParentPageId { get; set; }

}
