package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// APIKeysAPI implements API Keys API.
type APIKeysAPI struct {
	http *httpclient.HTTPClient
}

func NewAPIKeysAPI(http *httpclient.HTTPClient) *APIKeysAPI {
	return &APIKeysAPI{http: http}
}

func (a *APIKeysAPI) GetApiKeys(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "api-keys", request)
}

func (a *APIKeysAPI) CreateApiKey(ctx context.Context, request *models.CreateApiKeyDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "api-keys/create", request)
}

func (a *APIKeysAPI) UpdateApiKey(ctx context.Context, request *models.UpdateApiKeyDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "api-keys/update", request)
}

func (a *APIKeysAPI) RevokeApiKey(ctx context.Context, request *models.RevokeApiKeyDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "api-keys/revoke", request)
}

