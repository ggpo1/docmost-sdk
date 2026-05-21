namespace Docmost.Sdk.Models;

public class DisableMfaDto
{
    [System.Text.Json.Serialization.JsonPropertyName("confirmPassword")]
    public string? ConfirmPassword { get; set; }

}
