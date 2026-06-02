# Hermes Run Logging

Use this convention to preserve auditable input/output traces from Hermes while
keeping raw generated material out of Git by default.

Role-specific input/output expectations are defined in
`docs/role_contracts.md`.

## Purpose

Hermes can produce useful intermediate reasoning, role outputs, skill drafts,
and critiques. The harness should keep these traces separate from curated
project memory.

This prevents three common failures:

- losing what each role or profile actually received as input
- promoting rough Hermes output into durable memory too early
- mixing raw generated text with reviewed reports, schemas, prompts, or skills

## Storage Rules

Raw Hermes traces go under:

```text
data/raw/hermes_runs/
```


Each Hermes run gets a timestamped run directory:

```text
data/raw/hermes_runs/run-YYYYMMDD-HHMMSS/
```

Inside a run directory, store one folder per role/profile. The official term in
the harness is `Role`, but the run directory uses `profiles/` because Hermes may
run one role through one or more local profiles.

```text
data/raw/hermes_runs/run-YYYYMMDD-HHMMSS/
  00_metadata.json
  profiles/
    01_research_lead/
      input/
        prompt.md
        context.md
      output/
        response.md
        codex_review.md
      artifacts/
    02_literature_scout/
      input/
      output/
      artifacts/
    03_methodology_reviewer/
      input/
      output/
      artifacts/
    04_devils_advocate/
      input/
      output/
      artifacts/
    05_angel_advocate/
      input/
      output/
      artifacts/
    06_argument_arbiter/
      input/
      output/
      artifacts/
    07_evidence_auditor/
      input/
      output/
      artifacts/
    08_experiment_designer/
      input/
      output/
      artifacts/
    09_research_scribe/
      input/
      output/
      artifacts/
```

Only create files for roles that actually ran. It is acceptable to create empty
role/profile directories from the template, but do not fabricate missing role
outputs.

Use the checked-in template directory at:

```text
data/raw/hermes_runs/_template/
```

Copy it when starting a new auditable Hermes run, then fill only the inputs,
outputs, reviews, and artifacts that actually occur.

## Folder Semantics

Use each profile folder consistently:

- `input/`: prompts, context packets, constraints, role contracts, and any
  material sent to Hermes before the profile acted.
- `output/`: raw Hermes response, Codex review of the response, and any explicit
  promotion/discard decision.
- `artifacts/`: files produced by the profile during that run before they are
  reviewed or promoted.

Do not store secrets, credentials, private account data, raw private PDFs, or
unapproved private extracted text in any run folder.

## Promotion Rules

Raw run files are evidence of process, not curated conclusions.

Promote only reviewed material:

| Raw material | Curated destination |
| --- | --- |
| Skill draft | `skills/<skill-name>/SKILL.md` |
| Research brief | `reports/` |
| Durable project decision | `memory/decisions.md` |
| Durable hypothesis update | `memory/hypotheses.md` |
| Durable claim | `memory/claims.md` |
| Curated paper metadata | `memory/reading_log.md` |
| Search failure | `reports/` or `templates/search_failure_note.md` instance |
| Harness prompt improvement | `prompts/` |
| Harness data contract | `schemas/` |

Before promotion, check:

- Evidence is separated from Inference, Assumption, and Open question.
- Citations, URLs, DOIs, metrics, and named results are verified or marked
  uncertain.
- Search failures include sources, queries, date, criteria, and confidence.
- The role output satisfies the relevant contract in `docs/role_contracts.md`.
- The promoted artifact follows the relevant schema/template where available.

## Metadata

Every run should include `00_metadata.json` based on
`templates/hermes_run_metadata.json`.

Required fields:

- `run_id`
- `created_at`
- `workspace`
- `operator`
- `hermes_session`
- `purpose`
- `roles`
- `artifacts_promoted`
- `notes`

Role entries in `00_metadata.json` should point to the role/profile folders,
not just flat files.

## Diagnostics

If Hermes misunderstands a prompt, ignores constraints, edits unexpectedly,
over-specializes a supposedly generic skill, or produces weak methodology,
record the issue in:

```text
reports/hermes_diagnostics.md
```

Diagnostics should include:

- Evidence
- Inference
- Assumption
- Open question
- Remediation

Do not label Codex shell/quoting mistakes as Hermes failures.

## Git Policy

`data/raw/hermes_runs/` is for raw generated traces and remains ignored by Git.
Only the directory marker and `_template/` are versioned so the convention is
visible.

Curated artifacts belong in versioned directories such as `reports/`, `skills/`,
`prompts/`, `schemas/`, and `memory/`.

## Anti-Retrospective-Copy Rule

Do not satisfy per-profile logging by copying a consolidated role log into profile folders after the fact. A copied retrospective reconstruction may be labeled for diagnostics, but it is not a valid role/profile capture. Valid runs create or update each existing profile folder under `data/raw/hermes_runs/<run-id>/profiles/` as that role executes.
