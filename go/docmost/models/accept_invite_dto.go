package models

// AcceptInviteDto from OpenAPI.
type AcceptInviteDto struct {
	InvitationId string `json:"invitationId"`
	Name string `json:"name"`
	Password string `json:"password"`
	Token string `json:"token"`
}
