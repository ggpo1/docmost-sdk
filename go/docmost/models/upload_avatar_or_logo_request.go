package models

import "io"

// UploadAvatarOrLogoRequest request.
type UploadAvatarOrLogoRequest struct {
	File io.Reader `json:"file"`
	Type string `json:"type"`
	SpaceId *string `json:"spaceId,omitempty"`
}
