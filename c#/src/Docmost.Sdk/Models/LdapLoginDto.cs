namespace Docmost.Sdk.Models;

public class LdapLoginDto
{
    [System.Text.Json.Serialization.JsonPropertyName("username")]
    public string Username { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("password")]
    public string Password { get; set; }

}
