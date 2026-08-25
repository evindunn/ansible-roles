#!/usr/bin/env python3

"""Create a new Ansible role from built-in Python templates."""

import argparse
import pathlib
import re


DEFAULT_FILES = {
    "README.md": """# {name}

{description}

## Example

```yml
- hosts: servers
  roles:
    - role: {name}
```
""",
    "defaults/main.yml": """---

""",
    "meta/main.yml": """---

dependencies: []
""",
    "tasks/main.yml": """---

- name: Placeholder task for {name}
  ansible.builtin.debug:
    msg: "Role {name} has not been implemented yet."
""",
}
ROLE_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+$")


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Role directory name to create.")
    parser.add_argument(
        "description",
        nargs="+",
        help="One-line role description for the generated README.",
    )
    return parser.parse_args()


def validate_role_name(name: str) -> None:
    """Validate that a role name is safe to create under the current directory."""
    if not ROLE_NAME_PATTERN.fullmatch(name):
        raise ValueError("Role names may only contain letters, numbers, dots, underscores, and dashes.")

    if name in {".", ".."}:
        raise ValueError("Role name must not be a relative directory marker.")


def create_role(name: str, description: str) -> pathlib.Path:
    """
    Create a role directory from the default templates.

    :param name: Role directory name.
    :param description: One-line README description.
    :returns: Path to the created role directory.
    :raises FileExistsError: If the role directory already exists.
    """
    validate_role_name(name)
    role_path = pathlib.Path(name)
    if role_path.exists():
        raise FileExistsError(f"{role_path} already exists")

    for relative_path, template in DEFAULT_FILES.items():
        target_path = role_path / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(
            template.format(name=name, description=description).rstrip() + "\n",
            encoding="utf-8",
        )

    return role_path


def main() -> None:
    """Run the role creation command."""
    args = parse_args()
    description = " ".join(args.description).strip()
    if not description:
        raise ValueError("Description must not be empty.")

    role_path = create_role(args.name, description)
    print(f"Created {role_path}")


if __name__ == "__main__":
    main()
