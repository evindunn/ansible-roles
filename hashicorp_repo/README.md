# hashicorp_repo

Adds the HashiCorp package repository for the target operating system.

## Example

```yml
- hosts: servers
  roles:
    - role: hashicorp_repo
    - role: vault
```
