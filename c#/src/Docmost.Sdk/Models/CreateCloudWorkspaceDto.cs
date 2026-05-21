namespace Docmost.Sdk.Models;

public class CreateCloudWorkspaceDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("email")]
    public string Email { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("password")]
    public string Password { get; set; }

}
