# nginx

Installs NGINX after applying operating-system-specific repository setup.

On Debian-family systems, configures NEEDRESTART to skip automatic NGINX restarts.

## Example

```yml
- hosts: web
  roles:
    - role: nginx
```
