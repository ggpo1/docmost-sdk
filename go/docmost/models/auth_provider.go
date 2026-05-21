package models

// AuthProvider from OpenAPI.
type AuthProvider struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Type_ *string `json:"type,omitempty"`
	IsEnabled *bool `json:"isEnabled,omitempty"`
	AllowSignup *bool `json:"allowSignup,omitempty"`
	GroupSync *bool `json:"groupSync,omitempty"`
	SamlUrl *string `json:"samlUrl,omitempty"`
	SamlCertificate *string `json:"samlCertificate,omitempty"`
	OidcIssuer *string `json:"oidcIssuer,omitempty"`
	OidcClientId *string `json:"oidcClientId,omitempty"`
	OidcClientSecret *string `json:"oidcClientSecret,omitempty"`
	LdapUrl *string `json:"ldapUrl,omitempty"`
	LdapBindDn *string `json:"ldapBindDn,omitempty"`
	LdapBaseDn *string `json:"ldapBaseDn,omitempty"`
	LdapUserSearchFilter *string `json:"ldapUserSearchFilter,omitempty"`
	LdapUserAttributes map[string]any `json:"ldapUserAttributes,omitempty"`
	LdapTlsEnabled *string `json:"ldapTlsEnabled,omitempty"`
	LdapTlsCaCert *string `json:"ldapTlsCaCert,omitempty"`
	CreatorId *string `json:"creatorId,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
