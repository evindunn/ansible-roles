# ntp-client

Configures OS-specific time synchronization and the system timezone.

## Example

```yml
- hosts: servers
  roles:
    - role: ntp-client
      timezone: America/New_York
      ntp_server: pool.ntp.org
```

## Defaults

`timezone` defaults to `America/New_York`. `ntp_server` defaults to `pool.ntp.org`.
