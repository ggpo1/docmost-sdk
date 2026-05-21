package models

// ChangePasswordDto from OpenAPI.
type ChangePasswordDto struct {
	OldPassword string `json:"oldPassword"`
	NewPassword string `json:"newPassword"`
}
