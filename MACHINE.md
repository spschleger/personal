# MACHINE.md — MacBook (M5) rebuild manifest

> If this machine is lost or wiped, this document is the map to put it back together.
> Written 2026-07-31; **rewritten 2026-08-18 for the fresh-start rebuild** (files-only backup strategy — no TM-image restore).
> **Rebuild executed 2026-08-18 (evening) — this M5 is now the fresh-start machine.** See "Rebuild log" at the bottom.
> Copies live in `~/Documents/` (iCloud) and on the encrypted backup HDD, so it survives the machine.
> **Rebuild path: fresh macOS → install Claude Code → point it at this file → CC drives the rebuild, restoring files selectively from the HDD.** Never Migration-Assistant the old state back in.

## The rebuild procedure (CC-first)

1. Fresh macOS setup: personal Apple ID, WiFi, user account. Nothing else by hand.
2. Sign into iCloud → Documents/Desktop/Photos start syncing back.
3. Install Claude Code (`curl -fsSL https://claude.ai/install.sh | bash`), log in, open this file (from `~/Documents/` once synced, or from the HDD).
4. CC then: Homebrew + brew list → apps → restore `~/personal` and `~/projects` from the HDD backup → clone/verify repos → recreate `~/.ssh` + gitconfigs from the HDD copy → re-auth CLIs (`gh`, `vercel`, Tailscale) → set up Time Machine to the HDD.
5. Verify: repos clean + pushed, budget app connects to Neon, `ssh mini` works, TM first backup completes.

## The shape

Two working trees, never inside iCloud-synced folders:

- `~/personal/` — life. Git identity **spschleger** (personal GitHub). Non-repo areas: finances (incl. `raw/` bank exports), health-appearance, Yuyjie, Work, family-history, tenancy docs.
- `~/projects/` — ventures. Git identity **spsholdco** (business GitHub). `_archive/` = dormant.

Every area/project root: `AGENTS.md` (canonical map) + `CLAUDE.md` (`@AGENTS.md` loader). Skills live in `<repo>/.claude/skills/`.

## Where every category of state lives

| State | Primary | Offsite | Rebuild without HDD |
|---|---|---|---|
| Code + repo docs | working trees | **GitHub** + HDD | `git clone` |
| Budget data | Neon Postgres (cloud) | is itself offsite | reconnect via DATABASE_URL (Neon console) |
| Documents/media (`~/Documents`, Desktop) | local | **iCloud** (verified 204GB used) + HDD | re-sign-in to iCloud |
| Bank exports (`~/personal/finances/raw/`) | local | **HDD** | re-export from NAB (limited history!) |
| `~/personal` non-repo docs (health, Yuyjie, tax, family-history) | local | **HDD** (gap closed 2026-08-18) | BusinessMac holds family-history + finances copies |
| `~/projects/_archive` non-repo folders | local | **HDD** | git history holds pre-move copies of micko-kb-archive |
| Claude memory + settings (`~/.claude/`) | local | **HDD** | rebuildable from AGENTS.md files + this doc, but history lost |
| SSH keys, `~/.gitconfig` + `~/.gitconfig-personal` | local | **HDD** | regenerate keys, re-register on GitHub, recreate configs from Identity section |
| Photos library (~19GB) | local | **iCloud Photos** + HDD | — |
| Micko dev-DB harness evidence | `~/projects/micko/db-dumps/` (gitignored; copied off HDD 2026-08-18) | TM | optional; prod data lives in Neon once provisioned |
| App auth (gh keyring, vercel, claude) | local | n/a | re-login each CLI |
| Cloud routines, MCP connectors | claude.ai (cloud) | is itself offsite | reconnect at claude.ai |

## The backup HDD

