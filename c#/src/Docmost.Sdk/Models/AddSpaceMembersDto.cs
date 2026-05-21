namespace Docmost.Sdk.Models;

public class AddSpaceMembersDto
{
    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string Role { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("userIds")]
    public List<string>? UserIds { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groupIds")]
    public List<string>? GroupIds { get; set; }

}
