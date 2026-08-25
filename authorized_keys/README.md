# authorized_keys

Manages SSH authorized keys and optionally disables password authentication.

## Example

```yml
- hosts: servers
  roles:
    - role: authorized_keys
      disable_ssh_passwords: true
      authorized_keys:
        - user: deploy
          key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA..."
```

## Defaults

`authorized_keys` defaults to an empty list. `disable_ssh_passwords` defaults to `False`.
