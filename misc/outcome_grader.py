"""
Outcome Grader — agents that verify their own work.
A writer agent drafts a research brief; an independent grader checks it
against a rubric and sends feedback; the writer revises until it passes.

Based on: managed_agents/CMA_verify_with_outcome_grader.ipynb
Requires: ANTHROPIC_API_KEY with credits + Managed Agents beta access.
"""

import os
import re
import time

import anthropic
from dotenv import load_dotenv

load_dotenv()

BETAS = ["managed-agents-2026-04-01"]
MODEL = os.environ.get("COOKBOOK_MODEL", "claude-sonnet-4-6")
client = anthropic.Anthropic()

# ── Task & Rubric ─────────────────────────────────────────────────────────────
# TASK  → the writer reads this (what to produce)
# RUBRIC → the grader reads this (how to verify it)
# They must agree on artifact location and format.

TASK = """Write a brief on the unit economics of public DC fast charging in the United States.
The brief should cover:
  1. Capex range
  2. Demand charges
  3. Utilization breakeven
  4. Subsidy programs
  5. Named-operator economics
  6. A contrarian or skeptical source
  7. Hardware vs install cost split
"""

RUBRIC = """
You are reviewing a research brief at /mnt/session/outputs/brief.md against a coverage
checklist and verifying its citations.

COVERAGE CHECKLIST:
  1. Capex range: a dollar range for installed cost per DC fast-charging stall or station.
  2. Demand charges: quantified impact on opex (a $/kW figure or a % of operating cost).
  3. Utilization breakeven: a breakeven or target utilization threshold (% or kWh/day).
  4. Subsidy programs: NEVI or another public funding program, named.
  5. Named operator: GAAP net income/loss from a specific public charging operator's most
     recent 10-K or 10-Q. Citation MUST be the SEC filing itself (sec.gov), not a press
     release, earnings-call recap, or news article.
  6. Contrarian source: at least one cited source whose thesis is that the economics are
     unfavorable or structurally challenged.
  7. Cost split: a hardware vs soft-cost (install, permitting, grid) breakdown or ratio.

CITATION CHECK for every [n] entry in Sources:
  a. LIVE: Fetch the URL. LIVE = readable page returned. DEAD = 404 / login-wall / 403.
     Do NOT corroborate via mirrors, reposts, or search snippets.
  b. VERBATIM: Search the fetched page for the quoted string. QUOTE_MATCH or NOT_FOUND.
  c. SUPPORTS CLAIM: Does the quote back the claim it's cited on? SUPPORTS_CLAIM or UNSUPPORTED.

OUTPUT FORMAT:
Line 1: Coverage N/7. Citations M/K verified.
Then one bullet per failed coverage item: "Item N name - MISSING. <what's missing>"
Then one bullet per failed citation: "[n] domain - REASON. <what's wrong and what to do>"
"""


# ── Helpers ───────────────────────────────────────────────────────────────────

HR = "━" * 46


def banner(label: str, tag: str = "") -> None:
    print(f"\n{HR}\n{label}  {tag}".rstrip())


def render_feedback(fb: str) -> None:
    s = re.sub(
        r"^An independent grader found.*?:\n\n- .*?\((?:partially |not )?met\): ",
        "",
        fb,
        count=1,
        flags=re.S,
    )
    s = re.sub(r"\n\nPlease revise your work.*$", "", s, flags=re.S)
    print(s)


# ── Main ──────────────────────────────────────────────────────────────────────

def run(topic: str = TASK, rubric: str = RUBRIC, max_iterations: int = 5) -> str:
    """Run a writer → grader → revise loop. Returns final outcome status."""

    # 1. Environment + writer agent
    env = client.beta.environments.create(
        name="research-brief",
        config={"type": "anthropic_cloud", "networking": {"type": "unrestricted"}},
    )

    writer = client.beta.agents.create(
        name="Research Analyst",
        model=MODEL,
        system="""You are a research analyst. You write one-page business briefs.

Cite every factual claim with an inline footnote [n]. End the brief with a Sources section:
[n] "verbatim quote from the page, 25 words or fewer" - Title - URL

Only cite pages you actually fetched and read. Quote must be copied character-for-character.
Cite no more than 6 sources total. Save the brief to /mnt/session/outputs/brief.md.""",
        tools=[
            {
                "type": "agent_toolset_20260401",
                "configs": [
                    {"name": "web_search"},
                    {"name": "web_fetch"},
                    {"name": "read"},
                    {"name": "write"},
                ],
            }
        ],
        betas=BETAS,
    )

    session = client.beta.sessions.create(
        agent={"type": "agent", "id": writer.id, "version": writer.version},
        environment_id=env.id,
        title="Research brief with outcome grader",
        betas=BETAS,
    )
    print(f"Session {session.id}")

    # 2. Define outcome (sends task to writer, rubric to grader)
    client.beta.sessions.events.send(
        session.id,
        betas=BETAS,
        events=[
            {
                "type": "user.define_outcome",
                "description": topic,
                "rubric": {"type": "text", "content": rubric},
                "max_iterations": max_iterations,
            }
        ],
    )

    # 3. Stream the loop
    TERMINAL = {"satisfied", "max_iterations_reached", "failed", "interrupted"}
    t0 = time.time()
    result, iters, n_search, last_len = None, 0, 0, 0

    with client.beta.sessions.events.stream(session.id, betas=BETAS) as stream:
        for ev in stream:
            if ev.type == "agent.tool_use":
                if ev.name in ("web_search", "web_fetch"):
                    n_search += 1
                if ev.name == "write" and ev.input.get("file_path", "").endswith("brief.md"):
                    last_len = len(ev.input["content"])
            elif ev.type == "span.outcome_evaluation_start":
                label = "draft" if iters == 0 else f"revision {iters}"
                banner(f"writer · {label}")
                print(f"searched/fetched {n_search}×  ·  wrote brief.md ({last_len:,} chars)")
                n_search = 0
            elif ev.type == "span.outcome_evaluation_end":
                result = ev.result
                tag = "✓ satisfied" if result == "satisfied" else "⟳ needs_revision"
                banner(f"grader · pass {iters}", tag)
                render_feedback(ev.explanation)
                iters += 1
                if result in TERMINAL:
                    break

    m, s = divmod(int(time.time() - t0), 60)
    print(f"\ndone: {result} after {iters} pass{'es' if iters != 1 else ''} · {m}m {s:02d}s")

    # 4. Print final brief structure
    _print_brief_structure(session.id)
    return result


def _print_brief_structure(session_id: str) -> None:
    content = ""
    for ev in client.beta.sessions.events.list(session_id, limit=1000, betas=BETAS):
        if ev.type != "agent.tool_use" or "brief.md" not in str(ev.input.get("file_path", "")):
            continue
        if ev.name == "write":
            content = ev.input["content"]
        elif ev.name == "edit":
            content = content.replace(ev.input["old_string"], ev.input["new_string"], 1)

    print("\n── Final brief structure ──")
    for line in content.splitlines():
        if line.startswith(("#", "[")):
            print(line)


if __name__ == "__main__":
    run()
