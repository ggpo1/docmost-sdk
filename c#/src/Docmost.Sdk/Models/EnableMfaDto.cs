namespace Docmost.Sdk.Models;

public class EnableMfaDto
{
    [System.Text.Json.Serialization.JsonPropertyName("secret")]
    public string Secret { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("verificationCode")]
    public string VerificationCode { get; set; }

}
