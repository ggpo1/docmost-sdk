package models

// DuplicatePageDto from OpenAPI.
type DuplicatePageDto struct {
	PageId string `json:"pageId"`
	SpaceId *string `json:"spaceId,omitempty"`
}
