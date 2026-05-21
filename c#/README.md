# Docmost.Sdk

.NET client library for the [Docmost](https://docmost.com) REST API.

## Installation

```bash
dotnet add package Docmost.Sdk
```

Or reference the project locally:

```bash
dotnet add reference path/to/Docmost.Sdk.csproj
```

## Quick start

### API token (Bearer)

```csharp
using Docmost.Sdk;

await using var client = new DocmostClient("https://docs.example.com", apiToken: "your-api-key");

using Docmost.Sdk.Json;
using Docmost.Sdk.Models;

var me = await client.Users.GetUserInfoAsync();
var profile = me.DeserializeData<User>(); // typed via ApiResponseExtensions
```

### Email and password (cookie session)

```csharp
await using var client = new DocmostClient(
    "https://docs.example.com",
    email: "admin@example.com",
    password: "secret");

var spaces = await client.Spaces.GetWorkspaceSpacesAsync(
    new PaginationOptions { Limit = 20 });
```

### Advanced configuration

```csharp
using Docmost.Sdk;

var client = new DocmostClient(new DocmostClientOptions
{
    BaseUrl = new Uri("https://docs.example.com"),
    ApiToken = Environment.GetEnvironmentVariable("DOCMOST_API_TOKEN"),
    Timeout = TimeSpan.FromSeconds(60),
    LoginOnStartup = false,
});

await client.LoginAsync(); // when using email/password
```

## API surface

`DocmostClient` exposes grouped clients matching the OpenAPI tags:

| Property | Description |
|----------|-------------|
| `Auth` | Login, logout, password reset, setup |
| `Users` | Current user profile |
| `Workspace` | Workspace settings, members, invites |
| `Spaces` | Spaces and membership |
| `Pages` | Pages, history, tree |
| `Comments` | Page comments |
| `Attachments` | Uploads and file downloads |
| `Search` | Full-text search |
| `Shares` | Public sharing |
| `Groups` | User groups |
| `Export` / `Import` | Export and import |
| `Health` / `Version` | Health and version |
| `ApiKeys`, `Mfa`, `License`, `Sso`, `Ai`, `Cloud` | Enterprise features |

All POST endpoints return `ApiResponse<JsonElement?>`. Use `System.Text.Json` to map `Data` to strongly typed models from `Docmost.Sdk.Models`.

## Building & publishing to NuGet

```bash
cd c#
dotnet pack src/Docmost.Sdk/Docmost.Sdk.csproj -c Release
dotnet nuget push src/Docmost.Sdk/bin/Release/Docmost.Sdk.1.0.0.nupkg --api-key <key> --source https://api.nuget.org/v3/index.json
```

## License

MIT
