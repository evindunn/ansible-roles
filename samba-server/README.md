# samba-server

Installs and starts Samba, with an optional Samba exporter on amd64 hosts.

## Example

```yml
- hosts: file_servers
  roles:
    - role: custom-facts

    - role: samba-server
```

## Defaults

Exporter repository key settings live in `vars/main.yml`.
