# docker

Installs pinned Docker packages, configures the daemon, and prevents package upgrades.

## How It Works

The role loads OS-specific variables and repository setup tasks, installs Docker dependencies and packages, then pins those packages with `dpkg_selections` on Debian or `dnf versionlock` on RedHat.

It templates `/etc/docker/daemon.json` from `docker_daemon_opts`, writes a systemd mount-flags override, reloads Docker when needed, and ensures the service is enabled and running.

## Defaults

`docker_daemon_opts` follows Kubernetes-oriented defaults with `overlay2`, systemd cgroups, live restore, and bounded JSON logs.
