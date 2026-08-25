# bash

Adds global Bash defaults to `/etc/bash.bashrc`.

## How It Works

The role writes each string from `bash_opts` to `/etc/bash.bashrc` with `lineinfile`, creating the file if it does not exist.

Use `bash_opts` for simple global shell aliases or options that should be present exactly once.

## Defaults

`bash_opts` defines `ls` and `ll` aliases.