4TB portable HDD, APFS container `disk5` on the **mini** (steady state — plugged into the mini, fleet TM destination). Volumes:
- `TM-mini` — mini's local Time Machine (encrypted, TM-formatted). First backup 2026-08-19.
- `TM-M5` — M5's Time Machine over the network: shared from the mini via SMB (`smb://sps@100.64.175.108/TM-M5`, over Tailscale), encrypted sparsebundle `Shane's MacBook Pro (2).sparsebundle`. First backup 2026-08-19 (19 GB).
- (`TM`, the 2026-08-18 files-only backup volume, was deleted 2026-08-19 once both TM lines had a completed backup.)

Mini-side share recipe (no GUI needed; `sps` has passwordless sudo via `/etc/sudoers.d/sps`; CC on the M5 has `Bash(ssh mini:*)` + `Bash(scp *mini:*)` allowed in `~/.claude/settings.json`, so it can drive the mini directly):
`sudo launchctl enable system/com.apple.smbd; sudo launchctl bootstrap system /System/Library/LaunchDaemons/com.apple.smbd.plist; sudo sharing -a /Volumes/TM-M5 -S TM-M5 -s 001 -g 000 -n TM-M5; sudo dscl . -create /SharePoints/TM-M5 dsAttrTypeNative:timemachine 1; sudo launchctl kickstart -k system/com.apple.smbd`
M5 side: mount `smb://sps@100.64.175.108/TM-M5` in Finder (remember in keychain) → TM pane → Add Backup Disk → TM-M5 → Encrypt.

Throughput: both Macs were on 2.4GHz 802.11n (~0.5 MB/s) at first backup; both moved to the 5G SSID 2026-08-19 (~8 MB/s). Wiring the mini (en0) would still be better.

## Identity & access inventory

- **GitHub `spschleger`** (personal) — email spschleger@gmail.com, SSH key `~/.ssh/id_ed25519`, host alias `github-personal` in `~/.ssh/config`.
- **GitHub `spsholdco`** (business) — email spsholdco@gmail.com, SSH key `~/.ssh/id_spsholdco`, default for github.com; `gh` CLI authed as this account.
- **`~/.gitconfig`**: global user = spsholdco; `includeIf gitdir/i:~/personal/` → `~/.gitconfig-personal` (spschleger).
- **Tailscale machines** (pruned 2026-08-19 to two): `m5` = this MacBook (100.89.24.13); `mini` = Mac mini (100.64.175.108, user **`sps`**, Apple ID spsholdco, aerial + Hermes-agent host, `sps` has passwordless sudo). `~/.ssh/config` has `mini` only (via `id_ed25519`). Old MacBook (`shanes-macbook-pro`, holdco) and `apc-agent` removed from the tailnet — re-add if the old Mac is ever needed as failover.

## Repo table (all pushed)

| Repo | Path | Remote |
|---|---|---|
| weekly-budget | `~/personal/finances/weekly-budget` | `github-personal:spschleger/weekly-budget` (origin); legacy copy at spsholdco |
| micko | `~/projects/micko` | `git@github.com:spsholdco/micko` |
| mysupercheck (Leapt, archived) | `~/projects/_archive/mysupercheck` | `git@github.com:spsholdco/mysupercheck` |

Non-repo but versioned elsewhere: `~/personal/family-history` (HDD + BusinessMac holdco account).

## Secrets (never in git — locations only)

- `weekly-budget/.env.local` — Neon DATABASE_URL (recoverable: Neon console)
- `~/projects/micko/.env` — Micko runtime env (see `.env.example` for shape; values from providers)
- Both included in the HDD backup.

## Software to reinstall (fresh-start cut, decided 2026-08-18)

- Homebrew, then: `gh git node poppler python@3.13` (postgresql@17 **dropped** — all DBs are cloud/Neon now)
- Casks (`brew install --cask`): `1password bluewallet chatgpt claude obsidian telegram visual-studio-code wechat wispr-flow` (Chrome, Tailscale were installed by hand pre-CC; 1Password 7 was replaced by the v8 cask 2026-08-18)
- npm globals: `vercel` only (openclaw/acpx/agent-browser **dropped** — OpenClaw era over; agent stack = Hermes on the mini)
- Apps: **1Password, BlueWallet, Chrome (+ Claude extension + `~/tools/x-tweet-newtab` unpacked — rebuilt 2026-08-19, now covered by TM; source in that folder), Claude, Claude Code, ChatGPT, Hermes Desktop, Obsidian (vaults = `~/personal` and `~/projects/micko/kb`), Tailscale, Telegram, VS Code, WeChat, Wispr Flow**
- Cut on rebuild: Astrill (was meant to be gone since July), Cursor, GarageBand, iMovie

