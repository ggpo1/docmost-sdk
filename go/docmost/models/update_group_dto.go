package models

// UpdateGroupDto from OpenAPI.
type UpdateGroupDto struct {
	GroupId string `json:"groupId"`
	Name *string `json:"name,omitempty"`
	Description *string `json:"description,omitempty"`
}
