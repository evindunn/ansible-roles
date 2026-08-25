# iptables-persistent

Installs `iptables-persistent` and renders persistent IPv4 and IPv6 rules.

## Defaults

```yml
iptables_persistent_rules: []

iptables_persistent_ipv4_rules: "{{ iptables_persistent_rules }}"
iptables_persistent_ipv6_rules: "{{ iptables_persistent_rules }}"

iptables_persistent_default_policies:
  INPUT: ACCEPT
  FORWARD: ACCEPT
  OUTPUT: ACCEPT

iptables_persistent_ipv4_default_policies: "{{ iptables_persistent_default_policies }}"
iptables_persistent_ipv6_default_policies: "{{ iptables_persistent_default_policies }}"
iptables_persistent_force_restart: false
```

## Rule Format

Rules are defined as YAML lists of strings. Each item is rendered literally as
one line in the `filter` table.

```yml
iptables_persistent_rules:
  - "-A INPUT -p tcp --dport 22 -j ACCEPT"
  - "-A INPUT -p tcp --dport 80 -j ACCEPT"
```

`iptables_persistent_rules` is a shared list used by both IPv4 and IPv6 by
default. Use `iptables_persistent_ipv4_rules` or `iptables_persistent_ipv6_rules`
when rules contain address-family-specific values.

`iptables_persistent_default_policies` is shared by both address families by
default. Use `iptables_persistent_ipv4_default_policies` or
`iptables_persistent_ipv6_default_policies` when policies differ by family.

## Examples

```yml
iptables_persistent_ipv4_default_policies:
  INPUT: DROP
  FORWARD: DROP
  OUTPUT: ACCEPT
  DOCKER-USER: "-"

iptables_persistent_ipv4_rules:
  - "-A INPUT -i lo -j ACCEPT"
  - "-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT"
  - "-A INPUT -p tcp -s 203.0.113.0/24 --dport 22 -j ACCEPT"
  - "-A INPUT -p tcp -m multiport --dports 80,443 -j ACCEPT"
  - '-A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables dropped: " --log-level info'
  - "-A INPUT -j DROP"

iptables_persistent_ipv6_rules:
  - "-A INPUT -i lo -j ACCEPT"
  - "-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT"
  - "-A INPUT -p tcp -s 2001:db8::/32 --dport 22 -j ACCEPT"
```
