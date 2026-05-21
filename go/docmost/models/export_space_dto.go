package models

// ExportSpaceDto from OpenAPI.
type ExportSpaceDto struct {
	SpaceId string `json:"spaceId"`
	Format string `json:"format"`
	IncludeAttachments *bool `json:"includeAttachments,omitempty"`
}
