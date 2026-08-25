# consul

Installs Consul, optional consul-template, server service overrides, firewalld service definitions, and Envoy.

## Example

```yml
- hosts: consul_servers
  roles:
    - role: hashicorp_repo

    - role: consul
      consul_server: true
```

## Defaults

`consul_server` defaults to `false`. Version variables live in `vars/main.yml`.
