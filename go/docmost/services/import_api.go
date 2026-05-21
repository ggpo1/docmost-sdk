package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// ImportAPI implements Import API.
type ImportAPI struct {
	http *httpclient.HTTPClient
}

func NewImportAPI(http *httpclient.HTTPClient) *ImportAPI {
	return &ImportAPI{http: http}
}

func (a *ImportAPI) ImportPage(ctx context.Context, request *models.ImportPageRequest) (*httpclient.ApiResponse, error) {
	return a.http.PostMultipart(ctx, "pages/import", request)
}

func (a *ImportAPI) ImportZip(ctx context.Context, request *models.ImportZipRequest) (*httpclient.ApiResponse, error) {
	return a.http.PostMultipart(ctx, "pages/import-zip", request)
}

