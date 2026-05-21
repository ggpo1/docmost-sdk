package models

// EnableMfaDto from OpenAPI.
type EnableMfaDto struct {
	Secret string `json:"secret"`
	VerificationCode string `json:"verificationCode"`
}
