package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// UsersAPI implements Users API.
type UsersAPI struct {
	http *httpclient.HTTPClient
}

func NewUsersAPI(http *httpclient.HTTPClient) *UsersAPI {
	return &UsersAPI{http: http}
}

func (a *UsersAPI) GetUserInfo(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "users/me", nil)
}

func (a *UsersAPI) UpdateUser(ctx context.Context, request *models.UpdateUserDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "users/update", request)
}

