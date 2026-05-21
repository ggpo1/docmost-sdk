package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// PagesAPI implements Pages API.
type PagesAPI struct {
	http *httpclient.HTTPClient
}

func NewPagesAPI(http *httpclient.HTTPClient) *PagesAPI {
	return &PagesAPI{http: http}
}

func (a *PagesAPI) GetPage(ctx context.Context, request *models.PageInfoDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/info", request)
}

func (a *PagesAPI) CreatePage(ctx context.Context, request *models.CreatePageDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/create", request)
}

func (a *PagesAPI) UpdatePage(ctx context.Context, request *models.UpdatePageDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/update", request)
}

func (a *PagesAPI) DeletePage(ctx context.Context, request *models.DeletePageDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/delete", request)
}

func (a *PagesAPI) RestorePage(ctx context.Context, request *models.PageIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/restore", request)
}

func (a *PagesAPI) GetRecentPages(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/recent", nil)
}

func (a *PagesAPI) GetDeletedPages(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/trash", nil)
}

func (a *PagesAPI) GetPageHistory(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/history", nil)
}

func (a *PagesAPI) GetPageHistoryInfo(ctx context.Context, request *models.PageHistoryIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/history/info", request)
}

func (a *PagesAPI) GetSidebarPages(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/sidebar-pages", nil)
}

func (a *PagesAPI) MovePageToSpace(ctx context.Context, request *models.MovePageToSpaceDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/move-to-space", request)
}

func (a *PagesAPI) DuplicatePage(ctx context.Context, request *models.DuplicatePageDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/duplicate", request)
}

func (a *PagesAPI) MovePage(ctx context.Context, request *models.MovePageDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/move", request)
}

func (a *PagesAPI) GetPageBreadcrumbs(ctx context.Context, request *models.PageIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "pages/breadcrumbs", request)
}

