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

## Parser contributions

Groups and roles can contribute parsers through distinct variables named
`crowdsec_parsers__<name>`, using the same convention as the
[needsrestart role](../needsrestart/README.md). For example:

```yml
---
crowdsec_parsers__nginx:
  - crowdsecurity/nginx-logs
```

The role combines all matching contributions with `crowdsec_parsers`, removes
duplicates, and installs parsers in sorted order. Use a distinct suffix for each
contribution so overlapping groups do not replace each other's lists.
Setting the base list to `[]` does not disable group contributions; empty or
remove the relevant contribution as well. Removing a parser from the lists
does not uninstall an already installed parser.
