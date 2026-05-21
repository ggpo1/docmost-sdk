package models

// SidebarPage from OpenAPI.
type SidebarPage struct {
	Id *string `json:"id,omitempty"`
	SlugId *string `json:"slugId,omitempty"`
	Title *string `json:"title,omitempty"`
	Icon *string `json:"icon,omitempty"`
	Position *string `json:"position,omitempty"`
	ParentPageId *string `json:"parentPageId,omitempty"`
	HasChildren *bool `json:"hasChildren,omitempty"`
	SpaceId *string `json:"spaceId,omitempty"`
}
