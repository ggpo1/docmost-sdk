package models

// ApiResponse is the standard API envelope.
type ApiResponse struct {
	Data    any  `json:"data,omitempty"`
	Success bool `json:"success"`
	Status  int  `json:"status"`
}

// ErrorResponse is returned on HTTP errors.
type ErrorResponse struct {
	StatusCode int      `json:"statusCode,omitempty"`
	Message    any      `json:"message,omitempty"`
	Error      string   `json:"error,omitempty"`
}
