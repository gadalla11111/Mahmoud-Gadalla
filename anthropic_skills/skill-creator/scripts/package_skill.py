#!/usr/bin/env python3
"""Validate and package a skill directory into a distributable zip."""
import argparse
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def validate(skill_dir: Path) -> list[str]:
    errors = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md not found")
        return errors

    content = skill_md.read_text()
    if not content.startswith("---"):
        errors.append("SKILL.md missing YAML frontmatter")
        return errors

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md frontmatter not properly closed")
        return errors

    frontmatter = parts[1]
    if yaml:
        meta = yaml.safe_load(frontmatter)
    else:
        meta = {}
        for line in frontmatter.strip().splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip()

    if not meta.get("name"):
        errors.append("SKILL.md missing required 'name' field")
    elif meta["name"] != skill_dir.name:
        errors.append(f"name '{meta['name']}' must match directory name '{skill_dir.name}'")

    if not meta.get("description"):
        errors.append("SKILL.md missing required 'description' field")
    elif "TODO" in meta.get("description", ""):
        errors.append("description still contains TODO placeholder")

    if not parts[2].strip():
        errors.append("SKILL.md body is empty")

    return errors


def package(skill_dir: Path, output_dir: Path) -> None:
    errors = validate(skill_dir)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"{skill_dir.name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in skill_dir.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(skill_dir.parent))
    print(f"Packaged: {zip_path}")


def main():
    parser = argparse.ArgumentParser(description="Validate and package a skill directory.")
    parser.add_argument("skill_path", help="Path to skill directory")
    parser.add_argument("output_dir", nargs="?", default=".", help="Output directory for zip")
    args = parser.parse_args()

    package(Path(args.skill_path), Path(args.output_dir))


if __name__ == "__main__":
    main()
