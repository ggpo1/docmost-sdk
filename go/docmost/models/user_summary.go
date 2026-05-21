package models

// UserSummary from OpenAPI.
type UserSummary struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	AvatarUrl *string `json:"avatarUrl,omitempty"`
}
