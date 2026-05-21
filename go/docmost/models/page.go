package models

// Page from OpenAPI.
type Page struct {
	Id *string `json:"id,omitempty"`
	SlugId *string `json:"slugId,omitempty"`
	Title *string `json:"title,omitempty"`
	Icon *string `json:"icon,omitempty"`
	CoverPhoto *string `json:"coverPhoto,omitempty"`
	Content map[string]any `json:"content,omitempty"`
	Position *string `json:"position,omitempty"`
	ParentPageId *string `json:"parentPageId,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	LastUpdatedById *string `json:"lastUpdatedById,omitempty"`
	IsLocked *bool `json:"isLocked,omitempty"`
	ContributorIds *string `json:"contributorIds,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
	DeletedAt *string `json:"deletedAt,omitempty"`
}
