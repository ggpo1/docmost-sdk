namespace Docmost.Sdk.Models;

public class UpdateSsoProviderDto
{
    [System.Text.Json.Serialization.JsonPropertyName("providerId")]
    public string ProviderId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("name")]
    public string? Name { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("samlUrl")]
    public string? SamlUrl { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("samlCertificate")]
    public string? SamlCertificate { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("oidcIssuer")]
    public string? OidcIssuer { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("oidcClientId")]
    public string? OidcClientId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("oidcClientSecret")]
    public string? OidcClientSecret { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapUrl")]
    public string? LdapUrl { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapBindDn")]
    public string? LdapBindDn { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapBindPassword")]
    public string? LdapBindPassword { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapBaseDn")]
    public string? LdapBaseDn { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapUserSearchFilter")]
    public string? LdapUserSearchFilter { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapUserAttributes")]
    public Dictionary<string, object?>? LdapUserAttributes { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapTlsEnabled")]
    public bool? LdapTlsEnabled { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("ldapTlsCaCert")]
    public string? LdapTlsCaCert { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("allowSignup")]
    public bool? AllowSignup { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("isEnabled")]
    public bool? IsEnabled { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("groupSync")]
    public bool? GroupSync { get; set; }

}
