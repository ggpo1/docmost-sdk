package models

// Share from OpenAPI.
type Share struct {
	Id *string `json:"id,omitempty"`
	Key *string `json:"key,omitempty"`
	PageId *string `json:"pageId,omitempty"`
	IncludeSubPages *string `json:"includeSubPages,omitempty"`
	SearchIndexing *string `json:"searchIndexing,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
