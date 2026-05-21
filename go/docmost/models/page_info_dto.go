package models

// PageInfoDto from OpenAPI.
type PageInfoDto struct {
	PageId string `json:"pageId"`
	IncludeSpace *bool `json:"includeSpace,omitempty"`
	IncludeContent *bool `json:"includeContent,omitempty"`
	Format *string `json:"format,omitempty"`
}
