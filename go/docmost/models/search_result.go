package models

// SearchResult from OpenAPI.
type SearchResult struct {
	Id *string `json:"id,omitempty"`
	Title *string `json:"title,omitempty"`
	Icon *string `json:"icon,omitempty"`
	ParentPageId *string `json:"parentPageId,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	Rank *float64 `json:"rank,omitempty"`
	Highlight *string `json:"highlight,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
	Space *SpaceSummary `json:"space,omitempty"`
}
