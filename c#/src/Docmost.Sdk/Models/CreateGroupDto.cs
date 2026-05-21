namespace Docmost.Sdk.Models;

public class CreateGroupDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("description")]
    public string? Description { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("userIds")]
    public List<string>? UserIds { get; set; }

}
