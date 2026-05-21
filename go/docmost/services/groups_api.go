package services

import (
	"context"

	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// GroupsAPI implements Groups API.
type GroupsAPI struct {
	http *httpclient.HTTPClient
}

func NewGroupsAPI(http *httpclient.HTTPClient) *GroupsAPI {
	return &GroupsAPI{http: http}
}

func (a *GroupsAPI) GetWorkspaceGroups(ctx context.Context, request *models.PaginationOptions) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups", request)
}

func (a *GroupsAPI) GetGroupInfo(ctx context.Context, request *models.GroupIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/info", request)
}

func (a *GroupsAPI) CreateGroup(ctx context.Context, request *models.CreateGroupDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/create", request)
}

func (a *GroupsAPI) UpdateGroup(ctx context.Context, request *models.UpdateGroupDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/update", request)
}

func (a *GroupsAPI) GetGroupMembers(ctx context.Context) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/members", nil)
}

func (a *GroupsAPI) AddGroupMembers(ctx context.Context, request *models.AddGroupUserDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/members/add", request)
}

func (a *GroupsAPI) RemoveGroupMember(ctx context.Context, request *models.RemoveGroupUserDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/members/remove", request)
}

func (a *GroupsAPI) DeleteGroup(ctx context.Context, request *models.GroupIdDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "groups/delete", request)
}

