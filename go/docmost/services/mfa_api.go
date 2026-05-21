package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// MFAAPI implements MFA API.
type MFAAPI struct {
	http *httpclient.HTTPClient
}

func NewMFAAPI(http *httpclient.HTTPClient) *MFAAPI {
	return &MFAAPI{http: http}
}

func (a *MFAAPI) MfaSetup(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/setup", nil)
}

func (a *MFAAPI) MfaEnable(ctx context.Context, request *models.EnableMfaDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/enable", request)
}

func (a *MFAAPI) MfaDisable(ctx context.Context, request *models.DisableMfaDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/disable", request)
}

func (a *MFAAPI) MfaStatus(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/status", nil)
}

func (a *MFAAPI) MfaRegenerateBackupCodes(ctx context.Context, request *models.RegenerateBackupCodesDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/generate-backup-codes", request)
}

func (a *MFAAPI) MfaVerify(ctx context.Context, request *models.MfaDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/verify", request)
}

func (a *MFAAPI) MfaValidateAccess(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "mfa/validate-access", nil)
}

