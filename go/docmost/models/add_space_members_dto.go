package models

// AddSpaceMembersDto from OpenAPI.
type AddSpaceMembersDto struct {
	SpaceId string `json:"spaceId"`
	Role string `json:"role"`
	UserIds []string `json:"userIds,omitempty"`
	GroupIds []string `json:"groupIds,omitempty"`
}
