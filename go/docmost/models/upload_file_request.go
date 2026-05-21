package models

import "io"

// UploadFileRequest request.
type UploadFileRequest struct {
	File io.Reader `json:"file"`
	PageId string `json:"pageId"`
	AttachmentId *string `json:"attachmentId,omitempty"`
}
