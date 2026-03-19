# kb-cloud-client-python

[![PyPI version](https://img.shields.io/pypi/v/kb-cloud-client.svg)](https://pypi.org/project/kb-cloud-client/)
[![Python versions](https://img.shields.io/pypi/pyversions/kb-cloud-client.svg)](https://pypi.org/project/kb-cloud-client/)
[![CI](https://github.com/apecloud/kb-cloud-client-python/actions/workflows/ci.yaml/badge.svg)](https://github.com/apecloud/kb-cloud-client-python/actions/workflows/ci.yaml)
[![Docs](https://github.com/apecloud/kb-cloud-client-python/actions/workflows/docs.yaml/badge.svg)](https://apecloud.github.io/kb-cloud-client-python/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Python client for the [KubeBlocks Cloud](https://www.apecloud.com/) API.

## Overview

KubeBlocks Cloud exposes two API surfaces, each backed by its own control-plane console:

| Console | Audience | Python package | Go equivalent |
|---------|----------|----------------|---------------|
| **User Portal** | Regular organization users | `kb_cloud_client.kbcloud` | `api/kbcloud` |
| **Admin Portal** | Platform administrators | `kb_cloud_client.kbcloud.admin` | `api/kbcloud/admin` |

This mirrors the package structure of the [Go client](https://github.com/apecloud/kb-cloud-client-go).

## Requirements

- Python 3.10+
- `requests`, `python-dateutil`, `urllib3`

## Installation

```bash
pip install kb-cloud-client
```

Or install from source:

```bash
pip install -e .
```

## Package Layout

```
kb_cloud_client/
├── kbcloud/            ← User portal API (openapi.yaml)
│   ├── api/            ← ClusterApi, OrganizationApi, …
│   ├── model/          ← Cluster, ClusterCreate, …
│   └── admin/          ← Admin portal API (adminapi.yaml)
│       ├── api/        ← EnvironmentApi, UserApi, …
│       └── model/      ← Environment, OrgCreate, …
├── api_client.py       ← HTTP transport (requests + Digest auth)
├── configuration.py    ← Host, credentials, retry settings
└── exceptions.py       ← ApiException hierarchy
```

## Authentication

The API uses **HTTP Digest authentication** with an API key name and secret.

### Recommended: environment variables

```bash
export KB_CLOUD_API_KEY_NAME="your-key-name"
export KB_CLOUD_API_KEY_SECRET="your-key-secret"
export KB_CLOUD_SITE="https://api.apecloud.com"   # optional
```

```python
from kb_cloud_client import ApiClient, Configuration

configuration = Configuration()        # reads env vars automatically
with ApiClient(configuration) as client:
    ...
```

### Explicit configuration

```python
from kb_cloud_client import ApiClient, Configuration

configuration = Configuration(
    api_key_name="your-key-name",
    api_key_secret="your-key-secret",
    host="https://api.apecloud.com",
)
```

## Quick Start

### User Portal

```python
import os
from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud import ClusterApi

with ApiClient(Configuration()) as client:
    api = ClusterApi(client)
    clusters = api.list_cluster(org_name=os.environ["KB_CLOUD_ORG"])
    for c in clusters.items:
        print(c.name, c.status)
```

### Admin Portal

```python
import os
from kb_cloud_client import ApiClient, Configuration
from kb_cloud_client.kbcloud.admin import EnvironmentApi

with ApiClient(Configuration()) as client:
    api = EnvironmentApi(client)
    envs = api.list_environment()
    for e in envs.items:
        print(e.name, e.status)
```

## Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `KB_CLOUD_API_KEY_NAME` | API key name | — |
| `KB_CLOUD_API_KEY_SECRET` | API key secret | — |
| `KB_CLOUD_SITE` | API base URL | `https://api.apecloud.com` |
| `HTTP_PROXY` / `HTTPS_PROXY` | HTTP proxy | — |

### Configuration Parameters

```python
from kb_cloud_client import Configuration

cfg = Configuration(
    host="https://api.apecloud.com",
    api_key_name="...",
    api_key_secret="...",
    verify_ssl=True,          # set False to skip TLS verification (not recommended)
    debug=False,              # enable request/response logging
    retry_config={
        "total": 3,
        "backoff_factor": 0.5,
    },
)
```

## Examples

All examples live under `examples/`:

```
examples/
├── user/                   ← User portal examples
│   ├── list_clusters.py
│   ├── create_cluster.py
│   └── list_organizations.py
└── admin/                  ← Admin portal examples
    ├── list_organizations.py
    ├── list_environments.py
    ├── list_clusters.py
    ├── list_engines.py
    ├── get_current_user.py
    └── manage_organization.py
```

Run any example after exporting your credentials:

```bash
export KB_CLOUD_API_KEY_NAME=...
export KB_CLOUD_API_KEY_SECRET=...
export KB_CLOUD_SITE=https://api.apecloud.com

python examples/user/list_clusters.py
python examples/admin/list_environments.py
```

## Development

### Regenerate the client

The client code under `src/kb_cloud_client/kbcloud/` is fully generated from OpenAPI
specifications in `.generator/schemas/`. To regenerate:

```bash
./generate.sh
```

The generator reads `openapi.yaml` (user portal) and `adminapi.yaml` (admin portal), and
outputs to:

- `src/kb_cloud_client/kbcloud/`  — user portal
- `src/kb_cloud_client/kbcloud/admin/`  — admin portal (nested, mirrors Go `api/kbcloud/admin`)

### Project structure

```
.
├── .generator/             ← Code generator (Jinja2 templates + Python)
│   ├── schemas/            ← openapi.yaml, adminapi.yaml
│   └── src/generator/      ← Generator source
├── src/
│   └── kb_cloud_client/    ← Generated + hand-written runtime
│       ├── kbcloud/        ← User portal
│       │   └── admin/      ← Admin portal (nested)
│       ├── api_client.py
│       ├── configuration.py
│       └── exceptions.py
├── examples/
│   ├── user/
│   └── admin/
├── generate.sh
└── setup.cfg
```

## Acknowledgments

This project is inspired by the [DataDog Python API client](https://github.com/DataDog/datadog-api-client-python) (Apache 2.0).

## License

Apache-2.0 — see [LICENSE](LICENSE).
