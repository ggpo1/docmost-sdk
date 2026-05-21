package models

// FindPageCommentsRequest request.
type FindPageCommentsRequest struct {
	PageId string `json:"pageId"`
	Limit *int `json:"limit,omitempty"`
	Cursor *string `json:"cursor,omitempty"`
}
