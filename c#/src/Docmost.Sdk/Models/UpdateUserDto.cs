namespace Docmost.Sdk.Models;

public class UpdateUserDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("email")]
    public string? Email { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("avatarUrl")]
    public string? AvatarUrl { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("fullPageWidth")]
    public bool? FullPageWidth { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("pageEditMode")]
    public string PageEditMode { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("locale")]
    public string? Locale { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("confirmPassword")]
    public string? ConfirmPassword { get; set; }

}
