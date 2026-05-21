package models

// CreateSsoProviderDto from OpenAPI.
type CreateSsoProviderDto struct {
	Name string `json:"name"`
	Type_ string `json:"type"`
	SamlUrl *string `json:"samlUrl,omitempty"`
	SamlCertificate *string `json:"samlCertificate,omitempty"`
	OidcIssuer *string `json:"oidcIssuer,omitempty"`
	OidcClientId *string `json:"oidcClientId,omitempty"`
	OidcClientSecret *string `json:"oidcClientSecret,omitempty"`
	LdapUrl *string `json:"ldapUrl,omitempty"`
	LdapBindDn *string `json:"ldapBindDn,omitempty"`
	LdapBindPassword *string `json:"ldapBindPassword,omitempty"`
	LdapBaseDn *string `json:"ldapBaseDn,omitempty"`
	LdapUserSearchFilter *string `json:"ldapUserSearchFilter,omitempty"`
	LdapUserAttributes map[string]any `json:"ldapUserAttributes,omitempty"`
	LdapTlsEnabled *bool `json:"ldapTlsEnabled,omitempty"`
	LdapTlsCaCert *string `json:"ldapTlsCaCert,omitempty"`
	AllowSignup *bool `json:"allowSignup,omitempty"`
	IsEnabled *bool `json:"isEnabled,omitempty"`
	GroupSync *bool `json:"groupSync,omitempty"`
}
