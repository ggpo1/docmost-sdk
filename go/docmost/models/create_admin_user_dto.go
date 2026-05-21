package models

// CreateAdminUserDto from OpenAPI.
type CreateAdminUserDto struct {
	Name string `json:"name"`
	Email string `json:"email"`
	Password string `json:"password"`
	WorkspaceName *string `json:"workspaceName,omitempty"`
	Hostname *string `json:"hostname,omitempty"`
}