## Backup layers (current state)

1. **HDD files backup** — done 2026-08-18 (see "The backup HDD" above). Pre-wipe safety net.
2. **GitHub** — all repos, push at session close (rule in each AGENTS.md).
3. **iCloud** — Documents/Desktop sync + Photos (2TB plan, 204GB used, verified 2026-08-18). One-shot `personal-mirror` from 2026-08-12 still in `~/Documents/` (contains `.env` files — delete post-rebuild if unwanted in iCloud).
4. **Time Machine → HDD on the mini** — LIVE 2026-08-19 for both Macs (mini local → `TM-mini`; M5 → `TM-M5` over SMB/Tailscale). See "The backup HDD". Daily iCloud mirror job: considered and **rejected 2026-08-18** (keep it simple; accepted same-premises risk — offsite = GitHub + iCloud + Neon only).
5. Micko production DB → Neon (cloud) with PITR once provisioned; no local dump job needed.

## Keeping this current

Regenerate the software lists (`brew leaves`, `brew list --cask`, `npm ls -g --depth=0`); re-copy to `~/Documents/` and the HDD after edits. Any session can be asked: "update MACHINE.md and re-copy to iCloud."

## Rebuild log — 2026-08-18

Fresh macOS → CC drove the rebuild from `TM/MACHINE.md` (copy on Desktop). Restored selectively from `TM/m5-backup-2026-08-18/`:
- `~/.ssh` (both keys, config, known_hosts; kept the mini's new `authorized_keys`), `~/.gitconfig` + `~/.gitconfig-personal` — both GitHub identities + `ssh mini` verified.
- `~/personal`, `~/projects` (excl. `.next`/`node_modules`) — all 3 repos clean at HEAD, `.env` files present.
- `~/.claude`: `projects/` (memory + old sessions), `plugins/`, `settings.json`, `settings.local.json`, plans/file-history/backups, prompt history merged. `~/.claude.json` (login) left fresh. `~/.cache/plugins` restored for the vercel marketplace.
- **Deliberately not restored:** old `.zshrc` (OpenClaw-era API keys + completion), `.openclaw/`, `.cursor/`, `.codex/`, `.copilot/`, `.bun/`, `.playwright-mcp/`, `.agent-browser/`, old `Library/`. Clean `.zshrc`/`.zprofile` written (PATH + brew shellenv only).
- Installed: Homebrew 6, `gh git node poppler python@3.13`, 8 casks, `vercel` (npm -g).
- Gap found: `~/tools/x-tweet-newtab` was never in the backup.
- Post-rebuild done same night: `gh auth login` (spsholdco, https protocol; remotes stay SSH), `vercel login`; HDD moved to the mini; `TM-mini` + `TM-M5` volumes; mini SMB share + first backups on both Macs (2026-08-19); tailnet pruned + renamed (`m5`, `mini`); 1Password 7 → 8; micko `db-dumps/` gitignored + pushed.
- 2026-08-19: `TM` volume deleted; both Macs on 5G WiFi; tailnet = `m5` + `mini`; CC allowed `ssh mini`. Still open: Obsidian vaults re-open; Chrome + Claude extension; optionally delete `~/Documents/personal-mirror` (has `.env` files).
- 2026-08-25: Hermes Desktop v0.20.5 installed on the M5 and connected to Max on the mini through its `ssh mini` tailnet route. The connection starts a loopback-only remote backend on demand; no mini port is exposed. Homebrew `ripgrep` and `ffmpeg` installed for the local runtime.
