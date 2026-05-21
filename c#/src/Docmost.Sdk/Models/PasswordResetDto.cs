namespace Docmost.Sdk.Models;

public class PasswordResetDto
{
    [System.Text.Json.Serialization.JsonPropertyName("token")]
    public string Token { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("newPassword")]
    public string NewPassword { get; set; }

}
