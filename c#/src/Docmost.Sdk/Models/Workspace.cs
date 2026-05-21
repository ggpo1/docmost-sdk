namespace Docmost.Sdk.Models;

public class Workspace
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("description")]
    public string? Description { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("logo")]
    public string? Logo { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hostname")]
    public string? Hostname { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("customDomain")]
    public string? CustomDomain { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("defaultRole")]
    public string? DefaultRole { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("defaultSpaceId")]
    public string? DefaultSpaceId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("emailDomains")]
    public string? EmailDomains { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("enforceSso")]
    public bool? EnforceSso { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("enforceMfa")]
    public string? EnforceMfa { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("settings")]
    public string? Settings { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("plan")]
    public string? Plan { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("status")]
    public string? Status { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("createdAt")]
    public string? CreatedAt { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("updatedAt")]
    public string? UpdatedAt { get; set; }

}
