# docmost-sdk (Go)

Go client for the [Docmost](https://docmost.com) REST API — aligned with the [.NET](../c#/README.md), [Python](../python/README.md), and [TypeScript](../typescript/README.md) SDKs.

**Module:** `github.com/ggpo1/docmost-sdk/go`

## Installation

```bash
go get github.com/ggpo1/docmost-sdk/go/docmost
```

Requires **Go 1.21+**.

## Quick start

### API token (Bearer)

```go
package main

import (
	"context"
	"fmt"
	"log"

	"github.com/ggpo1/docmost-sdk/go/docmost"
	"github.com/ggpo1/docmost-sdk/go/docmost/models"
)

func main() {
	client, err := docmost.NewClientWithToken("https://docs.example.com", "your-api-key")
	if err != nil {
		log.Fatal(err)
	}

	ctx := context.Background()
	me, err := client.Users.GetUserInfo(ctx)
	if err != nil {
		log.Fatal(err)
	}

	var user models.User
	if err := me.ParseData(&user); err != nil {
		log.Fatal(err)
	}
	fmt.Println(user.Email)
}
```

### Email and password (cookie session)

```go
client, err := docmost.NewClientWithCredentials(
	"https://docs.example.com",
	"admin@example.com",
	"secret",
)
if err != nil {
	log.Fatal(err)
}

limit := 20
spaces, err := client.Spaces.GetWorkspaceSpaces(ctx, &models.PaginationOptions{
	Limit: &limit,
})
```

### Options

```go
client, err := docmost.NewClient("https://docs.example.com", docmost.ClientOptions{
	APIToken:       os.Getenv("DOCMOST_API_TOKEN"),
	LoginOnStartup: false,
	Timeout:        60,
})
```

## API surface

`DocmostClient` exposes grouped APIs matching OpenAPI tags:

| Field | Description |
|-------|-------------|
| `Auth` | Login, logout, password reset, setup |
| `Users` | Current user profile |
| `Workspace` | Workspace settings, members, invites |
| `Spaces` | Spaces and membership |
| `Pages` | Pages, history, tree |
| `Comments` | Page comments |
| `Attachments` | Uploads and downloads |
| `Search` | Full-text search |
| `Shares` | Public sharing |
| `Groups` | User groups |
| `Export` / `Import` | Export and import |
| `Health` / `Version` | Health and version |
| `APIKeys`, `MFA`, `License`, `SSO`, `AI`, `Cloud` | Enterprise features |

Methods return `*docmost.ApiResponse` with `json.RawMessage` data. Use `ParseData(&model)` for typed structs from `docmost/models`.

## Authentication

| Mode | Constructor |
|------|-------------|
| API token | `NewClientWithToken(url, token)` or `ClientOptions{APIToken: "..."}` |
| Cookie session | `NewClientWithCredentials(url, email, password)` |

Do not set both `APIToken` and `Email`/`Password`.

## Regenerate from OpenAPI

```bash
python3 scripts/generate_sdk.py
# from repo root: python3 go/scripts/generate_sdk.py
go build ./...
```

## Publishing

Tag a release on GitHub; Go modules are resolved via `go get` and [pkg.go.dev](https://pkg.go.dev) from your module path.

## License

MIT
