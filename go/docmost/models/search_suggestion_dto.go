package models

// SearchSuggestionDto from OpenAPI.
type SearchSuggestionDto struct {
	Query string `json:"query"`
	IncludeUsers *bool `json:"includeUsers,omitempty"`
	IncludeGroups *bool `json:"includeGroups,omitempty"`
	IncludePages *bool `json:"includePages,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	Limit *int `json:"limit,omitempty"`
}
