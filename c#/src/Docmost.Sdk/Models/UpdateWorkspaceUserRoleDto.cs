namespace Docmost.Sdk.Models;

public class UpdateWorkspaceUserRoleDto
{
    [System.Text.Json.Serialization.JsonPropertyName("userId")]
    public string UserId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string Role { get; set; }

}
