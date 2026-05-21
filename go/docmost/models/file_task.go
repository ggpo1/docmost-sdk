package models

// FileTask from OpenAPI.
type FileTask struct {
	Id *string `json:"id,omitempty"`
	FileName *string `json:"fileName,omitempty"`
	FileExt *string `json:"fileExt,omitempty"`
	FilePath *string `json:"filePath,omitempty"`
	FileSize *string `json:"fileSize,omitempty"`
	Type_ *string `json:"type,omitempty"`
	Source *string `json:"source,omitempty"`
	Status *string `json:"status,omitempty"`
	ErrorMessage *string `json:"errorMessage,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
