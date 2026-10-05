# docker

Installs pinned Docker packages, configures the daemon, and prevents package upgrades.

On Debian-family systems, configures NEEDRESTART to skip automatic Docker restarts.

## Example

```yml
- hosts: container_hosts
  roles:
    - role: docker
      docker_daemon_opts:
        live-restore: true
        storage-driver: overlay2
        exec-opts:
          - native.cgroupdriver=systemd
```

## Defaults

`docker_daemon_opts` follows Kubernetes-oriented defaults with `overlay2`, systemd cgroups, live restore, and bounded JSON logs.
