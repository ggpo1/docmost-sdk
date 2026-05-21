namespace Docmost.Sdk.Models;

public class User
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("email")]
    public string? Email { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("emailVerifiedAt")]
    public string? EmailVerifiedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("avatarUrl")]
    public string? AvatarUrl { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string? Role { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("locale")]
    public string? Locale { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("timezone")]
    public string? Timezone { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("settings")]
    public string? Settings { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasGeneratedPassword")]
    public string? HasGeneratedPassword { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("lastLoginAt")]
    public string? LastLoginAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("deactivatedAt")]
    public string? DeactivatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
