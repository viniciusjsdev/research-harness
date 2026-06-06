# Research Ideation Skill

Use this skill when developing, testing, attacking, or defending a new scientific R&D idea.

Use official terminology from `docs/nomenclature.md`.

## Inputs

- A raw idea, hypothesis, domain, paper list, or technical question.
- Optional constraints such as available compute, available data, target venue, or product context.

## Workflow

1. Read `memory/research_profile.md`, `memory/hypotheses.md`, `memory/claims.md`, and `memory/reading_log.md`.
2. Convert the raw idea using `prompts/new_idea.md`.
3. Use `prompts/roles/research_lead.md` to plan the investigation.
4. Use `prompts/roles/literature_scout.md` and `prompts/source_policy.md` to generate literature queries and run or request `scripts/search_literature.py`.
5. Curate only meaningful papers into `memory/reading_log.md`.
6. Use `prompts/roles/methodology_reviewer.md` to assess methods, metrics, datasets, and baselines.
7. Run Devil's Advocate review with `prompts/roles/devil_advocate.md` and `prompts/devil_advocate.md`.
8. Run Angel Advocate defense construction with `prompts/roles/angel_advocate.md` and `prompts/defense_brief.md`.
9. Use `prompts/roles/argument_arbiter.md` and `prompts/argument_review_loop.md` to decide whether to pass or revise.
10. If the arbiter returns `revise_search`, `revise_defense`, or `revise_hypothesis`, send the work back to the specified role and repeat the review loop.
11. Use `prompts/roles/evidence_auditor.md` before finalizing high-confidence claims.
12. Use `prompts/roles/experiment_designer.md` to define the minimum viable experiment.
13. Create or update a brief from `templates/research_brief.md`.
14. Use `prompts/roles/research_scribe.md` to record durable decisions in `memory/decisions.md`.

## Quality Rules

- Do not treat search results as validated papers until metadata is checked.
- Do not infer novelty from absence of quick search results.
- Treat well-documented failure to find related work as limited negative evidence, not proof of novelty.
- Accept absence of articles as a valid intermediate or final finding when the searched sources, queries, and failures are explicit.
- Every defense argument should have either evidence or a named experiment that could produce evidence.
- Every high-confidence claim must cite a stable source.
- The final brief does not need perfect certainty, but it must not rely on known holes that could be repaired by another search or defense pass.
- Keep project memory concise and curated.

## Output Style

Prefer:

- concise technical summaries
- tables for paper comparison
- explicit confidence labels
- short decision records

Avoid:

- broad inspirational language
- unsupported novelty claims
- long unstructured summaries
