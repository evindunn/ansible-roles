# vault

Installs Vault and configures either a server service or an AppRole-backed Vault Agent.

## How It Works

The role installs the `vault` package. When `vault_server` is true, it writes a profile script that points `VAULT_ADDR` at the local HTTPS listener and starts/enables the Vault service.

When `vault_server` is false and `vault_approle_id` is set, it prepares `/run/vault`, removes extra Vault config files, writes the AppRole ID, templates `agent.hcl`, installs a `vault-agent` systemd unit, and points shells at the agent Unix socket.

## Defaults

`vault_addr` defaults to `https://127.0.0.1:8200`. `vault_server` defaults to `false`; `vault_approle_id` defaults to an empty string.
