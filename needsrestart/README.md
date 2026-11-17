# needsrestart

Configures services that NEEDRESTART must exclude from automatic restarts.

## Example

Apply the role before package updates or other roles that install packages:

```yml
---
- hosts: servers
  become: true
  roles:
    - role: needsrestart
      needsrestart_ignore_services:
        - docker
        - nginx.service
        - worker@production
```

## Variables

`needsrestart_ignore_services` defaults to an empty list. Entries are literal
service names, with or without the `.service` suffix. Duplicates are removed.
Regular expressions and wildcards are not supported.

Groups can contribute lists through distinct variables named
`needsrestart_ignore_services__<name>`. For example:

```yml
---
# group_vars/docker/all.yml
needsrestart_ignore_services__docker:
  - docker
```

```yml
---
# group_vars/nginx_servers/all.yml
needsrestart_ignore_services__nginx:
  - nginx
```

The role combines all matching contribution variables available to the host
with `needsrestart_ignore_services`. A host in both groups excludes both services.
Use distinct suffixes for separate contributions; assigning the same variable
in multiple groups still follows normal Ansible variable precedence. The role
uses built-in lookups and does not require a list merge plugin.

The role writes `/etc/needrestart/conf.d/ansible-ignored-services.conf` and
validates its Perl syntax before saving it. It adds entries to
`$nrconf{override_rc}` without replacing other NEEDRESTART settings.
These services remain visible in NEEDRESTART reports but are not selected
for automatic restarts.

Each run replaces this role's exclusions with the combined lists. To clear this
role's exclusions, all applicable lists must be empty or removed. The role
removes the old `docker.conf` and
`nginx.conf` drop-ins after writing the central configuration. Exclusions in
other files still apply.

NEEDRESTART and Perl must already be installed. The role does not install
packages or change NEEDRESTART's restart mode. No service restart is needed.

See the [upstream configuration](https://github.com/liske/needrestart/blob/master/ex/needrestart.conf)
for the `override_rc` setting.
