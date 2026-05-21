package models

// PageHistory from OpenAPI.
type PageHistory struct {
	Id *string `json:"id,omitempty"`
	PageId *string `json:"pageId,omitempty"`
	Title *string `json:"title,omitempty"`
	Icon *string `json:"icon,omitempty"`
	SlugId *string `json:"slugId,omitempty"`
	Slug *string `json:"slug,omitempty"`
	Content map[string]any `json:"content,omitempty"`
	Version *string `json:"version,omitempty"`
	LastUpdatedById *string `json:"lastUpdatedById,omitempty"`
	ContributorIds *string `json:"contributorIds,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
