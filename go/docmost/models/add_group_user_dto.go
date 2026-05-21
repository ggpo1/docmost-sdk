package models

// AddGroupUserDto from OpenAPI.
type AddGroupUserDto struct {
	GroupId string `json:"groupId"`
	UserIds []string `json:"userIds"`
}
