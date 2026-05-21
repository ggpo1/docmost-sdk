package models

// CreateGroupDto from OpenAPI.
type CreateGroupDto struct {
	Name string `json:"name"`
	Description *string `json:"description,omitempty"`
	UserIds []string `json:"userIds,omitempty"`
}
