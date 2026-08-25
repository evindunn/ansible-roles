# node_exporter

Installs Prometheus node_exporter from GitHub releases and manages its systemd service.

## How It Works

The role detects the Debian package architecture, creates `node_exporter_directory`, and unarchives the selected node_exporter release into that directory.

It creates a system user, templates `/etc/systemd/system/node-exporter.service`, reloads systemd through the handler, and enables the `node-exporter` service.

## Defaults

`node_exporter_version` defaults to `1.3.1`. `node_exporter_listen_addr` defaults to `0.0.0.0:9100`.
