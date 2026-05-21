package models

// OffsetPaginationMeta from OpenAPI.
type OffsetPaginationMeta struct {
	Limit *int `json:"limit,omitempty"`
	Page *int `json:"page,omitempty"`
	HasNextPage *bool `json:"hasNextPage,omitempty"`
	HasPrevPage *bool `json:"hasPrevPage,omitempty"`
}
