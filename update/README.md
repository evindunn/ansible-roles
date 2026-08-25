# update

Runs operating-system-specific package update tasks.

## How It Works

The role includes the task file matching `ansible_facts['os_family']`.

Debian and RedHat implementations live in separate task files so package cache refresh and upgrade behavior can follow each platform's package manager.
