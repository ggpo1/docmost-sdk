package docmost

import "github.com/ggpo1/docmost-sdk/go/internal/httpclient"

// Re-export HTTP and response types for convenience.
type (
	ApiResponse   = httpclient.ApiResponse
	APIError      = httpclient.APIError
	ErrorResponse = httpclient.ErrorResponse
	HTTPClient    = httpclient.HTTPClient
	HTTPOptions   = httpclient.HTTPOptions
)

var NewHTTPClient = httpclient.NewHTTPClient
