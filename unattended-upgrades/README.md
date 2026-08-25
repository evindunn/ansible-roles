# unattended-upgrades

Configures unattended package updates for Debian and RedHat families.

## Example

```yml
- hosts: servers
  roles:
    - role: unattended-upgrades
      upgrade_exclude_packages:
        - docker-ce
        - kubelet
```

## Defaults

`upgrade_exclude_packages` defaults to an empty list.
