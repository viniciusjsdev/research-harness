# Decisions

Record durable decisions here. Keep entries short and auditable.

## DEC-0001: Separate Hermes Runtime From Project Harness

Date: 2026-05-31

Decision:
Keep Hermes Agent installed outside the repository. Version only the research harness assets in this repo.

Rationale:
Hermes contains runtime configuration, auth state, sessions, and machine-specific paths. The harness should remain portable and safe to commit.

Consequences:

- Tokens and Hermes auth files stay outside Git.
- Project memory in `memory/` is versioned.
- Hermes can later run from the repo root and use these files.

## DEC-0002: Use Role-Based Argument Review Loop

Date: 2026-06-01

Decision:
Use explicit research roles: Research Lead, Literature Scout, Methodology Reviewer, Devil's Advocate, Angel Advocate, Argument Arbiter, Evidence Auditor, Experiment Designer, and Research Scribe.

Rationale:
Research ideation needs competing lenses. The harness should not only defend ideas; it should attack them, build the best honest defense, and then compare both sides before moving forward.

Consequences:

- The Argument Arbiter can send work back to search, defense, or hypothesis revision.
- The final output does not need perfect certainty.
- The final output must have a solid, honest argumentative base.

## DEC-0003: Treat Search Failure As Limited Negative Evidence

Date: 2026-06-01

Decision:
When preferred sources do not reveal directly related work, record the failed search as limited negative evidence only if sources, queries, date, inclusion criteria, and confidence are documented.

Rationale:
This helps identify possible novelty without allowing the model to hallucinate citations or defend a thesis from absence alone.

Consequences:

- Absence of results can support a "possible gap" claim.
- Absence of results cannot prove novelty.
- Literature Scout and Evidence Auditor must preserve search provenance.

## DEC-0004: Accept Missing Literature As A First-Class Finding

Date: 2026-06-01

Decision:
The harness should accept "no adequate articles found" as a valid finding when the search was documented with sources, queries, date, criteria, and confidence.

Rationale:
Scientific reasoning should not force evidence where none was found. A missing evidence base can be useful for identifying gaps, weakening claims, or motivating experiments.

Consequences:

- The system must explicitly state where it searched and where it failed.
- The system must not hallucinate papers to defend a thesis.
- Missing literature can move the project forward only with honest uncertainty and clear follow-up.

## DEC-0005: Standardize Role Nomenclature

Date: 2026-06-01

Decision:
Use official role names and decision labels from `docs/nomenclature.md`.

Rationale:
The project is educational and should make the harness concepts easy to learn. Stable terminology also prevents the workflow from mixing vague "personalities" with technical roles.

Consequences:

- Use `Angel Advocate`, not generic defense agent, for the pro-hypothesis role.
- Use `Devil's Advocate` for the adversarial reviewer role.
- Use `Argument Arbiter` for the gatekeeper that compares attack and defense.
- Use `Search failure` for documented absence of adequate evidence.

## DEC-0006: Keep The Harness Domain-Agnostic

Date: 2026-06-02

Decision:
Treat each user-supplied research objective as a temporary object of analysis, not as the permanent identity of the repository.

Rationale:
The repository exists to let Hermes receive many different research ideas and dissect them with the same cold, structured method. Attaching the harness to one domain would bias later analyses and weaken the role-based review loop.

Consequences:

- `AGENTS.md` carries the operating contract for any Hermes instance launched in this repository.
- `memory/research_profile.md` records the stable project identity as domain-agnostic.
- Domain-specific conclusions belong in reports, hypothesis notes, reading logs, or decision entries only when they are durable and explicitly scoped.
- Future Hermes sessions should not assume the current research idea is the main project.

## DEC-0007: Version Role Input/Output Logs

Date: 2026-06-02

Decision:
For each harness run, store the visible input and output of every activated role/profile under `data/raw/hermes_runs/<run-id>/profiles/<role>/{input,output,artifacts}/`.

Rationale:
The user needs role-level traces to analyze and improve Harness behavior across many research objectives. Without per-role input/output records, later review cannot distinguish whether failures came from the initial framing, a specific role prompt, weak evidence, poor arbitration, or final synthesis.

Consequences:

- Each run should create or update one run directory in `data/raw/hermes_runs/`.
- Each activated role/profile should have its own `input/`, `output/`, and `artifacts/` subdirectories.
- Role outputs should preserve `Evidence`, `Inference`, `Assumption`, and `Open question` labels when they appear.
- If a role was used only implicitly or retrospectively, its profile output must say so instead of pretending an exact transcript exists.
- Final reports in `reports/` may summarize results, but `data/raw/hermes_runs/` is the audit trail for Harness behavior.

## DEC-0008: Revise Fine-Tuning Versus Harness Framing

Date: 2026-06-07

Decision:
Revise the research framing that compares Fine-Tuning and Harness for financial-industrial correlation analysis. Treat Harness as an auditable methodological layer and Fine-Tuning as a possible auxiliary component for labeled subtasks, not as a direct alternative to Harness.

Rationale:
The Hermes run `run-20260607-200637-fine-tuning-vs-harness-industrial-financial` reached `revise_hypothesis`. The Argument Arbiter found that the original framing compared non-equivalent categories. The Evidence Auditor found no support for superiority or novelty claims.

Consequences:

- Do not claim that Harness is superior to Fine-Tuning for this task without an experiment.
- Do not claim novelty from the absence of direct papers in the searched artifacts.
- Future work must include statistical/BI baselines without LLM.
- Fine-Tuning should be evaluated only when a concrete labeled subtask exists.
- Validity of correlations and auditability of workflow must be measured separately.
