# trusted-certs

Installs additional trusted certificate authorities and refreshes the system trust store.

## Example

```yml
- hosts: servers
  roles:
    - role: trusted-certs
      trusted_certs:
        - internal-root-ca.crt
        - internal-issuing-ca.crt
```

## Defaults

`trusted_certs` defaults to an empty list.
