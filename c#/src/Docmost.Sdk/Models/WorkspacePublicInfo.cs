namespace Docmost.Sdk.Models;

public class WorkspacePublicInfo
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("logo")]
    public string? Logo { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hostname")]
    public string? Hostname { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("enforceSso")]
    public bool? EnforceSso { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasLicenseKey")]
    public bool? HasLicenseKey { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("authProviders")]
    public List<Dictionary<string, object?>>? AuthProviders { get; set; }

}
