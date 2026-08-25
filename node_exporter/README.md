# node_exporter

Installs Prometheus node_exporter from GitHub releases and manages its systemd service.

## Example

```yml
- hosts: servers
  roles:
    - role: node_exporter
      node_exporter_version: 1.3.1
      node_exporter_listen_addr: "0.0.0.0:9100"
```

## Defaults

`node_exporter_version` defaults to `1.3.1`. `node_exporter_listen_addr` defaults to `0.0.0.0:9100`.
