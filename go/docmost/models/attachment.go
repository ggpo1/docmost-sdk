package models

// Attachment from OpenAPI.
type Attachment struct {
	Id *string `json:"id,omitempty"`
	FileName *string `json:"fileName,omitempty"`
	FileExt *string `json:"fileExt,omitempty"`
	FilePath *string `json:"filePath,omitempty"`
	FileSize *string `json:"fileSize,omitempty"`
	MimeType *string `json:"mimeType,omitempty"`
	Type_ *string `json:"type,omitempty"`
	PageId *string `json:"pageId,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
