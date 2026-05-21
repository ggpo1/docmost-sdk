package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// AuthAPI implements Auth API.
type AuthAPI struct {
	http *httpclient.HTTPClient
}

func NewAuthAPI(http *httpclient.HTTPClient) *AuthAPI {
	return &AuthAPI{http: http}
}

func (a *AuthAPI) Login(ctx context.Context, request *models.LoginDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/login", request)
}

func (a *AuthAPI) SetupWorkspace(ctx context.Context, request *models.CreateAdminUserDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/setup", request)
}

func (a *AuthAPI) ChangePassword(ctx context.Context, request *models.ChangePasswordDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/change-password", request)
}

func (a *AuthAPI) ForgotPassword(ctx context.Context, request *models.ForgotPasswordDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/forgot-password", request)
}

func (a *AuthAPI) PasswordReset(ctx context.Context, request *models.PasswordResetDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/password-reset", request)
}

func (a *AuthAPI) VerifyResetToken(ctx context.Context, request *models.VerifyUserTokenDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/verify-token", request)
}

func (a *AuthAPI) CollabToken(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/collab-token", nil)
}

func (a *AuthAPI) Logout(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "auth/logout", nil)
}

