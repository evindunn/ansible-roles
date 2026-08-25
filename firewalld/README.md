# firewalld

Installs firewalld and manages zone XML from Ansible variables.

## Example

```yml
- hosts: servers
  roles:
    - role: firewalld
      firewalld_default_zone: public
      firewalld_zones:
        public:
          target: DROP
          services:
            - ssh
            - http
            - https
```

## Defaults

`firewalld_default_zone` defaults to `public`. The default public zone drops traffic except SSH.
