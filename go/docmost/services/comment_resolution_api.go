package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// CommentResolutionAPI implements Comment Resolution API.
type CommentResolutionAPI struct {
	http *httpclient.HTTPClient
}

func NewCommentResolutionAPI(http *httpclient.HTTPClient) *CommentResolutionAPI {
	return &CommentResolutionAPI{http: http}
}

func (a *CommentResolutionAPI) ResolveComment(ctx context.Context, request *models.ResolveCommentDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "comments/resolve", request)
}

