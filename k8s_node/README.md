# k8s_node

Installs Kubernetes node packages from the upstream apt repository and disables swap.

## How It Works

The role installs apt prerequisites, downloads and dearmors the Kubernetes package key, adds the repository for `k8s_version`, and installs `kubelet`, `kubeadm`, and `kubectl`.

If swap is active, it runs `swapoff -a` and removes swap entries from `/etc/fstab`.

## Defaults

`k8s_version` defaults to `1.30`.
