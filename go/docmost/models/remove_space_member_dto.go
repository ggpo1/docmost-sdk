package models

// RemoveSpaceMemberDto from OpenAPI.
type RemoveSpaceMemberDto struct {
	SpaceId string `json:"spaceId"`
	UserId *string `json:"userId,omitempty"`
	GroupId *string `json:"groupId,omitempty"`
}
