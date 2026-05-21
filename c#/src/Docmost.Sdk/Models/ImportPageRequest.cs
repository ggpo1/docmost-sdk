namespace Docmost.Sdk.Models;

public class ImportPageRequest
{
    [System.Text.Json.Serialization.JsonPropertyName("file")]
    public System.IO.Stream File { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string SpaceId { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("parentPageId")]
    public string? ParentPageId { get; set; } = default!;

}
