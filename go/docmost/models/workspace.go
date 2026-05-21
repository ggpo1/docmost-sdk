package models

// Workspace from OpenAPI.
type Workspace struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Description *string `json:"description,omitempty"`
	Logo *string `json:"logo,omitempty"`
	Hostname *string `json:"hostname,omitempty"`
	CustomDomain *string `json:"customDomain,omitempty"`
	DefaultRole *string `json:"defaultRole,omitempty"`
	DefaultSpaceId *string `json:"defaultSpaceId,omitempty"`
	EmailDomains *string `json:"emailDomains,omitempty"`
	EnforceSso *bool `json:"enforceSso,omitempty"`
	EnforceMfa *string `json:"enforceMfa,omitempty"`
	Settings *string `json:"settings,omitempty"`
	Plan *string `json:"plan,omitempty"`
	Status *string `json:"status,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
