# iptables-persistent

Installs `iptables-persistent` and renders persistent IPv4 and IPv6 rules.

Contributes `netfilter-persistent` to the [needsrestart role](../needsrestart/README.md)
through `needsrestart_ignore_services__iptables_persistent`. Run `needsrestart`
before package changes. Set the contribution to `[]` to allow automatic restarts.

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

Rules are defined as YAML lists of strings. Append rules for `INPUT`, `OUTPUT`,
and `FORWARD` are redirected into role-owned `ANSIBLE-*` chains. The configured
policy is the final verdict in each of those chains.

The systemd override applies these files with `iptables-restore --noflush` and
`ip6tables-restore --noflush`. Only declared custom chains are replaced. Existing
Docker chains and built-in-chain rules are preserved. Hooks are inserted only
when missing. On hosts that declare `DOCKER-USER`, Docker owns forwarding;
the role does not hook its `ANSIBLE-FORWARD` chain into `FORWARD`.

Only declare custom chains that this role owns, such as `DOCKER-USER`. Do not
declare Docker's internal chains. Do not add direct built-in-chain rules with
operations other than `-A`; these are not redirected into managed chains.

Use `systemctl reload netfilter-persistent` to apply edits. The service override
also applies the same rules at boot. Do not use `netfilter-persistent save` or
the stock command-line `reload`: those bypass this service override. Existing
legacy rules in built-in chains remain during migration; the new hooks take
precedence. A reboot removes those legacy in-memory rules.

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

## Example

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
