# docmost-sdk

[![PyPI](https://img.shields.io/pypi/v/docmost-sdk.svg)](https://pypi.org/project/docmost-sdk/)
[![PyPI downloads](https://img.shields.io/pypi/dm/docmost-sdk.svg)](https://pypi.org/project/docmost-sdk/)
[![Python](https://img.shields.io/pypi/pyversions/docmost-sdk.svg)](https://pypi.org/project/docmost-sdk/)

Python client for the [Docmost](https://docmost.com) REST API — same surface as the [.NET client](../c#/README.md).

**PyPI:** [docmost-sdk](https://pypi.org/project/docmost-sdk/) · current release **1.0.0**

Import name: `docmost` (package on PyPI: `docmost-sdk`).

## Installation

From [PyPI](https://pypi.org/project/docmost-sdk/):

```bash
pip install docmost-sdk
```

Requires **Python 3.10+**.

In `requirements.txt` or `pyproject.toml`:

```text
docmost-sdk==1.0.0
```

### Local development

```bash
cd python
pip install .
```

## Quick start

### API token (Bearer)

```python
from docmost import DocmostClient
from docmost.models import PaginationOptions, User
from docmost.response import parse_data

with DocmostClient("https://docs.example.com", api_token="your-api-key") as client:
    me = client.users.get_user_info()
    user = parse_data(me, User)
    print(user.email if user else None)
```

### Email and password (cookie session)

```python
with DocmostClient(
    "https://docs.example.com",
    email="admin@example.com",
    password="secret",
) as client:
    spaces = client.spaces.get_workspace_spaces(PaginationOptions(limit=20))
```

### Advanced options

```python
import os

with DocmostClient(
    "https://docs.example.com",
    api_token=os.environ["DOCMOST_API_TOKEN"],
    login_on_startup=False,
    timeout=60.0,
) as client:
    ...
```

## API surface

`DocmostClient` exposes grouped APIs (snake_case), matching OpenAPI tags:

| Attribute | Description |
|-----------|-------------|
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
| `export` / `import_` | Export and import (`import_` — reserved keyword) |
| `health` / `version` | Health and version |
| `api_keys`, `mfa`, `license`, `sso`, `ai`, `cloud` | Enterprise features |

Methods return `ApiResponse` with a `data` field (usually `dict`). Use `parse_data(response, Model)` for typed Pydantic models from `docmost.models`.

## Authentication

| Mode | Constructor |
|------|-------------|
| API token | `DocmostClient(url, api_token="...")` |
| Cookie session | `DocmostClient(url, email="...", password="...")` |

Do not pass both `api_token` and `email`/`password`.

## Source & spec

- Monorepo: [docmost-sdk](../)
- OpenAPI: [api-1.json](../api-1.json)
- Regenerate models/services: `python3 scripts/generate_sdk.py` (from repo root: `python3 python/scripts/generate_sdk.py`)

## Releasing a new version

For maintainers after changes are ready:

```bash
cd python
# bump version in pyproject.toml and docmost/__init__.py
python3 -m pip install build twine
python3 -m build
twine upload dist/*
```

Use a PyPI API token (`__token__` as username). Each version can be uploaded only once.

## License

MIT
