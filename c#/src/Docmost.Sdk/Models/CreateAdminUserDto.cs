namespace Docmost.Sdk.Models;

public class CreateAdminUserDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("email")]
    public string Email { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("password")]
    public string Password { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceName")]
    public string? WorkspaceName { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hostname")]
    public string? Hostname { get; set; }

}
