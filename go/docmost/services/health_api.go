package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
)

// HealthAPI implements Health API.
type HealthAPI struct {
	http *httpclient.HTTPClient
}

func NewHealthAPI(http *httpclient.HTTPClient) *HealthAPI {
	return &HealthAPI{http: http}
}

func (a *HealthAPI) HealthCheck(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Get(ctx, "health", nil)
}

func (a *HealthAPI) Liveness(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Get(ctx, "health/live", nil)
}

