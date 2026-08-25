# vim

Installs Vim and deploys a global vimrc.

## Example

```yml
- hosts: servers
  roles:
    - role: vim
      pkgs:
        - vim
```

## Defaults

`pkgs` defaults to `vim`.
