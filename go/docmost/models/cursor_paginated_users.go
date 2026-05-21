package models

// CursorPaginatedUsers from OpenAPI.
type CursorPaginatedUsers struct {
	Items []User `json:"items,omitempty"`
	Meta *CursorPaginationMeta `json:"meta,omitempty"`
}
