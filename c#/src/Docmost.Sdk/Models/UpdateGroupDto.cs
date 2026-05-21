namespace Docmost.Sdk.Models;

public class UpdateGroupDto
{
    [System.Text.Json.Serialization.JsonPropertyName("groupId")]
    public string GroupId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("description")]
    public string? Description { get; set; }

}
