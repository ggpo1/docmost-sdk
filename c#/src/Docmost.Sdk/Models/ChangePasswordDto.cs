namespace Docmost.Sdk.Models;

public class ChangePasswordDto
{
    [System.Text.Json.Serialization.JsonPropertyName("oldPassword")]
    public string OldPassword { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("newPassword")]
    public string NewPassword { get; set; }

}
