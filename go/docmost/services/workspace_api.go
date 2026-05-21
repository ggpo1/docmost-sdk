package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// WorkspaceAPI implements Workspace API.
type WorkspaceAPI struct {
	http *httpclient.HTTPClient
}

func NewWorkspaceAPI(http *httpclient.HTTPClient) *WorkspaceAPI {
	return &WorkspaceAPI{http: http}
}

func (a *WorkspaceAPI) GetWorkspacePublicInfo(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/public", nil)
}

func (a *WorkspaceAPI) GetWorkspaceInfo(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/info", nil)
}

func (a *WorkspaceAPI) UpdateWorkspace(ctx context.Context, request *models.UpdateWorkspaceDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/update", request)
}

func (a *WorkspaceAPI) GetWorkspaceMembers(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/members", request)
}

func (a *WorkspaceAPI) DeactivateWorkspaceMember(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/members/deactivate", nil)
}

func (a *WorkspaceAPI) DeleteWorkspaceMember(ctx context.Context, request *models.RemoveWorkspaceUserDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/members/delete", request)
}

func (a *WorkspaceAPI) UpdateWorkspaceMemberRole(ctx context.Context, request *models.UpdateWorkspaceUserRoleDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/members/change-role", request)
}

func (a *WorkspaceAPI) GetInvitations(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites", request)
}

func (a *WorkspaceAPI) GetInvitationById(ctx context.Context, request *models.InvitationIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites/info", request)
}

func (a *WorkspaceAPI) InviteUser(ctx context.Context, request *models.InviteUserDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites/create", request)
}

func (a *WorkspaceAPI) ResendInvite(ctx context.Context, request *models.InvitationIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites/resend", request)
}

func (a *WorkspaceAPI) RevokeInvite(ctx context.Context, request *models.InvitationIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites/revoke", request)
}

func (a *WorkspaceAPI) AcceptInvite(ctx context.Context, request *models.AcceptInviteDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites/accept", request)
}

func (a *WorkspaceAPI) GetInviteLink(ctx context.Context, request *models.InvitationIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/invites/link", request)
}

func (a *WorkspaceAPI) CheckHostname(ctx context.Context, request *models.CheckHostnameDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "workspace/check-hostname", request)
}

