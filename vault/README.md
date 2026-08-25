# vault

Installs Vault and configures either a server service or an AppRole-backed Vault Agent.

## Example

```yml
- hosts: vault_agents
  roles:
    - role: hashicorp_repo

    - role: vault
      vault_server: false
      vault_addr: https://vault.example.com:8200
      vault_approle_id: "{{ vault_agent_role_id }}"
```

## Defaults

`vault_addr` defaults to `https://127.0.0.1:8200`. `vault_server` defaults to `false`; `vault_approle_id` defaults to an empty string.
