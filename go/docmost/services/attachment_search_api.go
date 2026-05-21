package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// AttachmentSearchAPI implements Attachment Search API.
type AttachmentSearchAPI struct {
	http *httpclient.HTTPClient
}

func NewAttachmentSearchAPI(http *httpclient.HTTPClient) *AttachmentSearchAPI {
	return &AttachmentSearchAPI{http: http}
}

func (a *AttachmentSearchAPI) SearchAttachments(ctx context.Context, request *models.SearchDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "search-attachments", request)
}

func (a *AttachmentSearchAPI) TriggerAttachmentIndexing(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "search-attachments/indexing", nil)
}

