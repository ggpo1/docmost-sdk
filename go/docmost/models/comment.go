package models

// Comment from OpenAPI.
type Comment struct {
	Id *string `json:"id,omitempty"`
	PageId *string `json:"pageId,omitempty"`
	Content map[string]any `json:"content,omitempty"`
	Selection *string `json:"selection,omitempty"`
	Type_ *string `json:"type,omitempty"`
	ParentCommentId *string `json:"parentCommentId,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	LastEditedById *string `json:"lastEditedById,omitempty"`
	EditedAt *string `json:"editedAt,omitempty"`
	ResolvedAt *string `json:"resolvedAt,omitempty"`
	ResolvedById *string `json:"resolvedById,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
