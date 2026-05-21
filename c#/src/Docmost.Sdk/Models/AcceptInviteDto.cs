namespace Docmost.Sdk.Models;

public class AcceptInviteDto
{
    [System.Text.Json.Serialization.JsonPropertyName("invitationId")]
    public string InvitationId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("password")]
    public string Password { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("token")]
    public string Token { get; set; }

}
