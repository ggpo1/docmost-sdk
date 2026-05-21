using Docmost.Sdk.Http;
using Docmost.Sdk.Models;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace Docmost.Sdk.Services;

public sealed class ImportApi(DocmostHttpClient http)
{
    private readonly DocmostHttpClient _http = http;

    public async Task<ApiResponse<JsonElement?>> ImportPageAsync(ImportPageRequest request, CancellationToken cancellationToken = default)
    {
        using var form = new MultipartFormDataContent();
        var fileContent = new StreamContent(request.File);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
        form.Add(fileContent, "file", "upload.bin");
        form.Add(new StringContent(request.SpaceId?.ToString() ?? string.Empty), "spaceId");
        form.Add(new StringContent(request.ParentPageId?.ToString() ?? string.Empty), "parentPageId");
        return await _http.PostMultipartAsync<JsonElement?>("pages/import", form, cancellationToken).ConfigureAwait(false);
    }

    public async Task<ApiResponse<JsonElement?>> ImportZipAsync(ImportZipRequest request, CancellationToken cancellationToken = default)
    {
        using var form = new MultipartFormDataContent();
        var fileContent = new StreamContent(request.File);
        fileContent.Headers.ContentType = new MediaTypeHeaderValue("application/octet-stream");
        form.Add(fileContent, "file", "upload.bin");
        form.Add(new StringContent(request.SpaceId?.ToString() ?? string.Empty), "spaceId");
        form.Add(new StringContent(request.Source?.ToString() ?? string.Empty), "source");
        form.Add(new StringContent(request.ParentPageId?.ToString() ?? string.Empty), "parentPageId");
        return await _http.PostMultipartAsync<JsonElement?>("pages/import-zip", form, cancellationToken).ConfigureAwait(false);
    }

}
