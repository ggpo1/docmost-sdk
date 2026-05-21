package models

// PasswordResetDto from OpenAPI.
type PasswordResetDto struct {
	Token string `json:"token"`
	NewPassword string `json:"newPassword"`
}
