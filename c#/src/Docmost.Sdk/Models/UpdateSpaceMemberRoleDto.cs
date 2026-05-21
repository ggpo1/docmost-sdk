namespace Docmost.Sdk.Models;

public class UpdateSpaceMemberRoleDto
{
    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string SpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("userId")]
    public string? UserId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groupId")]
    public string? GroupId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string Role { get; set; }

}
