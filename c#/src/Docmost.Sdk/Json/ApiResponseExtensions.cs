using System.Text.Json;
using Docmost.Sdk.Models;

namespace Docmost.Sdk.Json;

/// <summary>
/// Helpers for mapping <see cref="ApiResponse{T}.Data"/> to typed models.
/// </summary>
public static class ApiResponseExtensions
{
    private static readonly JsonSerializerOptions Options = new()
    {
        PropertyNameCaseInsensitive = true,
    };

    public static T? DeserializeData<T>(this ApiResponse<JsonElement?> response)
    {
        if (response.Data is null or { ValueKind: JsonValueKind.Null or JsonValueKind.Undefined })
            return default;
        return response.Data.Value.Deserialize<T>(Options);
    }

    public static T? DeserializeData<T>(this ApiResponse<JsonElement?> response, JsonSerializerOptions options) =>
        response.Data is null or { ValueKind: JsonValueKind.Null or JsonValueKind.Undefined }
            ? default
            : response.Data.Value.Deserialize<T>(options);
}
