namespace Docmost.Sdk.Models;

public class UploadFileRequest
{
    [System.Text.Json.Serialization.JsonPropertyName("file")]
    public System.IO.Stream File { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("pageId")]
    public string PageId { get; set; } = default!;

    [System.Text.Json.Serialization.JsonPropertyName("attachmentId")]
    public string? AttachmentId { get; set; } = default!;

}
