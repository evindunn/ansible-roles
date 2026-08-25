# custom-facts

Collects OS-specific details into an Ansible local fact file.

## How It Works

The role initializes `collected_facts`, includes an OS-family task file, and writes the resulting JSON to `/etc/ansible/facts.d/custom.fact`.

When the fact file changes, it re-runs setup with the `local` gather subset so `ansible_local` reflects the new custom facts during the same play.
