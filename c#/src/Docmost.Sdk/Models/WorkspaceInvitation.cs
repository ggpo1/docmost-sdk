namespace Docmost.Sdk.Models;

public class WorkspaceInvitation
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("email")]
    public string? Email { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("role")]
    public string? Role { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("token")]
    public string? Token { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groupIds")]
    public string? GroupIds { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("invitedById")]
    public string? InvitedById { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("workspaceId")]
    public string? WorkspaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
