namespace Docmost.Sdk.Models;

public class SidebarPage
{
    [System.Text.Json.Serialization.JsonPropertyName("id")]
    public string? Id { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("slugId")]
    public string? SlugId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("title")]
    public string? Title { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("icon")]
    public string? Icon { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("position")]
    public string? Position { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("parentPageId")]
    public string? ParentPageId { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("hasChildren")]
    public bool? HasChildren { get; set; }

    [System.Text.Json.Serialization.JsonPropertyName("spaceId")]
    public string? SpaceId { get; set; }

}
