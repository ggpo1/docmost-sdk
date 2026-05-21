package services

import (
	"net/http"
	"fmt"
	"context"

	"net/url"
	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

// AttachmentsAPI implements Attachments API.
type AttachmentsAPI struct {
	http *httpclient.HTTPClient
}

func NewAttachmentsAPI(http *httpclient.HTTPClient) *AttachmentsAPI {
	return &AttachmentsAPI{http: http}
}

func (a *AttachmentsAPI) UploadFile(ctx context.Context, request *models.UploadFileRequest) (*httpclient.ApiResponse, error) {
	return a.http.PostMultipart(ctx, "files/upload", request)
}

func (a *AttachmentsAPI) GetFile(ctx context.Context, fileId string, fileName string) (*http.Response, error) {
	return a.http.GetRaw(ctx, fmt.Sprintf("files/%s/%s", url.PathEscape(fileId), url.PathEscape(fileName)), nil)
}

func (a *AttachmentsAPI) GetPublicFile(ctx context.Context, fileId string, fileName string, jwt *string) (*http.Response, error) {
	path := fmt.Sprintf("files/public/%s/%s", url.PathEscape(fileId), url.PathEscape(fileName))
	params := url.Values{}
	if jwt != nil {
		params.Set("jwt", *jwt)
	}
	return a.http.GetRaw(ctx, path, params)
}

func (a *AttachmentsAPI) UploadAvatarOrLogo(ctx context.Context, request *models.UploadAvatarOrLogoRequest) (*httpclient.ApiResponse, error) {
	return a.http.PostMultipart(ctx, "attachments/upload-image", request)
}

func (a *AttachmentsAPI) GetLogoOrAvatar(ctx context.Context, attachmentType string, fileName string) (*http.Response, error) {
	return a.http.GetRaw(ctx, fmt.Sprintf("attachments/img/%s/%s", url.PathEscape(attachmentType), url.PathEscape(fileName)), nil)
}

func (a *AttachmentsAPI) RemoveIcon(ctx context.Context, request *models.RemoveIconDto) (*httpclient.ApiResponse, error) {
	return a.http.Post(ctx, "attachments/remove-icon", request)
}

