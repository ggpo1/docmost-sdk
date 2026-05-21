package httpclient

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"reflect"
	"strings"
	"sync"
	"time"
)

// HTTPClient performs authenticated requests to the Docmost API.
type HTTPClient struct {
	baseURL    string
	apiToken   string
	email      string
	password   string
	client     *http.Client
	loggedIn   bool
	loginMu    sync.Mutex
}

// HTTPOptions configures HTTPClient.
type HTTPOptions struct {
	APIToken string
	Email    string
	Password string
	Timeout  time.Duration
}

// NewHTTPClient creates a client for baseURL (e.g. https://docs.example.com).
func NewHTTPClient(baseURL string, opts HTTPOptions) (*HTTPClient, error) {
	if opts.APIToken != "" && (opts.Email != "" || opts.Password != "") {
		return nil, fmt.Errorf("use either APIToken or Email/Password, not both")
	}
	jar, err := cookiejar.New(nil)
	if err != nil {
		return nil, err
	}
	timeout := opts.Timeout
	if timeout == 0 {
		timeout = 100 * time.Second
	}
	return &HTTPClient{
		baseURL:  strings.TrimRight(baseURL, "/") + "/api/",
		apiToken: opts.APIToken,
		email:    opts.Email,
		password: opts.Password,
		client: &http.Client{
			Timeout: timeout,
			Jar:     jar,
		},
	}, nil
}

func (c *HTTPClient) EnsureAuthenticated(ctx context.Context) error {
	if c.apiToken != "" {
		return nil
	}
	if c.email == "" || c.password == "" {
		return fmt.Errorf("provide APIToken or Email and Password")
	}
	c.loginMu.Lock()
	defer c.loginMu.Unlock()
	if c.loggedIn {
		return nil
	}
	return c.login(ctx)
}

// Login authenticates with email/password (cookie session).
func (c *HTTPClient) Login(ctx context.Context) error {
	c.loginMu.Lock()
	defer c.loginMu.Unlock()
	return c.login(ctx)
}

func (c *HTTPClient) login(ctx context.Context) error {
	body := map[string]string{"email": c.email, "password": c.password}
	_, err := c.Post(ctx, "auth/login", body)
	if err != nil {
		return err
	}
	c.loggedIn = true
	return nil
}

// Logout clears the session cookie.
func (c *HTTPClient) Logout(ctx context.Context) (*ApiResponse, error) {
	resp, err := c.Post(ctx, "auth/logout", nil)
	if err != nil {
		return nil, err
	}
	c.loggedIn = false
	return resp, nil
}

// Post sends a JSON POST request.
func (c *HTTPClient) Post(ctx context.Context, path string, body any) (*ApiResponse, error) {
	if err := c.EnsureAuthenticated(ctx); err != nil {
		return nil, err
	}
	var reader io.Reader
	if body != nil {
		b, err := json.Marshal(body)
		if err != nil {
			return nil, err
		}
		reader = bytes.NewReader(b)
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, c.url(path), reader)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "application/json")
	c.applyAuth(req)
	return c.do(req)
}

// Get sends a GET request.
func (c *HTTPClient) Get(ctx context.Context, path string, params url.Values) (*ApiResponse, error) {
	if err := c.EnsureAuthenticated(ctx); err != nil {
		return nil, err
	}
	u := c.url(path)
	if len(params) > 0 {
		u += "?" + params.Encode()
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, u, nil)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Accept", "application/json")
	c.applyAuth(req)
	return c.do(req)
}

// GetRaw returns the raw HTTP response (file downloads).
func (c *HTTPClient) GetRaw(ctx context.Context, path string, params url.Values) (*http.Response, error) {
	if err := c.EnsureAuthenticated(ctx); err != nil {
		return nil, err
	}
	u := c.url(path)
	if len(params) > 0 {
		u += "?" + params.Encode()
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodGet, u, nil)
	if err != nil {
		return nil, err
	}
	c.applyAuth(req)
	resp, err := c.client.Do(req)
	if err != nil {
		return nil, err
	}
	if resp.StatusCode >= 400 {
		defer resp.Body.Close()
		return nil, c.errorFromResponse(resp)
	}
	return resp, nil
}

// PostMultipart sends multipart/form-data (file uploads).
func (c *HTTPClient) PostMultipart(ctx context.Context, path string, request any) (*ApiResponse, error) {
	if err := c.EnsureAuthenticated(ctx); err != nil {
		return nil, err
	}
	var buf bytes.Buffer
	w := multipart.NewWriter(&buf)
	v := reflect.ValueOf(request)
	if v.Kind() == reflect.Ptr {
		v = v.Elem()
	}
	t := v.Type()
	for i := 0; i < v.NumField(); i++ {
		field := t.Field(i)
		tag := field.Tag.Get("json")
		name := strings.Split(tag, ",")[0]
		if name == "" || name == "-" {
			name = field.Name
		}
		fv := v.Field(i)
		if fv.IsNil() {
			continue
		}
		if fv.Kind() == reflect.Ptr && fv.Elem().Kind() == reflect.Interface {
			// skip
		}
		if r, ok := fv.Interface().(io.Reader); ok {
			part, err := w.CreateFormFile(name, "upload.bin")
			if err != nil {
				return nil, err
			}
			if _, err := io.Copy(part, r); err != nil {
				return nil, err
			}
			continue
		}
		if fv.Kind() == reflect.Ptr {
			fv = fv.Elem()
		}
		_ = w.WriteField(name, fmt.Sprint(fv.Interface()))
	}
	if err := w.Close(); err != nil {
		return nil, err
	}
	req, err := http.NewRequestWithContext(ctx, http.MethodPost, c.url(path), &buf)
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", w.FormDataContentType())
	c.applyAuth(req)
	return c.do(req)
}

func (c *HTTPClient) url(path string) string {
	return c.baseURL + strings.TrimPrefix(path, "/")
}

func (c *HTTPClient) applyAuth(req *http.Request) {
	if c.apiToken != "" {
		req.Header.Set("Authorization", "Bearer "+c.apiToken)
	}
}

func (c *HTTPClient) do(req *http.Request) (*ApiResponse, error) {
	resp, err := c.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()
	if resp.StatusCode >= 400 {
		return nil, c.errorFromResponse(resp)
	}
	var envelope ApiResponse
	if err := json.NewDecoder(resp.Body).Decode(&envelope); err != nil {
		return nil, err
	}
	if !envelope.Success {
		return nil, &APIError{
			StatusCode: envelope.Status,
			Message:    fmt.Sprintf("API returned success=false (status %d)", envelope.Status),
		}
	}
	return &envelope, nil
}

func (c *HTTPClient) errorFromResponse(resp *http.Response) error {
	body, _ := io.ReadAll(resp.Body)
	var errBody ErrorResponse
	_ = json.Unmarshal(body, &errBody)
	msg := errBody.Error
	if msg == "" {
		if s, ok := errBody.Message.(string); ok {
			msg = s
		}
	}
	if msg == "" {
		msg = resp.Status
	}
	return &APIError{StatusCode: resp.StatusCode, Message: msg, Body: &errBody}
}
