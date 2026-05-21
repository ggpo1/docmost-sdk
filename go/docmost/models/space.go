package models

// Space from OpenAPI.
type Space struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Slug *string `json:"slug,omitempty"`
	Description *string `json:"description,omitempty"`
	Logo *string `json:"logo,omitempty"`
	DefaultRole *string `json:"defaultRole,omitempty"`
	Visibility *string `json:"visibility,omitempty"`
	Settings *string `json:"settings,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
