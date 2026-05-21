package models

// WorkspaceInvitation from OpenAPI.
type WorkspaceInvitation struct {
	Id *string `json:"id,omitempty"`
	Email *string `json:"email,omitempty"`
	Role *string `json:"role,omitempty"`
	Token *string `json:"token,omitempty"`
	GroupIds *string `json:"groupIds,omitempty"`
	InvitedById *string `json:"invitedById,omitempty"`
	WorkspaceId *string `json:"workspaceId,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
	UpdatedAt *string `json:"updatedAt,omitempty"`
}
