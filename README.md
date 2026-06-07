# Research Harness

Research Harness is a versioned workspace for early-stage scientific R&D. It is designed to help an agent or human researcher turn a rough idea into a structured research brief with hypotheses, literature search, adversarial critique, defense points, and next experiments.

Hermes Agent is the intended runtime/orchestrator, but this repository does not require Hermes to be installed in order to evolve the project assets.

## Goals

- Capture durable research memory in versioned files.
- Analyze new research ideas through a repeatable workflow.
- Search and compare related papers with explicit evidence.
- Separate facts, citations, claims, assumptions, and inferences.
- Produce technical briefs that can survive adversarial review.

## Core Nomenclature

The project uses a few terms precisely:

- Harness: the structured research environment around the agent.
- Runtime: the tool that executes the workflow, such as Hermes Agent.
- Versioned memory: durable project knowledge stored in `memory/`.
- Role: a technical lens used during the workflow.
- Search failure: a documented failure to find adequate evidence in searched sources.

See [docs/nomenclature.md](docs/nomenclature.md) for the full glossary.

## Repository Layout

```text
memory/      Versioned project memory: ideas, decisions, claims, reading log.
prompts/     Reusable prompt contracts for each workflow step.
schemas/     JSON Schemas for structured research artifacts.
scripts/     Local helpers for literature search and PDF ingestion.
skills/      Agent skills/instructions, including Hermes-oriented workflows.
templates/   Report and brief templates.
papers/      Local PDF workspace. Raw PDFs are ignored by Git by default.
reports/     Curated reports and research briefs.
data/        Generated search and extraction data. Ignored by default.
tests/       Future tests for scripts and schema validation.
```

Hermes input/output traces should be stored by run under
`data/raw/hermes_runs/` using the convention in
[docs/hermes_run_logging.md](docs/hermes_run_logging.md). Raw traces stay
ignored by Git; only reviewed artifacts are promoted to `reports/`, `memory/`,
`skills/`, `prompts/`, or `schemas/`.

Role-specific input/output contracts are defined in
[docs/role_contracts.md](docs/role_contracts.md).

## What Gets Versioned

Commit durable, reviewable project assets:

- prompts
- schemas
- agent skills
- curated research memory
- curated reports
- scripts
- documentation

Do not commit:

- Hermes tokens or auth files
- `.env` with secrets
- private PDFs
- generated caches
- raw extracted text from private PDFs unless explicitly approved

## Suggested Workflow

1. Add or update the research idea in `memory/hypotheses.md`.
2. Run the `new_idea` prompt to break the idea into assumptions, claims, keywords, and risks.
3. Use `scripts/search_literature.py` to gather candidate papers.
4. Curate useful papers into `memory/reading_log.md`.
5. Run Devil's Advocate to attack the hypothesis.
6. Run Angel Advocate to build the strongest honest defense.
7. Run Argument Arbiter to compare objections and defenses.
8. If the arbiter finds avoidable holes, return to literature search, defense, or hypothesis revision.
9. Produce a research brief with `templates/research_brief.md`.
10. Record major decisions in `memory/decisions.md`.

## Official Roles

The harness uses role prompts rather than free-form personality. Each role is a technical lens:

| Role | Purpose |
| --- | --- |
| Research Lead | Owns the investigation flow and decides the next role. |
| Literature Scout | Searches scientific sources and records search provenance. |
| Methodology Reviewer | Reviews methods, metrics, datasets, baselines, and validity. |
| Devil's Advocate | Attacks the hypothesis like a strict reviewer. |
| Angel Advocate | Builds the strongest technically honest defense. |
| Argument Arbiter | Compares attack and defense, then passes or sends the work back. |
| Evidence Auditor | Verifies that claims are supported or explicitly marked as missing. |
| Experiment Designer | Converts uncertainty into minimum viable experiments. |
| Research Scribe | Updates versioned memory with durable conclusions. |

The Argument Arbiter is the gatekeeper. It does not require a perfect final answer, but it sends the work backward when the defense has avoidable holes or unsupported claims.

## Argument Review Loop

The main loop is:

```text
Research Lead
  -> Literature Scout
  -> Methodology Reviewer
  -> Devil's Advocate
  -> Angel Advocate
  -> Argument Arbiter
      -> pass
      -> revise_search
      -> revise_defense
      -> revise_hypothesis
      -> pause
  -> Evidence Auditor
  -> Experiment Designer
  -> Research Scribe
```

## Source Discipline

The literature workflow searches preferred academic sources first, including OpenAlex, Semantic Scholar, arXiv, Crossref, PubMed or Europe PMC for biomedical work, ACL Anthology for NLP, and official publisher/venue/dataset/code pages when relevant.

If no directly relevant work is found, that is recorded as a limited search finding with sources, queries, date, inclusion criteria, and confidence. It is not treated as proof of novelty.

This absence of evidence can still be useful. The harness should say exactly where it searched and where it failed, then use that fact honestly: as a possible gap, a weakness in the defense, or a reason to design a new experiment.

## CLI Usage Without Hermes

Install local helper dependencies:

```powershell
pip install -r requirements.txt
```

Search OpenAlex and arXiv:

```powershell
python scripts/search_literature.py --query "retrieval augmented generation scientific literature review" --limit 10
```

Extract text from PDFs:

```powershell
python scripts/ingest_pdf.py papers/inbox --out data/processed/pdf_text
```

## Hermes Runtime Setup

Hermes Agent is the intended runtime/orchestrator, but it should stay outside
this repository. For Windows machines where drive C should be avoided, install
Hermes on drive D and set `HERMES_HOME` / `HERMES_INSTALL_DIR` as described in
[docs/runtime_requirements.md](docs/runtime_requirements.md).

After Hermes is installed and authenticated, run it from the repository root:

```powershell
cd D:\Projetos\Github_ViniciusJ\research-harness
hermes
```

Or from WSL:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes
```

The agent should read `AGENTS.md`, use the prompts and schemas in this repo, and update the versioned memory files when a research decision becomes durable.
