# postgres-client

Installs the PostgreSQL client package for a selected major version.

## Example

```yml
- hosts: app
  roles:
    - role: postgres-common

    - role: postgres-client
      postgres_version: 12
```

## Defaults

`postgres_version` defaults to `12`.
