package services

import (
	"fmt"
	"context"

	"net/url"
	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// SSOAPI implements SSO API.
type SSOAPI struct {
	http *httpclient.HTTPClient
}

func NewSSOAPI(http *httpclient.HTTPClient) *SSOAPI {
	return &SSOAPI{http: http}
}

func (a *SSOAPI) GetSsoProviders(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "sso/providers", request)
}

func (a *SSOAPI) GetSsoProvider(ctx context.Context, request *models.SsoProviderIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "sso/info", request)
}

func (a *SSOAPI) CreateSsoProvider(ctx context.Context, request *models.CreateSsoProviderDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "sso/create", request)
}

func (a *SSOAPI) UpdateSsoProvider(ctx context.Context, request *models.UpdateSsoProviderDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "sso/update", request)
}

func (a *SSOAPI) DeleteSsoProvider(ctx context.Context, request *models.SsoProviderIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "sso/delete", request)
}

func (a *SSOAPI) LdapLogin(ctx context.Context, request *models.LdapLoginDto, providerId string) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, fmt.Sprintf("sso/ldap/%s/login", url.PathEscape(providerId)), request)
}

