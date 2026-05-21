package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// LicenseAPI implements License API.
type LicenseAPI struct {
	http *httpclient.HTTPClient
}

func NewLicenseAPI(http *httpclient.HTTPClient) *LicenseAPI {
	return &LicenseAPI{http: http}
}

func (a *LicenseAPI) GetLicenseInfo(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "license/info", nil)
}

func (a *LicenseAPI) ActivateLicense(ctx context.Context, request *models.ActivateLicenseDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "license/activate", request)
}

func (a *LicenseAPI) RemoveLicense(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "license/remove", nil)
}

