package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// SearchAPI implements Search API.
type SearchAPI struct {
	http *httpclient.HTTPClient
}

func NewSearchAPI(http *httpclient.HTTPClient) *SearchAPI {
	return &SearchAPI{http: http}
}

func (a *SearchAPI) PageSearch(ctx context.Context, request *models.SearchDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "search", request)
}

func (a *SearchAPI) SearchSuggestions(ctx context.Context, request *models.SearchSuggestionDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "search/suggest", request)
}

func (a *SearchAPI) SearchShare(ctx context.Context, request *models.SearchShareDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "search/share-search", request)
}

