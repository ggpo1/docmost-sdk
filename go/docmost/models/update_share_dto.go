package models

// UpdateShareDto from OpenAPI.
type UpdateShareDto struct {
	ShareId string `json:"shareId"`
	PageId *string `json:"pageId,omitempty"`
	IncludeSubPages *bool `json:"includeSubPages,omitempty"`
	SearchIndexing *bool `json:"searchIndexing,omitempty"`
}
