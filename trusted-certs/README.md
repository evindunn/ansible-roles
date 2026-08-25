# trusted-certs

Installs additional trusted certificate authorities and refreshes the system trust store.

## How It Works

The role loads OS-family variables, ensures `ca-certificates` is installed, and copies each file listed in `trusted_certs` into the platform certificate directory.

When any certificate changes, it runs the OS-specific certificate update command.

## Defaults

`trusted_certs` defaults to an empty list.
