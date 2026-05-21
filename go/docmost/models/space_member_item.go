package models

// SpaceMemberItem from OpenAPI.
type SpaceMemberItem struct {
	Id *string `json:"id,omitempty"`
	Name *string `json:"name,omitempty"`
	Type_ *string `json:"type,omitempty"`
	Email *string `json:"email,omitempty"`
	AvatarUrl *string `json:"avatarUrl,omitempty"`
	MemberCount *int `json:"memberCount,omitempty"`
	IsDefault *bool `json:"isDefault,omitempty"`
	Role *string `json:"role,omitempty"`
	CreatedAt *string `json:"createdAt,omitempty"`
}
