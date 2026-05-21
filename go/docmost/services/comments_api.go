package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// CommentsAPI implements Comments API.
type CommentsAPI struct {
	http *httpclient.HTTPClient
}

func NewCommentsAPI(http *httpclient.HTTPClient) *CommentsAPI {
	return &CommentsAPI{http: http}
}

func (a *CommentsAPI) CreateComment(ctx context.Context, request *models.CreateCommentDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "comments/create", request)
}

func (a *CommentsAPI) FindPageComments(ctx context.Context, request *models.FindPageCommentsRequest) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "comments", request)
}

func (a *CommentsAPI) GetComment(ctx context.Context, request *models.CommentIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "comments/info", request)
}

func (a *CommentsAPI) UpdateComment(ctx context.Context, request *models.UpdateCommentDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "comments/update", request)
}

func (a *CommentsAPI) DeleteComment(ctx context.Context, request *models.CommentIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "comments/delete", request)
}

