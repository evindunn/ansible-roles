# hashicorp_repo

Adds the HashiCorp package repository for the target operating system.

## How It Works

The role loads variables based on `ansible_facts['os_family']` and then includes the matching OS-specific task file.

Use this role before installing HashiCorp packages such as Consul or Vault from official repositories.
