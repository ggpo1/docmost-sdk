package models

// UpdateWorkspaceDto from OpenAPI.
type UpdateWorkspaceDto struct {
	Name *string `json:"name,omitempty"`
	Hostname *string `json:"hostname,omitempty"`
	Description *string `json:"description,omitempty"`
	Logo *string `json:"logo,omitempty"`
	EmailDomains []string `json:"emailDomains,omitempty"`
	EnforceSso *bool `json:"enforceSso,omitempty"`
	EnforceMfa *bool `json:"enforceMfa,omitempty"`
	RestrictApiToAdmins *bool `json:"restrictApiToAdmins,omitempty"`
	AiSearch *bool `json:"aiSearch,omitempty"`
	GenerativeAi *bool `json:"generativeAi,omitempty"`
	DisablePublicSharing *bool `json:"disablePublicSharing,omitempty"`
}
