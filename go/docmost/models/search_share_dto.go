package models

// SearchShareDto from OpenAPI.
type SearchShareDto struct {
	Query string `json:"query"`
	ShareId string `json:"shareId"`
	SpaceId *string `json:"spaceId,omitempty"`
	Limit *int `json:"limit,omitempty"`
	Offset *int `json:"offset,omitempty"`
}
