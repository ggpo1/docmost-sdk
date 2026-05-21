package models

// WorkspacePublicInfo from OpenAPI.
type WorkspacePublicInfo struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Logo *string `json:"logo,omitempty"`
	Hostname *string `json:"hostname,omitempty"`
	EnforceSso *bool `json:"enforceSso,omitempty"`
	HasLicenseKey *bool `json:"hasLicenseKey,omitempty"`
	AuthProviders []map[string]any `json:"authProviders,omitempty"`
}
