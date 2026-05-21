package models

// SearchDto from OpenAPI.
type SearchDto struct {
	Query string `json:"query"`
	SpaceId *string `json:"spaceId,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	Limit *int `json:"limit,omitempty"`
	Offset *int `json:"offset,omitempty"`
}
