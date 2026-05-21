# @docmost/sdk

TypeScript/JavaScript client for the [Docmost](https://docmost.com) REST API — same surface as the [.NET](../c#/README.md) and [Python](../python/README.md) clients.

**npm:** `@docmost/sdk` · current release **1.0.0** (publish with `npm publish`)

## Installation

```bash
npm install @docmost/sdk
```

Requires **Node.js 18+**.

## Quick start

### API token (Bearer)

```typescript
import { DocmostClient, parseDataAs } from '@docmost/sdk';
import type { User } from '@docmost/sdk';

const client = new DocmostClient({
  baseUrl: 'https://docs.example.com',
  apiToken: 'your-api-key',
});

const me = await client.users.getUserInfo();
const user = parseDataAs<User>(me);
```

### Email and password (cookie session)

```typescript
import { DocmostClient } from '@docmost/sdk';
import { PaginationOptions } from '@docmost/sdk';

const client = await DocmostClient.create({
  baseUrl: 'https://docs.example.com',
  email: 'admin@example.com',
  password: 'secret',
});

const spaces = await client.spaces.getWorkspaceSpaces({ limit: 20 } as PaginationOptions);
```

### Shorthand constructor

```typescript
const client = new DocmostClient('https://docs.example.com', 'your-api-key');
```

## API surface

`DocmostClient` exposes grouped APIs (camelCase), matching OpenAPI tags:

| Property | Description |
|----------|-------------|
| `auth` | Login, logout, password reset, setup |
| `users` | Current user profile |
| `workspace` | Workspace settings, members, invites |
| `spaces` | Spaces and membership |
| `pages` | Pages, history, tree |
| `comments` | Page comments |
| `attachments` | Uploads and file downloads |
| `search` | Full-text search |
| `shares` | Public sharing |
| `groups` | User groups |
| `export` / `importApi` | Export and import |
| `health` / `version` | Health and version |
| `apiKeys`, `mfa`, `license`, `sso`, `ai`, `cloud` | Enterprise features |

Methods return `Promise<ApiResponse<unknown>>`. Use `parseDataAs<T>()` for typed `data`.

## Authentication

| Mode | Usage |
|------|--------|
| API token | `{ apiToken: '...' }` |
| Cookie session | `{ email, password }` + `await DocmostClient.create(...)` or `await client.login()` |

Do not pass both `apiToken` and `email`/`password`.

## Development

```bash
cd typescript
npm install
python3 scripts/generate_sdk.py   # from repo root: python3 typescript/scripts/generate_sdk.py
npm run build
```

## Publishing to npm

```bash
cd typescript
# bump version in package.json
npm run build
npm login
npm publish --access public
```

Scoped package `@docmost/sdk` requires `--access public` on first publish.

## License

MIT
