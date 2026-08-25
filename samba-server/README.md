# samba-server

Installs and starts Samba, with an optional Samba exporter on amd64 hosts.

## How It Works

The role installs `samba` and `gnupg2`, starts and enables the `smbd` service, and checks the custom fact `ansible_local.custom.dpkg_architecture`.

When that architecture is `amd64`, it includes `samba-exporter.yml` to configure the exporter repository and package.

## Defaults

Exporter repository key settings live in `vars/main.yml`.
