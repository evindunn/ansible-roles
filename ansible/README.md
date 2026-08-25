# ansible

Installs a pinned Ansible release into a dedicated virtualenv and exposes it on the system PATH.

## Example

```yml
- hosts: controllers
  roles:
    - role: ansible
      install_ansible_version: "5.6.0"
      install_ansible_extra_pkgs:
        - boto3
        - dnspython
```

## Defaults

`install_ansible_version` defaults to `5.6.0`. `install_ansible_extra_pkgs` includes `boto3` and `dnspython`.
