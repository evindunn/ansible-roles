# crio

Configures kernel prerequisites, the upstream CRI-O apt repository, and the CRI-O service.

## How It Works

The role installs `lvm2`, templates module-load configuration, loads required kernel modules, and applies CRI-O networking sysctls. If `crio_volume` is defined, it mounts that volume at `/var/lib/containers/storage`.

It downloads and dearmors the Kubernetes CRI-O repository key, adds the CRI-O apt repository for `crio_version`, installs `cri-o`, and starts/enables the `crio` service.

## Defaults

`crio_version` defaults to `1.30`. The default kernel modules are `overlay` and `br_netfilter`.
