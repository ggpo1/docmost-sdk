namespace Docmost.Sdk.Models;

public class RemoveSpaceMemberDto
{
    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("userId")]
    public string? UserId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groupId")]
    public string? GroupId { get; set; }

}
