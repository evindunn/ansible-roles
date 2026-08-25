# authorized_keys

Manages SSH authorized keys and optionally disables password authentication.

## How It Works

The role loops over `authorized_keys` and applies each entry with `ansible.posix.authorized_key` when both `user` and `key` are set. Each entry may also set `state`, which defaults to `present`.

It updates `PasswordAuthentication` in `/etc/ssh/sshd_config` from `disable_ssh_passwords` and notifies the SSH daemon reload handler when that setting changes.

## Defaults

`authorized_keys` defaults to an empty list. `disable_ssh_passwords` defaults to `False`.
