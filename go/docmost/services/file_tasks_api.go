package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// FileTasksAPI implements File Tasks API.
type FileTasksAPI struct {
	http *httpclient.HTTPClient
}

func NewFileTasksAPI(http *httpclient.HTTPClient) *FileTasksAPI {
	return &FileTasksAPI{http: http}
}

func (a *FileTasksAPI) GetFileTasks(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "file-tasks", request)
}

func (a *FileTasksAPI) GetFileTask(ctx context.Context, request *models.FileTaskIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "file-tasks/info", request)
}

