package httpclient

import "fmt"

// APIError is returned when the Docmost API returns an error HTTP status or success=false.
type APIError struct {
	StatusCode int
	Message    string
	Body       *ErrorResponse
}

func (e *APIError) Error() string {
	if e.Message != "" {
		return e.Message
	}
	return fmt.Sprintf("docmost api error: status %d", e.StatusCode)
}

// ErrorResponse is the API error payload.
type ErrorResponse struct {
	StatusCode int    `json:"statusCode,omitempty"`
	Message    any    `json:"message,omitempty"`
	Error      string `json:"error,omitempty"`
}
