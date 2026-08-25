# crio

Configures kernel prerequisites, the upstream CRI-O apt repository, and the CRI-O service.

## Example

```yml
- hosts: k8s_nodes
  roles:
    - role: crio
      crio_version: "1.30"
      crio_volume: /dev/disk/by-label/crio
```

## Defaults

`crio_version` defaults to `1.30`. The default kernel modules are `overlay` and `br_netfilter`.
