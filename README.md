### ansible-roles
Collection of ansible roles that I've written for the homelab

## Roles

<!-- role-table:start -->
| role | description |
| --- | --- |
| [ansible](ansible/) | Installs a pinned Ansible release into a dedicated virtualenv and exposes it on the system PATH. |
| [authorized_keys](authorized_keys/) | Manages SSH authorized keys and optionally disables password authentication. |
| [bash](bash/) | Adds global Bash defaults to `/etc/bash.bashrc`. |
| [consul](consul/) | Installs Consul, optional consul-template, server service overrides, firewalld service definitions, and Envoy. |
| [crio](crio/) | Configures kernel prerequisites, the upstream CRI-O apt repository, and the CRI-O service. |
| [crowdsec](crowdsec/) | Installs CrowdSec with the iptables firewall bouncer and optional parsers. |
| [custom-facts](custom-facts/) | Collects OS-specific details into an Ansible local fact file. |
| [docker](docker/) | Installs pinned Docker packages, configures the daemon, and prevents package upgrades. |
| [firewalld](firewalld/) | Installs firewalld and manages zone XML from Ansible variables. |
| [hashicorp_repo](hashicorp_repo/) | Adds the HashiCorp package repository for the target operating system. |
| [hostname](hostname/) | Sets the host name from the PTR record of the default IPv4 address. |
| [iptables-persistent](iptables-persistent/) | Installs `iptables-persistent` and renders persistent IPv4 and IPv6 rules. |
| [k8s_node](k8s_node/) | Installs Kubernetes node packages from the upstream apt repository and disables swap. |
| [locale](locale/) | Installs locale support and configures the system locale and keyboard layout. |
| [nginx](nginx/) | Installs NGINX after applying operating-system-specific repository setup. |
| [node_exporter](node_exporter/) | Installs Prometheus node_exporter from GitHub releases and manages its systemd service. |
| [ntp-client](ntp-client/) | Configures OS-specific time synchronization and the system timezone. |
| [postgres-client](postgres-client/) | Installs the PostgreSQL client package for a selected major version. |
| [postgres-common](postgres-common/) | Adds the upstream PostgreSQL apt repository and signing key. |
| [postgres-server](postgres-server/) | Installs the PostgreSQL server package for a selected major version. |
| [reboot](reboot/) | Provides a simple reboot task for roles that notify or include host restarts. |
| [samba-server](samba-server/) | Installs and starts Samba, with an optional Samba exporter on amd64 hosts. |
| [trusted-certs](trusted-certs/) | Installs additional trusted certificate authorities and refreshes the system trust store. |
| [unattended-upgrades](unattended-upgrades/) | Configures unattended package updates for Debian and RedHat families. |
| [update](update/) | Runs operating-system-specific package update tasks. |
| [vault](vault/) | Installs Vault and configures either a server service or an AppRole-backed Vault Agent. |
| [vim](vim/) | Installs Vim and deploys a global vimrc. |
<!-- role-table:end -->


### Setup

Create a local virtualenv:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python requirements:

```bash
pip install -r requirements.txt
```

Install the Ansible Galaxy collections:

```bash
ansible-galaxy collection install -r requirements.yml
```
