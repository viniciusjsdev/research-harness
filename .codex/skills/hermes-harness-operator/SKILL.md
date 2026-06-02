---
name: hermes-harness-operator
description: Operate Hermes Agent from Codex inside this research-harness repository. Use when the user asks Codex to interact with Hermes, relay tasks to Hermes, inspect Hermes outputs, diagnose Hermes misunderstandings, or implement files only after the user explicitly says Codex should create what Hermes cannot create.
---

# Hermes Harness Operator

## Overview

Use this skill to coordinate Codex with Hermes Agent for this repository. Hermes is treated as an external research/skill-generation agent; Codex is the operator that launches Hermes, relays user-approved tasks, inspects results, and records failure diagnostics.

## Operating Contract

- Do not invent Hermes outputs. If Hermes did not produce something, say so.
- Do not create project artifacts from Hermes suggestions unless the user explicitly asks Codex to create them.
- Do not bias Hermes with domain examples unless the user asks for a domain-specific test.
- Keep Hermes prompts short, visible, and aligned with the user's current instruction.
- If Hermes misunderstands, over-specializes, ignores constraints, edits unexpectedly, or produces weak skill content, report the failure in a diagnostic markdown file.

## Launch Hermes

The configured Hermes home for this machine is:

```bash
$HOME/Hermes/.hermes
```

From Windows/Codex, open Hermes in the harness with:

```powershell
wsl.exe bash -lc 'export HERMES_HOME="$HOME/Hermes/.hermes"; cd /mnt/d/Projetos/Github_ViniciusJ/research-harness && hermes'
```

For quick checks:

```powershell
wsl.exe bash -lc 'export HERMES_HOME="$HOME/Hermes/.hermes"; cd /mnt/d/Projetos/Github_ViniciusJ/research-harness && hermes --version'
```

If `HERMES_HOME` is omitted, Hermes may use `~/.hermes` instead of `~/Hermes/.hermes` and report that no provider is configured.

## Interaction Workflow

1. Restate the user's requested Hermes task in one or two sentences.
2. Ask Hermes only for the requested artifact or reasoning step.
3. If using interactive Hermes, tell the user the exact prompt to paste or run Hermes with the launch command above.
4. If using non-interactive Hermes, keep the prompt short and avoid complex quoting; prefer direct one-line prompts.
5. Inspect the Hermes output against the user's constraints and `AGENTS.md`.
6. If Hermes suggests code or files, wait for explicit user instruction before Codex creates or edits them.
7. If the user explicitly asks Codex to create files Hermes cannot create, implement them using normal Codex repo-editing rules.

## Diagnostic Reporting

When Hermes fails or partially fails, create or update a diagnostic markdown file in `reports/`, such as:

```text
reports/hermes_diagnostics.md
```

Use this structure:

```markdown
# Hermes Diagnostics

## <Date> - <Short Failure Name>

Evidence:

- What Hermes was asked.
- What Hermes returned or did.
- Relevant command/output excerpt.

Inference:

- Why this is a failure or risk.

Assumption:

- Any uncertain cause.

Open question:

- What would reduce uncertainty.

Remediation:

- Prompt change, workflow change, or repo change to consider.
```

Do not treat shell quoting failures or Codex operator mistakes as Hermes failures. Label those as Codex/operator failures if they matter.

## Known Local Pitfalls

- `hermes` opens correctly only when `HERMES_HOME="$HOME/Hermes/.hermes"` is set in this environment.
- WSL prints path translation warnings for old Windows Python paths under `E:\Linguagens\Python\...`; these warnings are noisy but did not prevent Hermes from launching.
- Interactive Hermes may show "Input is not a terminal" if launched through a non-interactive Codex shell with a timeout. That proves launchability, not a usable interactive session.
- Long prompts through `wsl.exe` can fail because of PowerShell/Bash quoting. Prefer short prompts or ask the user to paste the prompt into the interactive Hermes terminal.
