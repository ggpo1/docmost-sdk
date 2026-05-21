package models

// CreateSpaceDto from OpenAPI.
type CreateSpaceDto struct {
	Name string `json:"name"`
	Slug string `json:"slug"`
	Description *string `json:"description,omitempty"`
}
