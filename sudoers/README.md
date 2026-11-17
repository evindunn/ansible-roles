# sudoers

Creates local users and grants them passwordless sudo for all commands.

## Example

Run this role with an existing privileged account, before
[authorized_keys](../authorized_keys/README.md) when creating SSH users:

```yml
---
- hosts: servers
  become: true
  roles:
    - role: sudoers
      sudoers:
        - deploy
        - evin

    - role: authorized_keys
```

## Configuration

`sudoers` defaults to an empty list of usernames. Duplicate names are removed.
The role installs sudo, ensures the listed users and their home directories
exist, and writes `/etc/sudoers.d/99-ansible-users` with mode `0440`.
It validates the file with `visudo -cf` before saving it.

The system's main sudoers configuration must include `/etc/sudoers.d`, as
standard Debian, Ubuntu, and Red Hat installations do.

Removing a name removes its grant from this role's file on the next run.
It does not delete the user or remove sudo privileges granted elsewhere.
An empty list clears all grants managed by this role. The role does not
configure passwords or SSH keys.
