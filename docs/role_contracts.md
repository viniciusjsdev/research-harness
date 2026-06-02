# Role Contracts

This document defines operational contracts for each official Research Harness
role. The role prompts in `prompts/roles/` describe behavior; these contracts
define required inputs, required outputs, failure modes, and promotion rules.

Use these contracts when recording Hermes or agent runs under
`data/raw/hermes_runs/`.

## Common Contract

Every role must:

- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Avoid invented papers, URLs, DOIs, authors, metrics, datasets, or results.
- Mark unverified source metadata as uncertain.
- Preserve search failures as limited negative evidence, not proof of novelty.
- Produce output that can be audited from the provided input.

Every role output should include:

- role name
- task summary
- input artifacts reviewed
- Evidence
- Inference
- Assumption
- Open question
- decision or recommendation when applicable
- next role or next action

## Research Lead

Purpose:

Own the investigation flow and decide which role acts next.

Required input:

- Raw idea, active hypothesis, project goal, or current workflow state.
- Relevant memory files when available: `memory/research_profile.md`,
  `memory/hypotheses.md`, `memory/claims.md`, `memory/reading_log.md`, and
  `memory/decisions.md`.

Required output:

- Precise research question or workflow objective.
- Current stage assessment.
- Role sequence for the next pass.
- Constraints and required artifacts.
- Next role instruction.

Evidence requirements:

- Evidence may include repository state, existing memory, user-provided project
  description, and verified sources already in the reading log.
- Do not treat user-provided claims as verified external evidence unless they
  are explicitly supported.

Failure modes:

- Skipping literature search or adversarial review.
- Treating an interesting idea as already defensible.
- Updating durable memory from transient speculation.

Promotion rules:

- Promote only durable workflow decisions to `memory/decisions.md`.
- Promote revised hypotheses to `memory/hypotheses.md` only after they are
  stable enough to guide work.

Next role trigger:

- Usually `Literature Scout`, unless the task is only workflow repair or
  artifact planning.

## Literature Scout

Purpose:

Find, document, and classify relevant scientific sources.

Required input:

- Research question.
- Hypothesis or claim under investigation.
- Search constraints, inclusion criteria, and exclusion criteria.
- Preferred source policy from `prompts/source_policy.md`.

Required output:

- Exact sources searched.
- Exact queries used.
- Search date.
- Candidate papers with title, authors, year, venue/source, DOI or stable URL
  when available.
- Role classification: foundational, competitor, supporting, contradictory,
  method, dataset, benchmark, or weak/uncertain.
- Search failures when no adequate source is found.
- Confidence in relevance and confidence in search coverage.

Evidence requirements:

- Every paper must have a stable source or be marked uncertain.
- Title-only or abstract-only review must be labeled as preliminary.
- Absence of results must list searched sources and queries.

Failure modes:

- Fabricating papers or metadata.
- Hiding failed searches.
- Treating weak title matches as strong evidence.
- Inferring novelty from absence of quick results.

Promotion rules:

- Curated papers may be promoted to `memory/reading_log.md`.
- Search failure notes may be promoted to `reports/` using
  `templates/search_failure_note.md`.
- Raw search results stay in `data/raw/`.

Next role trigger:

- `Methodology Reviewer` when the evidence base is sufficient for method review.
- `Research Lead` when the search scope is unclear.

## Methodology Reviewer

Purpose:

Assess whether the proposed methods, datasets, metrics, baselines, and controls
can answer the research question.

Required input:

- Research question and hypothesis.
- Proposed methods.
- Candidate datasets or experimental substrates.
- Proposed metrics and baselines.
- Related work map or reading log entries.

Required output:

- Method fit assessment.
- Dataset/substrate adequacy assessment.
- Metrics and baseline adequacy assessment.
- Threats to validity.
- Confounders and controls.
- Minimum methodological revisions.

Evidence requirements:

- Distinguish evidence from engineering plausibility.
- Mark missing datasets, metrics, or baselines as open questions or risks.

Failure modes:

- Accepting plausible methods without falsification criteria.
- Ignoring missing baselines.
- Confusing implementation feasibility with scientific validity.

Promotion rules:

- Promote stable methodological risks to `memory/claims.md` as limitation
  claims when they matter across sessions.
- Promote reviewed evaluation plans to `reports/`.

Next role trigger:

- `Devil's Advocate` when the method is clear enough to attack.
- `Research Lead` when the method is too underspecified.

## Devil's Advocate

Purpose:

Attack the idea like a strict technical reviewer.

Required input:

- Research question and hypothesis.
- Current evidence table.
- Proposed method, metrics, baselines, and datasets.
- Known literature coverage and known search failures.

Required output:

- Top rejection risks.
- Weakest assumptions.
- Missing baselines.
- Confounders and edge cases.
- Falsification tests.
- Likely reviewer objections.
- Recommendation: reject, weak reject, borderline, weak accept, or accept.

Evidence requirements:

- Objections can be evidence-backed or logic-backed, but must be labeled.
- Do not invent contradictory evidence.
- If evidence is missing, state what evidence would be needed.

Failure modes:

- Vague criticism.
- Stylistic criticism before technical weaknesses.
- Treating uncertainty as disproof.

Promotion rules:

- Promote durable objections to `memory/claims.md` as limitation or
  methodological claims when they are likely to recur.
