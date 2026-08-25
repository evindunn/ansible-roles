# vim

Installs Vim and deploys a global vimrc.

## How It Works

The role loads OS-family variables, installs each package in `pkgs`, and copies the bundled `vimrc` to the OS-specific `vimrc_path`.

Use OS-family vars to adjust package names or the destination path for different distributions.

## Defaults

`pkgs` defaults to `vim`.
