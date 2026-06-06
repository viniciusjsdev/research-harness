# Hermes Audit Checklist

Use this checklist when reviewing Hermes outputs, role/profile assignments, tool
use, generated skills, or proposed repository changes.

## Scope

This checklist audits Hermes behavior inside this research harness. It does not
replace `AGENTS.md`, `docs/role_contracts.md`, or `prompts/source_policy.md`.

## Run Trace

- A run folder exists under `data/raw/hermes_runs/run-YYYYMMDD-HHMMSS[-slug]/`.
- `00_metadata.json` states the purpose, operator, Hermes session mode, and role
  statuses.
- Each activated role/profile has its own `input/`, `output/`, and `artifacts/`
  folders.
- Completed roles have captured input and output files created during the run.
- The run does not rely on a retrospective consolidated log copied into profile
  folders after the fact.
- Raw run material stays in `data/raw/hermes_runs/` until explicitly reviewed.

## Role Discipline

- Hermes uses official role names from `docs/nomenclature.md`.
- The role output satisfies the matching contract in `docs/role_contracts.md`.
- The output separates `Evidence`, `Inference`, `Assumption`, and
  `Open question` when making substantive claims.
- The next role or next action is explicit.
- `Argument Arbiter` uses only `pass`, `revise_search`, `revise_defense`,
  `revise_hypothesis`, or `pause`.

## Source Discipline

- Literature searches follow `prompts/source_policy.md`.
- Sources searched, exact queries, search date, inclusion criteria, and
  confidence are recorded.
- Papers have stable metadata or are marked uncertain.
- Abstract-only or metadata-only review is labeled as limited.
- Search failure is treated as limited negative evidence, not proof of novelty.
- No paper, DOI, URL, author, metric, dataset, or result is invented.

## Tool And Action Audit

- Claimed tool use matches observable terminal output, saved files, or documented
  source results.
- File edits are verified with `git diff` or direct file inspection.
- Hermes does not claim access to unavailable tools or private context.
- Hermes does not edit files or promote artifacts unless that was part of the
  approved task.
- Shell quoting or operator mistakes are recorded as operator issues, not Hermes
  failures.

## Skill Quality

- A generated skill has a specific trigger condition and clear non-goals.
- The skill is domain-agnostic unless the user requested a domain-specific skill.
- The workflow is executable with existing repo files, scripts, prompts, or
  schemas.
- The skill preserves source discipline and role nomenclature.
- The skill does not hide weak evidence, missing baselines, or missing datasets.
- The skill avoids duplicating existing docs unless it adds operational value.

## Promotion Readiness

- The artifact's destination is one of `reports/`, `memory/`, `skills/`,
  `prompts/`, or `schemas/`.
- The promotion rationale is recorded in the run metadata or output review.
- Durable memory updates are concise, audited, and not raw conversation dumps.
- High-confidence claims have been checked by `Evidence Auditor` or explicitly
  approved by the user.
- Diagnostics include `Evidence`, `Inference`, `Assumption`, `Open question`,
  and `Remediation`.

## Stop Conditions

Pause the refinement loop when:

- The same failure repeats after two prompt or workflow revisions.
- Hermes repeats broad suggestions without new evidence.
- A proposed structural change needs user judgment.
- Remaining issues are cosmetic rather than audit or correctness risks.
