# postgres-server

Installs the PostgreSQL server package for a selected major version.

## How It Works

The role installs `postgresql-{{ postgres_version }}` with the system package manager.

Use `postgres-common` first when the host needs the upstream PostgreSQL repository configured.

## Defaults

`postgres_version` defaults to `14`.
