# consul

Installs Consul, optional consul-template, server service overrides, firewalld service definitions, and Envoy.

## How It Works

The role installs the pinned Consul package and can install `consul-template` from HashiCorp releases. When `consul_server` is true, it prepares `/var/lib/consul` and writes a systemd service override.

If firewalld is available, the role copies Consul agent and server service definitions into `/etc/firewalld/services` and reloads firewalld when they change. It also imports the Envoy installation task file under the `envoy` tag.

## Defaults

`consul_server` defaults to `false`. Version variables live in `vars/main.yml`.
