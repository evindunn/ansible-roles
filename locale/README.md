# locale

Installs locale support and configures the system locale and keyboard layout.

## Example

```yml
- hosts: servers
  roles:
    - role: locale
      locale: en_US.UTF-8
      keyboard_layout: us
```

## Defaults

`locale` defaults to `en_US.UTF-8`. `keyboard_layout` defaults to `us`.
