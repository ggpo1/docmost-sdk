namespace Docmost.Sdk.Models;

public class UpdateWorkspaceDto
{
    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hostname")]
    public string? Hostname { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("description")]
    public string? Description { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("logo")]
    public string? Logo { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("emailDomains")]
    public List<string>? EmailDomains { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("enforceSso")]
    public bool? EnforceSso { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("enforceMfa")]
    public bool? EnforceMfa { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("restrictApiToAdmins")]
    public bool? RestrictApiToAdmins { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("aiSearch")]
    public bool? AiSearch { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("generativeAi")]
    public bool? GenerativeAi { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("disablePublicSharing")]
    public bool? DisablePublicSharing { get; set; }

}
