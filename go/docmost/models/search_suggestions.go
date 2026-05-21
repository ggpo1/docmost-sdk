package models

// SearchSuggestions from OpenAPI.
type SearchSuggestions struct {
	Users []map[string]any `json:"users,omitempty"`
	Groups []map[string]any `json:"groups,omitempty"`
	Pages []map[string]any `json:"pages,omitempty"`
}
