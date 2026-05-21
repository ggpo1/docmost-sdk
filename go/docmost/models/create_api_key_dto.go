package models

// CreateApiKeyDto from OpenAPI.
type CreateApiKeyDto struct {
	Name string `json:"name"`
	ExpiresAt *string `json:"expiresAt,omitempty"`
}
