package models

// ResolveCommentDto from OpenAPI.
type ResolveCommentDto struct {
	CommentId string `json:"commentId"`
	Resolved bool `json:"resolved"`
}
