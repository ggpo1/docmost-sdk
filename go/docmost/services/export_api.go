package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// ExportAPI implements Export API.
type ExportAPI struct {
	http *httpclient.HTTPClient
}

func NewExportAPI(http *httpclient.HTTPClient) *ExportAPI {
	return &ExportAPI{http: http}
}

func (a *ExportAPI) ExportPage(ctx context.Context, request *models.ExportPageDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/export", request)
}

func (a *ExportAPI) ExportSpace(ctx context.Context, request *models.ExportSpaceDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/export", request)
}

