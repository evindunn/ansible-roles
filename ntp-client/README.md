# ntp-client

Configures OS-specific time synchronization and the system timezone.

## How It Works

The role loads OS-family variables and task files, then starts and enables the configured time synchronization service.

It reads the current timezone with `timedatectl` and runs `timedatectl set-timezone` when it differs from `timezone`.

## Defaults

`timezone` defaults to `America/New_York`. `ntp_server` defaults to `pool.ntp.org`.
