# locale

Installs locale support and configures the system locale and keyboard layout.

## How It Works

The role loads OS-family variables, installs the locale package, enables `locale` in the platform locale-generation file, and runs the configured generation command when that file changes.

It writes the system language file for Debian or RedHat and sets the keyboard layout in `/etc/default/keyboard` or `/etc/vconsole.conf`, notifying the reboot handler when those settings change.

## Defaults

`locale` defaults to `en_US.UTF-8`. `keyboard_layout` defaults to `us`.
