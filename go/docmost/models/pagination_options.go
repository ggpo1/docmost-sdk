package models

// PaginationOptions from OpenAPI.
type PaginationOptions struct {
	Limit *int `json:"limit,omitempty"`
	Cursor *string `json:"cursor,omitempty"`
	Query *string `json:"query,omitempty"`
	AdminView *bool `json:"adminView,omitempty"`
}
