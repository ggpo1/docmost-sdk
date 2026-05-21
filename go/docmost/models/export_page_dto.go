package models

// ExportPageDto from OpenAPI.
type ExportPageDto struct {
	PageId string `json:"pageId"`
	Format string `json:"format"`
	IncludeChildren *bool `json:"includeChildren,omitempty"`
	IncludeAttachments *bool `json:"includeAttachments,omitempty"`
}
