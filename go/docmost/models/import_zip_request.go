package models

import "io"

// ImportZipRequest request.
type ImportZipRequest struct {
	File io.Reader `json:"file"`
	SpaceId string `json:"spaceId"`
	Source string `json:"source"`
	ParentPageId *string `json:"parentPageId,omitempty"`
}
