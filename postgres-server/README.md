# postgres-server

Installs the PostgreSQL server package for a selected major version.

## Example

```yml
- hosts: database
  roles:
    - role: postgres-common

    - role: postgres-server
      postgres_version: 14
```

## Defaults

`postgres_version` defaults to `14`.
