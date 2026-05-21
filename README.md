<p align="center">
  <strong>Docmost SDK</strong><br/>
  Official-style client libraries for the <a href="https://docmost.com">Docmost</a> REST API
</p>

<p align="center">
  <a href="https://www.nuget.org/packages/Docmost.Sdk/"><img src="https://img.shields.io/nuget/v/Docmost.Sdk.svg?label=NuGet" alt="NuGet" /></a>
  <a href="https://www.nuget.org/packages/Docmost.Sdk/"><img src="https://img.shields.io/nuget/dt/Docmost.Sdk.svg?label=NuGet%20downloads" alt="NuGet downloads" /></a>
  <a href="https://pypi.org/project/docmost-sdk/"><img src="https://img.shields.io/pypi/v/docmost-sdk.svg?label=PyPI" alt="PyPI" /></a>
  <a href="https://pypi.org/project/docmost-sdk/"><img src="https://img.shields.io/pypi/dm/docmost-sdk.svg?label=PyPI%20downloads" alt="PyPI downloads" /></a>
  <a href="https://www.npmjs.com/package/docmost-sdk"><img src="https://img.shields.io/npm/v/docmost-sdk.svg?label=npm" alt="npm" /></a>
  <a href="https://www.npmjs.com/package/docmost-sdk"><img src="https://img.shields.io/npm/dm/docmost-sdk.svg?label=npm%20downloads" alt="npm downloads" /></a>
</p>

<p align="center">
  <a href="https://github.com/docmost/docmost">Docmost</a> ·
  <a href="./api-1.json">OpenAPI spec</a> ·
  <a href="https://www.nuget.org/packages/Docmost.Sdk/">Docmost.Sdk</a> ·
  <a href="https://pypi.org/project/docmost-sdk/">docmost-sdk (PyPI)</a> ·
  <a href="https://www.npmjs.com/package/docmost-sdk">docmost-sdk (npm)</a>
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
| **Python** | [**docmost-sdk**](https://pypi.org/project/docmost-sdk/) `1.0.0` | Published on [PyPI](https://pypi.org/project/docmost-sdk/) | [README](./python/README.md) |
| **TypeScript** | [**docmost-sdk**](https://www.npmjs.com/package/docmost-sdk) `1.0.0` | Published on [npm](https://www.npmjs.com/package/docmost-sdk) | [README](./typescript/README.md) |
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

### Python — quick start

Install from PyPI:

```bash
pip install docmost-sdk
```

Package page: **[pypi.org/project/docmost-sdk](https://pypi.org/project/docmost-sdk/)**

```python
from docmost import DocmostClient
from docmost.models import PaginationOptions, User
from docmost.response import parse_data

with DocmostClient("https://docs.example.com", api_token="your-api-key") as client:
    me = client.users.get_user_info()
    user = parse_data(me, User)

with DocmostClient(
    "https://docs.example.com",
    email="admin@example.com",
    password="secret",
) as session:
    spaces = session.spaces.get_workspace_spaces(PaginationOptions(limit=20))
```

Full guide: **[python/README.md](./python/README.md)**

### TypeScript — quick start

Install from npm:

```bash
npm install docmost-sdk
```

Package page: **[npmjs.com/package/docmost-sdk](https://www.npmjs.com/package/docmost-sdk)**

```typescript
import { DocmostClient, parseDataAs } from 'docmost-sdk';
import type { User } from 'docmost-sdk';

const client = new DocmostClient({
  baseUrl: 'https://docs.example.com',
  apiToken: 'your-api-key',
});

const me = await client.users.getUserInfo();
const user = parseDataAs<User>(me);

const session = await DocmostClient.create({
  baseUrl: 'https://docs.example.com',
  email: 'admin@example.com',
  password: 'secret',
});
```

Full guide: **[typescript/README.md](./typescript/README.md)**

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
| Python | `DocmostClient(url, api_token="...")` | `DocmostClient(url, email="...", password="...")` |
| TypeScript | `new DocmostClient({ apiToken })` | `DocmostClient.create({ email, password })` |

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
├── c#/                 # C# / .NET — Docmost.Sdk on NuGet
│   ├── Docmost.Sdk.sln
│   ├── README.md
│   ├── scripts/        # codegen from OpenAPI
│   └── src/Docmost.Sdk/
├── python/             # docmost-sdk on PyPI
├── typescript/         # docmost-sdk on npm
└── context/            # dev notes
```

---

## Regenerating clients

After updating `api-1.json`:

| Language | Command |
|----------|---------|
| **C#** | `python3 c#/scripts/generate_sdk.py` then `dotnet build c#/Docmost.Sdk.sln` |
| **Python** | `python3 python/scripts/generate_sdk.py` |
| **TypeScript** | `python3 typescript/scripts/generate_sdk.py` then `npm run build` in `typescript/` |

Before a new release, bump versions in each package manifest (`Docmost.Sdk.csproj`, `python/pyproject.toml`, `typescript/package.json`).

---

## Requirements

- A running [Docmost](https://docmost.com) instance (self-hosted or cloud)
- .NET 8+ for [Docmost.Sdk](https://www.nuget.org/packages/Docmost.Sdk/)
- Python 3.10+ for [docmost-sdk on PyPI](https://pypi.org/project/docmost-sdk/)
- Node.js 18+ for [docmost-sdk on npm](https://www.npmjs.com/package/docmost-sdk)
- Network access to your instance’s `/api` routes

---

## Contributing

1. Keep changes aligned with `api-1.json`.
2. Prefer shared auth and response semantics across languages.
3. Add or update the language-specific `README.md` when shipping a new SDK.

---

## License

MIT — see [Docmost.Sdk on NuGet](https://www.nuget.org/packages/Docmost.Sdk/), [docmost-sdk on PyPI](https://pypi.org/project/docmost-sdk/), and [docmost-sdk on npm](https://www.npmjs.com/package/docmost-sdk).

---

<p align="center">
  <sub>Built for teams running <a href="https://docmost.com">Docmost</a> — collaborative wiki, self-hosted, full data control.</sub>
</p>
