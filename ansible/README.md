# ansible

Installs a pinned Ansible release into a dedicated virtualenv and exposes it on the system PATH.

## How It Works

The role removes the OS-packaged `ansible`, installs platform-specific prerequisites, creates `/opt/ansible-{{ install_ansible_version }}`, and installs Ansible plus any `install_ansible_extra_pkgs` with `pip`.

It templates `/etc/profile.d/ZZ-add-ansible-to-path.sh` so interactive shells find the virtualenv binaries first. Debian hosts use `python3`; RedHat hosts use `python3.8`.

## Defaults

`install_ansible_version` defaults to `5.6.0`. `install_ansible_extra_pkgs` includes `boto3` and `dnspython`.
