using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class AttachmentsApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> UploadFileAsync(UploadFileRequest request, CancellationToken cancellationToken = default)
    {
        using var form = new MultipartFormDataContent();
        var fileContent = new StreamContent(request.File);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
        form.Add(fileContent, "file", "upload.bin");
        form.Add(new StringContent(request.PageId?.ToString() ?? string.Empty), "pageId");
        form.Add(new StringContent(request.AttachmentId?.ToString() ?? string.Empty), "attachmentId");
        return await _http.PostMultipartAsync<JsonElement?>("files/upload", form, cancellationToken).ConfigureAwait(false);
    }

    public async Task<HttpResponseMessage> GetFileAsync(string fileId, string fileName, CancellationToken cancellationToken = default)
    {
        return await _http.GetRawAsync("files/" + Uri.EscapeDataString(fileId) + "/" + Uri.EscapeDataString(fileName) + "", cancellationToken).ConfigureAwait(false);
    }

    public async Task<HttpResponseMessage> GetPublicFileAsync(string fileId, string fileName, string? jwt = null, CancellationToken cancellationToken = default)
    {
        var rel = "files/public/" + Uri.EscapeDataString(fileId) + "/" + Uri.EscapeDataString(fileName) + "";
        var query = new List<string>();
        if (jwt is not null) query.Add("jwt=" + Uri.EscapeDataString(jwt));
        var finalPath = query.Count > 0 ? rel + "?" + string.Join("&", query) : rel;
        return await _http.GetRawAsync(finalPath, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> UploadAvatarOrLogoAsync(UploadAvatarOrLogoRequest request, CancellationToken cancellationToken = default)
    {
        using var form = new MultipartFormDataContent();
        var fileContent = new StreamContent(request.File);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
        form.Add(fileContent, "file", "upload.bin");
        form.Add(new StringContent(request.Type?.ToString() ?? string.Empty), "type");
        form.Add(new StringContent(request.SpaceId?.ToString() ?? string.Empty), "spaceId");
        return await _http.PostMultipartAsync<JsonElement?>("attachments/upload-image", form, cancellationToken).ConfigureAwait(false);
    }

    public async Task<HttpResponseMessage> GetLogoOrAvatarAsync(string attachmentType, string fileName, CancellationToken cancellationToken = default)
    {
        return await _http.GetRawAsync("attachments/img/" + Uri.EscapeDataString(attachmentType) + "/" + Uri.EscapeDataString(fileName) + "", cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> RemoveIconAsync(RemoveIconDto request, CancellationToken cancellationToken = default)
    {
        return await _http.PostAsync<JsonElement?>("attachments/remove-icon", request, cancellationToken).ConfigureAwait(false);
    }

}
