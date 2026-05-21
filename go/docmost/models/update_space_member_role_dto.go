package models

// UpdateSpaceMemberRoleDto from OpenAPI.
type UpdateSpaceMemberRoleDto struct {
	SpaceId string `json:"spaceId"`
	UserId *string `json:"userId,omitempty"`
	GroupId *string `json:"groupId,omitempty"`
	Role string `json:"role"`
}
