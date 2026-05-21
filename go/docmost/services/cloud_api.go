package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// CloudAPI implements Cloud API.
type CloudAPI struct {
	http *httpclient.HTTPClient
}

func NewCloudAPI(http *httpclient.HTTPClient) *CloudAPI {
	return &CloudAPI{http: http}
}

func (a *CloudAPI) CreateCloudWorkspace(ctx context.Context, request *models.CreateCloudWorkspaceDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/create", request)
}

func (a *CloudAPI) GetJoinedWorkspaces(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/joined", nil)
}

