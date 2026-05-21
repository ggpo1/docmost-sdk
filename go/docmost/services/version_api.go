package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
)

// VersionAPI implements Version API.
type VersionAPI struct {
	http *httpclient.HTTPClient
}

func NewVersionAPI(http *httpclient.HTTPClient) *VersionAPI {
	return &VersionAPI{http: http}
}

func (a *VersionAPI) GetVersion(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "version", nil)
}

