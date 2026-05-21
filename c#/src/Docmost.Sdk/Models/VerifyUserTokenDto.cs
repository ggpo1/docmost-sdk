namespace Docmost.Sdk.Models;

public class VerifyUserTokenDto
{
    [System.Text.Json.Serialization.JsonPropertyName("token")]
    public string Token { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("type")]
    public string Type { get; set; }

}
