package models

// CreatePageDto from OpenAPI.
type CreatePageDto struct {
	SpaceId string `json:"spaceId"`
	Title *string `json:"title,omitempty"`
	Icon *string `json:"icon,omitempty"`
	ParentPageId *string `json:"parentPageId,omitempty"`
	Content *string `json:"content,omitempty"`
	Format *string `json:"format,omitempty"`
}
