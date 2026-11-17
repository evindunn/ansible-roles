# nginx

Installs NGINX after applying operating-system-specific repository setup.

Configure automatic restart exclusions with the [needsrestart role](../needsrestart/README.md).

## Example

```yml
- hosts: web
  roles:
    - role: nginx
```
