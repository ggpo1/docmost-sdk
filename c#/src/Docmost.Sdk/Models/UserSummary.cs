namespace Docmost.Sdk.Models;

public class UserSummary
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("avatarUrl")]
    public string? AvatarUrl { get; set; }

}
