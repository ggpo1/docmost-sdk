package models

// ApiKey from OpenAPI.
type ApiKey struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	ExpiresAt *string `json:"expiresAt,omitempty"`
	LastUsedAt *string `json:"lastUsedAt,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
