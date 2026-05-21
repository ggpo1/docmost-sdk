<p align="center">
  <strong>Docmost SDK</strong><br/>
  Official-style client libraries for the <a href="https://docmost.com">Docmost</a> REST API
</p>

<p align="center">
  <a href="https://www.nuget.org/packages/Docmost.Sdk/"><img src="https://img.shields.io/nuget/v/Docmost.Sdk.svg?label=NuGet" alt="NuGet" /></a>
  <a href="https://www.nuget.org/packages/Docmost.Sdk/"><img src="https://img.shields.io/nuget/dt/Docmost.Sdk.svg?label=downloads" alt="Downloads" /></a>
</p>

<p align="center">
  <a href="https://github.com/docmost/docmost">Docmost</a> ·
  <a href="./api-1.json">OpenAPI spec</a> ·
  <a href="https://www.nuget.org/packages/Docmost.Sdk/">Docmost.Sdk on NuGet</a> ·
  Multi-language
</p>

---

## Overview

**docmost-sdk** is a monorepo of language-specific SDKs built from the same [OpenAPI 3.1 specification](./api-1.json). Each package wraps the Docmost API with idiomatic types, authentication, and error handling so you can automate wikis, spaces, pages, search, and workspace management from your stack of choice.

| Concern | Details |
|--------|---------|
| **Base URL** | `https://your-instance.example.com` (client adds `/api`) |
| **Auth** | API token (`Bearer`) or email/password (session cookie) |
| **Transport** | Mostly `POST` + JSON; cursor pagination on list endpoints |
| **Response** | `{ "data", "success", "status" }` unless noted (health, file downloads) |

---

## SDKs

| Language | Package | Status | Docs |
|----------|---------|--------|------|
| **C#** | [**Docmost.Sdk**](https://www.nuget.org/packages/Docmost.Sdk/) `1.0.0` | Published on [NuGet](https://www.nuget.org/packages/Docmost.Sdk/) | [README](./c#/README.md) |
| **Python** | `docmost` | Planned | — |
| **TypeScript** | `@docmost/sdk` | Planned | — |
| **Go** | `docmost` | Planned | — |

### C# — quick start

Install from NuGet:

```bash
dotnet add package Docmost.Sdk
```

Package page: **[nuget.org/packages/Docmost.Sdk](https://www.nuget.org/packages/Docmost.Sdk/)**

```csharp
using Docmost.Sdk;
using Docmost.Sdk.Json;
using Docmost.Sdk.Models;

// API token
await using var client = new DocmostClient("https://docs.example.com", apiToken: "your-api-key");

var me = await client.Users.GetUserInfoAsync();
var user = me.DeserializeData<User>();

// Email + password (cookie session)
await using var session = new DocmostClient(
    "https://docs.example.com",
    email: "admin@example.com",
    password: "secret");

var spaces = await session.Spaces.GetWorkspaceSpacesAsync(new PaginationOptions { Limit = 20 });
```

Full guide: **[c#/README.md](./c#/README.md)**

### Python — coming soon

```bash
# pip install docmost   (planned)
```

### TypeScript — coming soon

```bash
# npm install @docmost/sdk   (planned)
```

---

## Authentication

All SDKs support the same two modes:

### 1. API token (recommended for automation)

Pass your API key as a Bearer token. Create keys in Docmost (Enterprise: **API Keys** endpoints).

```
Authorization: Bearer <api_token>
```

### 2. Email and password (interactive / scripts)

Log in via `POST /api/auth/login`. The server sets a session cookie; subsequent requests reuse it until logout.

| SDK | API token | Cookie session |
|-----|-----------|----------------|
| C# | `new DocmostClient(url, apiToken: "...")` | `new DocmostClient(url, email, password)` |

Do not mix token and password credentials in a single client instance.

---

## API coverage

Generated and hand-maintained clients expose the OpenAPI **tags** as grouped APIs:

| Area | Examples |
|------|----------|
| **Auth** | Login, logout, password reset, setup |
| **Users** | Profile (`/users/me`) |
| **Workspace** | Settings, members, invitations |
| **Spaces** | CRUD, membership |
| **Pages** | CRUD, history, tree, trash |
| **Comments** | Page comments |
| **Attachments** | Upload, download |
| **Search** | Full-text search, suggestions |
| **Shares** | Public page sharing |
| **Groups** | User groups |
| **Export / Import** | HTML/Markdown, ZIP |
| **Health / Version** | Liveness, server version |
| **Enterprise** | API keys, MFA, license, SSO, AI, cloud |

See [api-1.json](./api-1.json) for the full operation list and schemas.

---

## Repository layout

```
docmost-sdk/
├── api-1.json          # OpenAPI 3.1 — source of truth
├── README.md           # this file
├── c#/                 # C# / .NET — published as Docmost.Sdk
│   ├── Docmost.Sdk.sln
│   ├── README.md
│   ├── scripts/        # codegen from OpenAPI
│   └── src/Docmost.Sdk/
├── python/             # (planned)
├── typescript/         # (planned)
└── context/            # dev notes
```

---

## Regenerating clients

After updating `api-1.json`:

| Language | Command |
|----------|---------|
| **C#** | `python3 c#/scripts/generate_sdk.py` then `dotnet build c#/Docmost.Sdk.sln` |

Bump `Version` in `c#/src/Docmost.Sdk/Docmost.Sdk.csproj` before publishing a new release to NuGet.

---

## Requirements

- A running [Docmost](https://docmost.com) instance (self-hosted or cloud)
- .NET 8+ for [Docmost.Sdk](https://www.nuget.org/packages/Docmost.Sdk/)
- Network access to your instance’s `/api` routes

---

## Contributing

1. Keep changes aligned with `api-1.json`.
2. Prefer shared auth and response semantics across languages.
3. Add or update the language-specific `README.md` when shipping a new SDK.

---

## License

MIT — see [Docmost.Sdk on NuGet](https://www.nuget.org/packages/Docmost.Sdk/) for package details.

---

<p align="center">
  <sub>Built for teams running <a href="https://docmost.com">Docmost</a> — collaborative wiki, self-hosted, full data control.</sub>
</p>
