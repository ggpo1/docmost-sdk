package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// AIAPI implements AI API.
type AIAPI struct {
	http *httpclient.HTTPClient
}

func NewAIAPI(http *httpclient.HTTPClient) *AIAPI {
	return &AIAPI{http: http}
}

func (a *AIAPI) AiAnswers(ctx context.Context, request *models.SearchDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "ai/answers", request)
}

