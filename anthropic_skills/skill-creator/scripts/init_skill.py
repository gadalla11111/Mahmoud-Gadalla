#!/usr/bin/env python3
"""Initialize a new skill directory with SKILL.md template and example resource dirs."""
import argparse
import os
import sys
from pathlib import Path

SKILL_MD_TEMPLATE = """\
---
name: {name}
description: TODO: Replace with description of what this skill does and when to use it.
license: Complete terms in LICENSE.txt
---

# {title}

TODO: Add skill instructions here.

## Purpose

TODO: Describe the skill's purpose.

## Usage

TODO: Describe how to use this skill.
"""

EXAMPLE_SCRIPT = """\
#!/usr/bin/env python3
\"\"\"Example script — replace or delete.\"\"\"
import sys

def main():
    print("Hello from skill script!")

if __name__ == "__main__":
    main()
"""

EXAMPLE_REFERENCE = """\
# Reference

TODO: Add reference material here (schemas, API docs, policies, etc.)
"""


def init_skill(name: str, output_path: Path) -> None:
    skill_dir = output_path / name
    if skill_dir.exists():
        print(f"Error: {skill_dir} already exists.", file=sys.stderr)
        sys.exit(1)

    (skill_dir / "scripts").mkdir(parents=True)
    (skill_dir / "references").mkdir()
    (skill_dir / "assets").mkdir()

    (skill_dir / "SKILL.md").write_text(
        SKILL_MD_TEMPLATE.format(name=name, title=name.replace("-", " ").title())
    )
    script = skill_dir / "scripts" / "example.py"
    script.write_text(EXAMPLE_SCRIPT)
    script.chmod(0o755)
    (skill_dir / "references" / "example.md").write_text(EXAMPLE_REFERENCE)

    print(f"Skill initialized at: {skill_dir}")
    print("Next: edit SKILL.md, add scripts/references/assets, then run package_skill.py")


def main():
    parser = argparse.ArgumentParser(description="Initialize a new Claude skill directory.")
    parser.add_argument("name", help="Skill name (lowercase, hyphens for spaces)")
    parser.add_argument("--path", default=".", help="Output directory (default: current dir)")
    args = parser.parse_args()

    if not args.name.replace("-", "").isalnum() or args.name != args.name.lower():
        print("Error: skill name must be lowercase alphanumeric + hyphens.", file=sys.stderr)
        sys.exit(1)

    init_skill(args.name, Path(args.path))


if __name__ == "__main__":
    main()
