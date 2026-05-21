package docmost

import (
	"context"
	"fmt"
	"time"

	"github.com/ggpo1/docmost-sdk/go/docmost/services"
	"github.com/ggpo1/docmost-sdk/go/internal/httpclient"
)

// Client is the entry point for the Docmost API.
type DocmostClient struct {
	HTTP *httpclient.HTTPClient

	Auth              *services.AuthAPI
	Users             *services.UsersAPI
	Workspace         *services.WorkspaceAPI
	Spaces            *services.SpacesAPI
	Pages             *services.PagesAPI
	Comments          *services.CommentsAPI
	Attachments       *services.AttachmentsAPI
	Search            *services.SearchAPI
	AttachmentSearch  *services.AttachmentSearchAPI
	Shares            *services.SharesAPI
	Groups            *services.GroupsAPI
	Export            *services.ExportAPI
	Import            *services.ImportAPI
	FileTasks         *services.FileTasksAPI
	Health            *services.HealthAPI
	Version           *services.VersionAPI
	APIKeys           *services.APIKeysAPI
	MFA               *services.MFAAPI
	CommentResolution *services.CommentResolutionAPI
	License           *services.LicenseAPI
	SSO               *services.SSOAPI
	AI                *services.AIAPI
	Cloud             *services.CloudAPI
}

// ClientOptions configures DocmostClient.
type ClientOptions struct {
	APIToken       string
	Email          string
	Password       string
	LoginOnStartup bool
	Timeout        int // seconds, 0 = default 100s
}

// NewClient creates a Docmost API client.
func NewClient(baseURL string, opts ClientOptions) (*DocmostClient, error) {
	httpOpts := httpclient.HTTPOptions{
		APIToken: opts.APIToken,
		Email:    opts.Email,
		Password: opts.Password,
	}
	if opts.Timeout > 0 {
		httpOpts.Timeout = time.Duration(opts.Timeout) * time.Second
	}
	http, err := httpclient.NewHTTPClient(baseURL, httpOpts)
	if err != nil {
		return nil, err
	}
	c := &DocmostClient{HTTP: http}
	c.wireServices()
	if opts.LoginOnStartup && opts.Email != "" && opts.Password != "" && opts.APIToken == "" {
		if err := http.Login(context.Background()); err != nil {
			return nil, err
		}
	}
	return c, nil
}

func (c *DocmostClient) wireServices() {
	c.Auth = services.NewAuthAPI(c.HTTP)
	c.Users = services.NewUsersAPI(c.HTTP)
	c.Workspace = services.NewWorkspaceAPI(c.HTTP)
	c.Spaces = services.NewSpacesAPI(c.HTTP)
	c.Pages = services.NewPagesAPI(c.HTTP)
	c.Comments = services.NewCommentsAPI(c.HTTP)
	c.Attachments = services.NewAttachmentsAPI(c.HTTP)
	c.Search = services.NewSearchAPI(c.HTTP)
	c.AttachmentSearch = services.NewAttachmentSearchAPI(c.HTTP)
	c.Shares = services.NewSharesAPI(c.HTTP)
	c.Groups = services.NewGroupsAPI(c.HTTP)
	c.Export = services.NewExportAPI(c.HTTP)
	c.Import = services.NewImportAPI(c.HTTP)
	c.FileTasks = services.NewFileTasksAPI(c.HTTP)
	c.Health = services.NewHealthAPI(c.HTTP)
	c.Version = services.NewVersionAPI(c.HTTP)
	c.APIKeys = services.NewAPIKeysAPI(c.HTTP)
	c.MFA = services.NewMFAAPI(c.HTTP)
	c.CommentResolution = services.NewCommentResolutionAPI(c.HTTP)
	c.License = services.NewLicenseAPI(c.HTTP)
	c.SSO = services.NewSSOAPI(c.HTTP)
	c.AI = services.NewAIAPI(c.HTTP)
	c.Cloud = services.NewCloudAPI(c.HTTP)
}

// Login authenticates with email/password.
func (c *DocmostClient) Login(ctx context.Context) error {
	return c.HTTP.Login(ctx)
}

// Logout clears the session cookie.
func (c *DocmostClient) Logout(ctx context.Context) (*ApiResponse, error) {
	return c.HTTP.Logout(ctx)
}

// NewClientWithToken is a shortcut for API token auth.
func NewClientWithToken(baseURL, apiToken string) (*DocmostClient, error) {
	return NewClient(baseURL, ClientOptions{APIToken: apiToken, LoginOnStartup: false})
}

// NewClientWithCredentials is a shortcut for email/password auth.
func NewClientWithCredentials(baseURL, email, password string) (*DocmostClient, error) {
	if email == "" || password == "" {
		return nil, fmt.Errorf("email and password are required")
	}
	return NewClient(baseURL, ClientOptions{
		Email:          email,
		Password:       password,
		LoginOnStartup: true,
	})
}
