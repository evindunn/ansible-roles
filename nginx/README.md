# nginx

Installs NGINX after applying operating-system-specific repository setup.

## How It Works

The role includes the task file matching `ansible_facts['os_family']`, then installs the `nginx` package and notifies the handler that enables and starts NGINX.

The role also ships common NGINX configuration snippets under `files/conf.d` for use by playbooks or companion roles.
