# firewalld

Installs firewalld and manages zone XML from Ansible variables.

## How It Works

The role installs and starts firewalld, discovers the current default zone and runtime zones, and merges any runtime zones into `firewalld_zones` before rendering zone XML files.

It templates each configured zone into `/etc/firewalld/zones` and sets `firewalld_default_zone` when it differs from the current default, notifying the reload handler for changes.

## Defaults

`firewalld_default_zone` defaults to `public`. The default public zone drops traffic except SSH.
