package models

// Group from OpenAPI.
type Group struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Description *string `json:"description,omitempty"`
	IsDefault *bool `json:"isDefault,omitempty"`
	MemberCount *int `json:"memberCount,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
