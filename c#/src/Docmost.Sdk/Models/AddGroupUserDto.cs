namespace Docmost.Sdk.Models;

public class AddGroupUserDto
{
    [System.Text.Json.Serialization.JsonPropertyName("groupId")]
    public string GroupId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("userIds")]
    public List<string> UserIds { get; set; }

}
