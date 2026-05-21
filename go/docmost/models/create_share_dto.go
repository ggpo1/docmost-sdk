package models

// CreateShareDto from OpenAPI.
type CreateShareDto struct {
	PageId string `json:"pageId"`
	IncludeSubPages *bool `json:"includeSubPages,omitempty"`
	SearchIndexing *bool `json:"searchIndexing,omitempty"`
}
