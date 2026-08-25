# postgres-common

Adds the upstream PostgreSQL apt repository and signing key.

## Example

```yml
- hosts: postgres_hosts
  roles:
    - role: postgres-common
      postgres_gpg_keyring: /etc/apt/trusted.gpg.d/postgres.gpg
```

## Defaults

`postgres_gpg_keyring` defaults to `/etc/apt/trusted.gpg.d/postgres.gpg`.
