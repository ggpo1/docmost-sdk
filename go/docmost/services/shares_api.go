package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// SharesAPI implements Shares API.
type SharesAPI struct {
	http *httpclient.HTTPClient
}

func NewSharesAPI(http *httpclient.HTTPClient) *SharesAPI {
	return &SharesAPI{http: http}
}

func (a *SharesAPI) GetShares(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares", request)
}

func (a *SharesAPI) GetSharedPageInfo(ctx context.Context, request *models.ShareInfoDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/page-info", request)
}

func (a *SharesAPI) GetShare(ctx context.Context, request *models.ShareIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/info", request)
}

func (a *SharesAPI) GetShareForPage(ctx context.Context, request *models.SharePageIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/for-page", request)
}

func (a *SharesAPI) CreateShare(ctx context.Context, request *models.CreateShareDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/create", request)
}

func (a *SharesAPI) UpdateShare(ctx context.Context, request *models.UpdateShareDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/update", request)
}

func (a *SharesAPI) DeleteShare(ctx context.Context, request *models.ShareIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/delete", request)
}

func (a *SharesAPI) GetSharePageTree(ctx context.Context, request *models.ShareIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "shares/tree", request)
}

