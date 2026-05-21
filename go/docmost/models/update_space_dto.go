package models

// UpdateSpaceDto from OpenAPI.
type UpdateSpaceDto struct {
	SpaceId string `json:"spaceId"`
	Name *string `json:"name,omitempty"`
	Slug *string `json:"slug,omitempty"`
	Description *string `json:"description,omitempty"`
	DisablePublicSharing *bool `json:"disablePublicSharing,omitempty"`
}