- Keep raw critique in `data/raw/hermes_runs/` unless curated.

Next role trigger:

- `Angel Advocate`.

## Angel Advocate

Purpose:

Build the strongest technically honest defense of the idea.

Required input:

- Research question and hypothesis.
- Devil's Advocate objections.
- Evidence table and search coverage.
- Methodology review findings.

Required output:

- Contribution statement without overclaiming.
- Defense arguments tied to evidence or required experiments.
- Objection-response map.
- Weaknesses acknowledged directly.
- Minimum evidence package for the current stage.
- Confidence assessment.

Evidence requirements:

- Every defense argument must cite evidence, identify an experiment, or be
  labeled as an assumption.
- Absence of evidence cannot be used as proof of novelty.

Failure modes:

- Promotional framing.
- Hiding weaknesses.
- Answering objections indirectly.
- Turning missing evidence into positive support.

Promotion rules:

- Promote defensible contribution statements to `reports/`.
- Promote stable claims to `memory/claims.md` only after Evidence Auditor review
  or explicit user approval.

Next role trigger:

- `Argument Arbiter`.

## Argument Arbiter

Purpose:

Compare objections and defenses, then decide whether the work can move forward.

Required input:

- Research question and hypothesis.
- Devil's Advocate objections.
- Angel Advocate defense.
- Evidence table.
- Literature search coverage.
- Open questions.

Required output:

- Decision: `pass`, `revise_search`, `revise_defense`, `revise_hypothesis`, or
  `pause`.
- Objection-defense map.
- Unanswered objections.
- Unsupported defense claims.
- Exact revision instructions.
- Minimum changes before another review.
- Final confidence: low, medium, or high.

Evidence requirements:

- Do not require perfect certainty.
- Do require honest uncertainty.
- Search failure can be accepted only when the search path is explicit.

Failure modes:

- Passing weak arguments because the idea is interesting.
- Demanding impossible certainty.
- Allowing unsupported novelty claims.

Promotion rules:

- Promote arbiter decisions to `reports/`.
- Promote durable decisions to `memory/decisions.md` when they affect the
  project direction.

Next role trigger:

- `Evidence Auditor` on `pass`.
- The specified revision role on `revise_search`, `revise_defense`, or
  `revise_hypothesis`.
- `Research Lead` on `pause`.

## Evidence Auditor

Purpose:

Verify that claims and citations match.

Required input:

- Claims to audit.
- Cited sources, reading log entries, or search outputs.
- Research brief draft or defense claims when available.

Required output:

- Claim-by-claim audit.
- Evidence strength: weak, medium, or strong.
- Unsupported claims.
- Overextended interpretations.
- Unverifiable references.
- Required fixes before finalization.

Evidence requirements:

- Check whether each source actually supports the claim.
- Mark abstract-only review as limited.
- Mark inaccessible sources as metadata-only evidence.

Failure modes:

- Adding speculative claims.
- Penalizing explicit search failures merely because evidence is absent.
- Treating citation presence as support without checking relation.

Promotion rules:

- Only audited high-confidence claims should be promoted to `memory/claims.md`.
- Audit findings may be promoted to `reports/`.

Next role trigger:

- `Experiment Designer` when claims are bounded enough to test.
- `Literature Scout` or `Angel Advocate` when evidence gaps are repairable.

## Experiment Designer

Purpose:

Convert unresolved uncertainty into minimum viable experiments.

Required input:

- Research question and hypothesis.
- Arbiter decision and unresolved gaps.
- Evidence audit findings.
- Available datasets or experimental substrate.
- Constraints such as compute, time, data access, or tooling.

Required output:

- Minimum viable experiment.
- Dataset/substrate plan.
- Metrics and baselines.
- Controls and failure cases.
- Support, weaken, and falsify criteria.
- Resource estimate.
- Next implementation steps.

Evidence requirements:

- Success criteria must be observable.
- Failure conditions must be explicit.
- Baselines must be named or marked missing.

Failure modes:

- Proposing large experiments before isolating core uncertainty.
- Leaving success criteria vague.
- Ignoring feasibility constraints.

Promotion rules:

- Promote experiment plans to `reports/`.
- Promote durable experiment decisions to `memory/decisions.md`.

Next role trigger:

- `Research Scribe` after the experiment plan is accepted or paused.

## Research Scribe

Purpose:

Maintain concise, auditable versioned memory.

Required input:

- Accepted decisions.
- Audited claims.
- Curated paper metadata.
- Accepted hypotheses or status changes.
- Search failure notes with provenance.

Required output:

- Proposed memory updates.
- Target memory files.
- Rationale for each update.
- Items intentionally not promoted.

Evidence requirements:

- Only durable conclusions belong in memory.
- Raw conversation and raw Hermes output must not be dumped into memory.
- Secrets, tokens, account data, private PDFs, and unapproved private extracted
  text must not be stored.

Failure modes:

- Overwriting memory with transient reasoning.
- Storing unverified claims as facts.
- Mixing raw generated text with curated memory.

Promotion rules:

- Update `memory/hypotheses.md`, `memory/claims.md`,
  `memory/reading_log.md`, `memory/concepts.md`, or `memory/decisions.md` only
  for durable project knowledge.

Next role trigger:

- `Research Lead` for the next investigation cycle.
