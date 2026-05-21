namespace Docmost.Sdk.Models;

public class UploadAvatarOrLogoRequest
{
    [System.Text.Json.Serialization.JsonPropertyName("file")]
    public System.IO.Stream File { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string Type { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; } = default!;

}
