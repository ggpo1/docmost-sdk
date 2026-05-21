package models

// DeletePageDto from OpenAPI.
type DeletePageDto struct {
	PageId string `json:"pageId"`
	PermanentlyDelete *bool `json:"permanentlyDelete,omitempty"`
}
