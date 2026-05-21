package models

// CreateCommentDto from OpenAPI.
type CreateCommentDto struct {
	PageId string `json:"pageId"`
	Content string `json:"content"`
	Selection *string `json:"selection,omitempty"`
	ParentCommentId *string `json:"parentCommentId,omitempty"`
}
