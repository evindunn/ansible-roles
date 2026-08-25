# unattended-upgrades

Configures unattended package updates for Debian and RedHat families.

## How It Works

The role includes the OS-family task file. Debian tasks install and configure `unattended-upgrades`; RedHat tasks configure `dnf-automatic`.

Use `upgrade_exclude_packages` to omit packages from automated upgrades where the OS-specific templates support it.

## Defaults

`upgrade_exclude_packages` defaults to an empty list.
