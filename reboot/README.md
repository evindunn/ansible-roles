# reboot

Provides a simple reboot task for roles that notify or include host restarts.

## How It Works

The role calls the Ansible `reboot` module with a `connect_timeout` of 180 seconds.

The task is marked unchanged so invoking this role does not report a normal configuration change by itself.
