# Docmost.Sdk

[![NuGet](https://img.shields.io/nuget/v/Docmost.Sdk.svg)](https://www.nuget.org/packages/Docmost.Sdk/)
[![NuGet downloads](https://img.shields.io/nuget/dt/Docmost.Sdk.svg)](https://www.nuget.org/packages/Docmost.Sdk/)
[![.NET](https://img.shields.io/badge/.NET-8.0-512BD4)](https://www.nuget.org/packages/Docmost.Sdk/)

.NET client library for the [Docmost](https://docmost.com) REST API.

**NuGet:** [Docmost.Sdk](https://www.nuget.org/packages/Docmost.Sdk/) · current release **1.0.0**

## Installation

From [NuGet](https://www.nuget.org/packages/Docmost.Sdk/):

```bash
dotnet add package Docmost.Sdk
```

Or in `.csproj`:

```xml
<PackageReference Include="Docmost.Sdk" Version="1.0.0" />
```

### Local development

Reference the project from this repository:

```bash
dotnet add reference path/to/c#/src/Docmost.Sdk/Docmost.Sdk.csproj
```

Requires **.NET 8** or later.

## Quick start

### API token (Bearer)

```csharp
using Docmost.Sdk;
using Docmost.Sdk.Json;
using Docmost.Sdk.Models;

await using var client = new DocmostClient("https://docs.example.com", apiToken: "your-api-key");

var me = await client.Users.GetUserInfoAsync();
var profile = me.DeserializeData<User>();
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

POST endpoints return `ApiResponse<JsonElement?>`. Map `Data` to models from `Docmost.Sdk.Models` via `ApiResponseExtensions.DeserializeData<T>()`.

## Source & spec

- Monorepo: [docmost-sdk](../)
- OpenAPI: [api-1.json](../api-1.json)
- Regenerate models/services: `python3 scripts/generate_sdk.py` (from repo root: `python3 c#/scripts/generate_sdk.py`)

## Releasing a new version

For maintainers after changes are ready:

```bash
cd c#
# bump <Version> in src/Docmost.Sdk/Docmost.Sdk.csproj
dotnet pack src/Docmost.Sdk/Docmost.Sdk.csproj -c Release -o ./artifacts
dotnet nuget push artifacts/Docmost.Sdk.*.nupkg \
  --api-key <KEY> \
  --source https://api.nuget.org/v3/index.json
```

## License

MIT
