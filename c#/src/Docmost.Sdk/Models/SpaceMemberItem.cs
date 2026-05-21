namespace Docmost.Sdk.Models;

public class SpaceMemberItem
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string Type { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("email")]
    public string? Email { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("avatarUrl")]
    public string? AvatarUrl { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("memberCount")]
    public int? MemberCount { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("isDefault")]
    public bool? IsDefault { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string? Role { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

}
