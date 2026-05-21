package models

// UpdatePageDto from OpenAPI.
type UpdatePageDto struct {
	PageId string `json:"pageId"`
	Title *string `json:"title,omitempty"`
	Icon *string `json:"icon,omitempty"`
	Content *string `json:"content,omitempty"`
	Format *string `json:"format,omitempty"`
	Operation *string `json:"operation,omitempty"`
}
