package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// SpacesAPI implements Spaces API.
type SpacesAPI struct {
	http *httpclient.HTTPClient
}

func NewSpacesAPI(http *httpclient.HTTPClient) *SpacesAPI {
	return &SpacesAPI{http: http}
}

func (a *SpacesAPI) GetWorkspaceSpaces(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces", request)
}

func (a *SpacesAPI) GetSpaceInfo(ctx context.Context, request *models.SpaceIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/info", request)
}

func (a *SpacesAPI) CreateSpace(ctx context.Context, request *models.CreateSpaceDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/create", request)
}

func (a *SpacesAPI) UpdateSpace(ctx context.Context, request *models.UpdateSpaceDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/update", request)
}

func (a *SpacesAPI) DeleteSpace(ctx context.Context, request *models.SpaceIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/delete", request)
}

func (a *SpacesAPI) GetSpaceMembers(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/members", nil)
}

func (a *SpacesAPI) AddSpaceMembers(ctx context.Context, request *models.AddSpaceMembersDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/members/add", request)
}

func (a *SpacesAPI) RemoveSpaceMember(ctx context.Context, request *models.RemoveSpaceMemberDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/members/remove", request)
}

func (a *SpacesAPI) UpdateSpaceMemberRole(ctx context.Context, request *models.UpdateSpaceMemberRoleDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "spaces/members/change-role", request)
}

