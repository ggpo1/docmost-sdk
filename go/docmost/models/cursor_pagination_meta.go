package models

// CursorPaginationMeta from OpenAPI.
type CursorPaginationMeta struct {
	Limit *int `json:"limit,omitempty"`
	HasNextPage *bool `json:"hasNextPage,omitempty"`
	HasPrevPage *bool `json:"hasPrevPage,omitempty"`
	NextCursor *string `json:"nextCursor,omitempty"`
	PrevCursor *string `json:"prevCursor,omitempty"`
}
