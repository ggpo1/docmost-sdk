package models

// CreateCloudWorkspaceDto from OpenAPI.
type CreateCloudWorkspaceDto struct {
	Name string `json:"name"`
	Email string `json:"email"`
	Password string `json:"password"`
}
