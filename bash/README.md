# bash

Adds global Bash defaults to `/etc/bash.bashrc`.

## Example

```yml
- hosts: servers
  roles:
    - role: bash
      bash_opts:
        - "alias ls='ls -h'"
        - "alias ll='ls -l'"
        - "set -o vi"
```

## Defaults

`bash_opts` defines `ls` and `ll` aliases.
