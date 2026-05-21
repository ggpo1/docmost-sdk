package models

// UpdateUserDto from OpenAPI.
type UpdateUserDto struct {
	Name *string `json:"name,omitempty"`
	Email *string `json:"email,omitempty"`
	AvatarUrl *string `json:"avatarUrl,omitempty"`
	FullPageWidth *bool `json:"fullPageWidth,omitempty"`
	PageEditMode *string `json:"pageEditMode,omitempty"`
	Locale *string `json:"locale,omitempty"`
	ConfirmPassword *string `json:"confirmPassword,omitempty"`
}
