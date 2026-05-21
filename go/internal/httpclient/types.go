package httpclient

import "encoding/json"

// ApiResponse is the standard API envelope.
type ApiResponse struct {
	Data    json.RawMessage `json:"data,omitempty"`
	Success bool            `json:"success"`
	Status  int             `json:"status"`
}

// ParseData unmarshals response.Data into dest.
func (r *ApiResponse) ParseData(dest any) error {
	if len(r.Data) == 0 || string(r.Data) == "null" {
		return nil
	}
	return json.Unmarshal(r.Data, dest)
}
