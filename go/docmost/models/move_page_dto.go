package models

// MovePageDto from OpenAPI.
type MovePageDto struct {
	PageId string `json:"pageId"`
	Position string `json:"position"`
	ParentPageId *string `json:"parentPageId,omitempty"`
}
