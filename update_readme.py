"""Update the top-level README role summary table."""

import pathlib


README_PATH = pathlib.Path("README.md")
ROLE_TABLE_END = "<!-- role-table:end -->"
ROLE_TABLE_START = "<!-- role-table:start -->"


def read_role_description(role_path: pathlib.Path) -> tuple[str, str, str] | None:
    """Read a role name and one-line description from its README."""
    readme_path = role_path / "README.md"
    if not readme_path.exists():
        return None

    lines = readme_path.read_text(encoding="utf-8").splitlines()
    role_name = ""
    description_parts: list[str] = []
    found_heading = False

    for line in lines:
        stripped = line.strip()
        if not found_heading:
            if stripped.startswith("# "):
                role_name = stripped[2:].strip()
                found_heading = True
            continue

        if not stripped:
            if description_parts:
                break
            continue

        if stripped.startswith("#"):
            break

        description_parts.append(stripped)

    if not role_name or not description_parts:
        return None

    return role_name, role_path.name, " ".join(description_parts)


def build_role_table() -> str:
    """Build the Markdown role summary table."""
    role_rows: list[tuple[str, str, str]] = []
    for role_path in sorted(path for path in pathlib.Path(".").iterdir() if path.is_dir()):
        if role_path.name.startswith("."):
            continue

        role_description = read_role_description(role_path)
        if role_description is not None:
            role_rows.append(role_description)

    lines = [
        ROLE_TABLE_START,
        "| role | description |",
        "| --- | --- |",
    ]
    lines.extend(
        f"| [{role}]({role_path}/) | {description} |"
        for role, role_path, description in role_rows
    )
    lines.append(ROLE_TABLE_END)
    return "\n".join(lines)


def update_readme() -> None:
    """Update or append the generated role table in README.md."""
    readme_text = README_PATH.read_text(encoding="utf-8")
    role_table = build_role_table()

    if ROLE_TABLE_START in readme_text and ROLE_TABLE_END in readme_text:
        start = readme_text.index(ROLE_TABLE_START)
        end = readme_text.index(ROLE_TABLE_END) + len(ROLE_TABLE_END)
        updated_text = f"{readme_text[:start]}{role_table}{readme_text[end:]}"
    else:
        updated_text = readme_text.rstrip() + "\n\n## Roles\n\n" + role_table + "\n"

    README_PATH.write_text(updated_text, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
