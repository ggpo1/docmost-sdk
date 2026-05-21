package models

// InviteUserDto from OpenAPI.
type InviteUserDto struct {
	Emails []string `json:"emails"`
	GroupIds []string `json:"groupIds,omitempty"`
	Role string `json:"role"`
}
