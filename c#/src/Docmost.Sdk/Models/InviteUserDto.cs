namespace Docmost.Sdk.Models;

public class InviteUserDto
{
    [System.Text.Json.Serialization.JsonPropertyName("emails")]
    public List<string> Emails { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groupIds")]
    public List<string>? GroupIds { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string Role { get; set; }

}
