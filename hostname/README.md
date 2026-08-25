# hostname

Sets the host name from the PTR record of the default IPv4 address.

## How It Works

The role performs a reverse DNS lookup for `ansible_facts['default_ipv4']['address']`. If the lookup returns a real hostname, it strips the trailing dot, derives the short hostname, and applies it with the `hostname` module.

It also writes `127.0.1.1` in `/etc/hosts` with the fully qualified and short hostnames.
