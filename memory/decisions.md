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
