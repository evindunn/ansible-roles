# crowdsec

Installs CrowdSec with the iptables firewall bouncer and optional parsers.

## Example

```yml
- hosts: edge
  roles:
    - role: crowdsec
      crowdsec_parsers:
        - crowdsecurity/sshd-logs
        - crowdsecurity/nginx-logs
```

## Defaults

`crowdsec_parsers` defaults to an empty list.
