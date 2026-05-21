package models

// User from OpenAPI.
type User struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Email *string `json:"email,omitempty"`
	EmailVerifiedAt *string `json:"emailVerifiedAt,omitempty"`
	AvatarUrl *string `json:"avatarUrl,omitempty"`
	Role *string `json:"role,omitempty"`
	Locale *string `json:"locale,omitempty"`
	Timezone *string `json:"timezone,omitempty"`
	Settings *string `json:"settings,omitempty"`
	HasGeneratedPassword *string `json:"hasGeneratedPassword,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	LastLoginAt *string `json:"lastLoginAt,omitempty"`
	DeactivatedAt *string `json:"deactivatedAt,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
