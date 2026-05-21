namespace Docmost.Sdk.Models;

public class ExportSpaceDto
{
    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("format")]
    public string Format { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("includeAttachments")]
    public bool? IncludeAttachments { get; set; }

}
