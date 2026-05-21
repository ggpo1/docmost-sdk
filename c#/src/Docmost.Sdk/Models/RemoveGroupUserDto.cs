namespace Docmost.Sdk.Models;

public class RemoveGroupUserDto
{
    [System.Text.Json.Serialization.JsonPropertyName("groupId")]
    public string GroupId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("userId")]
    public string UserId { get; set; }

}
