# k8s_node

Installs Kubernetes node packages from the upstream apt repository and disables swap.

## Example

```yml
- hosts: k8s_nodes
  roles:
    - role: crio

    - role: k8s_node
      k8s_version: "1.30"
```

## Defaults

`k8s_version` defaults to `1.30`.
