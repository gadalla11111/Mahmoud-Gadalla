#!/usr/bin/env python3
"""Skill-library maintenance auditor.

The mechanical half of the library-maintainer loop: OVERVIEW + EVALUATE.
Reports library state and every drift class this session learned to catch.
Exit code 0 = clean, 1 = issues found (so a loop/cron can decide to act).

Usage:
    python misc/library_audit.py            # human report
    python misc/library_audit.py --json     # machine report for a loop
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "anthropic_skills"
ROUTING_SURFACES = {
    "orchestrator": SKILLS / "orchestrator" / "SKILL.md",
    "CLAUDE.md": ROOT / "CLAUDE.md",
    "skills.md": ROOT / ".memory" / "skills.md",
}


def frontmatter(path: Path):
    text = path.read_text()
    if not text.startswith("---"):
        return None, "no-frontmatter"
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, "malformed-fences"
    try:
        return yaml.safe_load(parts[1]), None
    except Exception as exc:  # noqa: BLE001
        return None, f"invalid-yaml: {str(exc)[:60]}"


def audit():
    findings: list[dict] = []
    top = sorted(p for p in SKILLS.glob("*/SKILL.md"))
    nested = sorted(
        p for p in SKILLS.glob("*/*/SKILL.md")
        if not re.fullmatch(r"anthropic_skills/[^/]+/SKILL.md", str(p.relative_to(ROOT)))
    )
    custom = sorted((ROOT / "skills" / "custom_skills").glob("*/SKILL.md"))

    bundled, first_party, names = set(), set(), {}
    for p in top:
        name = p.parent.name
        fm, err = frontmatter(p)
        if err:
            findings.append({"sev": "high", "skill": name, "issue": err})
            continue
        names[name] = fm
        is_bundled = bool(re.search(r"license:.*LICENSE", p.read_text()))
        (bundled if is_bundled else first_party).add(name)
        # health block required on first-party
        if not is_bundled and "health" not in (fm or {}):
            findings.append({"sev": "med", "skill": name, "issue": "missing-health-block"})
        # stale/unrun eval on first-party
        if not is_bundled and isinstance(fm, dict):
            h = fm.get("health") or {}
            if h.get("pass_rate") is None:
                findings.append({"sev": "low", "skill": name, "issue": "eval-never-run"})

    # routing sync: every top-level skill reachable in each surface
    surface_text = {k: v.read_text() if v.exists() else "" for k, v in ROUTING_SURFACES.items()}
    EXEMPT = {"template", "agent-skills-spec"}  # scaffolds / non-routed
    for name in names:
        if name in EXEMPT:
            continue
        for surface, text in surface_text.items():
            if name not in text:
                findings.append(
                    {"sev": "med", "skill": name, "issue": f"missing-from-{surface}"}
                )

    # count-claim consistency
    total = len(top) + len(nested) + len(custom)
    claim = None
    m = re.search(r"(\d+)-skill library", surface_text["orchestrator"])
    if m:
        claim = int(m.group(1))
    expected_in_anthropic = len(top) + len(nested)
    if claim is not None and claim != expected_in_anthropic:
        findings.append({
            "sev": "low", "skill": "orchestrator",
            "issue": f"count-claim {claim} != actual anthropic_skills SKILL.md {expected_in_anthropic}",
        })

    return {
        "totals": {
            "top_level": len(top), "nested": len(nested),
            "custom": len(custom), "grand_total": total,
            "first_party": len(first_party), "bundled": len(bundled),
        },
        "count_claim": claim,
        "findings": findings,
        "clean": not findings,
    }


def main():
    report = audit()
    if "--json" in sys.argv:
        print(json.dumps(report, indent=2))
        sys.exit(0 if report["clean"] else 1)

    t = report["totals"]
    print(f"# Library Audit\n")
    print(f"Skills: {t['grand_total']} "
          f"({t['top_level']} top-level + {t['nested']} nested + {t['custom']} custom) | "
          f"first-party {t['first_party']}, bundled {t['bundled']}")
    print(f"Orchestrator claims: {report['count_claim']}-skill library\n")
    if report["clean"]:
        print("✅ CLEAN — no drift detected.")
        sys.exit(0)
    order = {"high": 0, "med": 1, "low": 2}
    for f in sorted(report["findings"], key=lambda x: order[x["sev"]]):
        sev = {"high": "🔴", "med": "🟠", "low": "🟡"}[f["sev"]]
        print(f"{sev} {f['skill']}: {f['issue']}")
    print(f"\n{len(report['findings'])} finding(s).")
    sys.exit(1)


if __name__ == "__main__":
    main()
