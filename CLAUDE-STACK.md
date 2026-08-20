# CLAUDE-STACK.md — how the Claude layers fit together on this machine

> Companion to `MACHINE.md`. That doc says where state lives; this one says how the
> Claude Code system is wired: context layers, capability layers, what's global vs
> per-project, and where a new thing should go. Written 2026-07-31.

## The one-sentence model

**Unix holds the hands, files hold the map, memory holds what Claude has learned,
MCP adds hands Unix doesn't have, and skills are recipes that tell the hands what
to do.**

## Context layers — what Claude *knows*, and when it loads

Ordered from "always loaded" to "loaded on demand":

| Layer | Path | Loads | Belongs there |
|---|---|---|---|
| 1. Constitution | `~/.claude/CLAUDE.md` | every session, everywhere | **Currently absent (deliberate slot).** Machine-wide invariants only, <15 lines: the two-tree rule, git identities, push-at-close, sensitive-data rules. Dictated by Shane, never inferred. |
| 2. Memory | `~/.claude/projects/-Users-shane/memory/` | index (`MEMORY.md`) every session; individual memories recalled as relevant | What Claude has *learned*: project state, preferences, corrections, pointers. Evolving knowledge. Not for hard rules — recall is selective. |
| 3. Territory maps | `AGENTS.md` at every area/project root (+ `CLAUDE.md` = `@AGENTS.md` loader) | on entering the territory | Canonical facts about that territory: what it is, its conventions, its tools and skills. Parents route, children own. |
| 4. Skills | `<repo>/.claude/skills/<name>/SKILL.md` (project) or `~/.claude/skills/` (personal, currently empty) | when invoked | Procedures: steps, output shapes, judgment rules for a repeatable job. |

A session opened at `~` loads: (1 if it existed) → (2, the memory index) → then 3 and 4 arrive as Claude enters territories or invokes skills. Nothing else is pre-loaded — the system is lazy by design.

## Capability layers — what Claude can *do*

| Kind | Examples here | Registered where | How Claude discovers it |
|---|---|---|---|
| Harness built-ins | Bash, file read/write, sub-agents, web search | ships with Claude Code | always present |
| Machine capabilities (via Bash) | `git`, `gh`, `vercel`, `psql`, `node`, `ssh` (Tailscale: `mini`, `apc-agent`, `macbook`), any script (`~/tools/`, repo `scripts/`) | **nowhere — Unix is the registry** (PATH, `~/.ssh/config`, `~/.gitconfig`) | probes (`which`, `--help`, reading config), or is told via layers 1–3 |
| MCP servers | Gmail (claude.ai connector), Chrome control, computer use, Playwright, Vercel plugin | user scope = available everywhere; a repo's `.mcp.json` = that project only | listed in session; typed tools with schemas |
| Plugins | superpowers (TDD etc.), Vercel pack | `~/.claude/plugins/` + `~/.cache/plugins/` | their skills appear in every session |

**When machine capabilities need writing down** (into layers 1–3): only when a cold
session would get it wrong or waste time discovering it — e.g. "the mini is `ssh mini`
and runs Micko's stack." If `which foo` answers it, don't document it.

**When something should be an MCP**: only when a shell can't reach it — live browser
state, OAuth'd services (credentials stay inside the server, never pass through
Claude as text), desktop control, persistent connections. Anyone can write one,
including us (e.g. a future micko-DB MCP, project-scoped).

## Global vs project — the actual split on this machine

**Global (`~/.claude/`)** — applies to every session:
- `CLAUDE.md` — empty slot, reserved for the constitution
- `projects/-Users-shane/memory/` — the memory system (MEMORY.md index + one file per fact)
- `skills/` — doesn't exist yet; first entry = first genuinely cross-project procedure
- `settings.json` / `settings.local.json` — harness config, permissions, hooks
- `plugins/` — installed plugin packs

**Per-project** — applies inside that territory:
- `AGENTS.md` — the canonical map (weekly-budget's has DB conventions + ingestion rules; micko's has the kb/doctrine structure + push rule)
- `.claude/skills/` — repo-owned procedures (weekly-budget: `reconcile`)
- `.mcp.json` — repo-scoped MCP servers (none yet)
- The repo's own scripts (`scripts/reconcile.ts`) — the tools those skills drive

**How they relate:** closest wins. A project convention overrides a global default
inside its territory; the constitution states only things no territory may override.
Skills follow the same idea — a repo skill shadows a same-named personal skill for
files in its territory.

## Where does a new thing go? (decision table)

| The new thing is… | It goes… |
|---|---|
| A rule that must never be violated, anywhere | `~/.claude/CLAUDE.md` (constitution) |
| A fact about one territory | that territory's `AGENTS.md` |
| Something Claude learned about Shane / project state | memory (Claude maintains it) |
| A repeatable procedure for one repo's tooling | `<repo>/.claude/skills/` |
| A repeatable procedure that's machine-wide | `~/.claude/skills/<name>/` (SKILL.md + optionally its own script) |
| A deterministic processing step | a script — in the repo it serves, or bundled inside the skill folder |
| A capability needing auth/live connection | MCP server — user scope if general, `.mcp.json` if project-only |
| An automated behaviour ("every time X, do Y") | a hook in `settings.json` — the harness enforces it, not Claude's memory |
| A scheduled/recurring job | cloud routine (claude.ai/code/routines) — fires without this machine |

## What this enables (the target UX)

Open a session anywhere → constitution + memory load → point at a folder → the
territory self-describes → say "do the thing" → the right skill names its own tools
and MCPs → it goes. The human never wires plumbing at prompt time; the wiring lives
in the layers above, each piece at the narrowest scope that owns it.

## Keeping this current

This doc changes when the *architecture* changes (new layer, new scope rule, first
personal skill, constitution installed) — not when individual skills or repos are
added; those are visible from their own territories. Copy to `~/Documents/` after
edits, same as MACHINE.md.
