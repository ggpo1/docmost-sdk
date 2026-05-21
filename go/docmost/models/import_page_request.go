package models

import "io"

// ImportPageRequest request.
type ImportPageRequest struct {
	File io.Reader `json:"file"`
	SpaceId string `json:"spaceId"`
	ParentPageId *string `json:"parentPageId,omitempty"`
}
