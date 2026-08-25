# postgres-common

Adds the upstream PostgreSQL apt repository and signing key.

## How It Works

The role installs `gnupg2`, imports the PostgreSQL signing key into `postgres_gpg_keyring`, and adds the PostgreSQL Global Development Group apt repository for the host distribution release.

Use this role before PostgreSQL client or server roles when you need versions from the upstream repository.

## Defaults

`postgres_gpg_keyring` defaults to `/etc/apt/trusted.gpg.d/postgres.gpg`.
