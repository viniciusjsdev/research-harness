# Prompt: Argument Review Loop

Use this prompt after Devil's Advocate and Angel Advocate have produced their arguments.

## Objective

Decide whether the research idea has a solid enough argumentative and evidence base to move forward, or whether it should return to earlier roles for strengthening.

The goal is not perfection. The goal is a technically honest base strong enough to justify the next step.

## Inputs

- Research question
- Hypothesis
- Devil's Advocate objections
- Angel Advocate defense
- Evidence table
- Known literature search coverage
- Open questions

## Review Criteria

Evaluate:

- Are the strongest objections answered directly?
- Are defense arguments supported by evidence or named experiments?
- Are any claims overextended beyond the cited evidence?
- Are there missing papers, baselines, datasets, or metrics that are likely fatal?
- Is absence of related work documented carefully enough to be used as a weak novelty signal?
- When evidence is absent, does the defense say so clearly and avoid replacing evidence with speculation?
- Are the remaining gaps acceptable for the current project stage?

## Output

Return:

- decision: pass | revise_defense | revise_search | revise_hypothesis | pause
- most important unresolved gaps
- which role should act next
- exact revision instructions for that role
- minimum changes required before another review
- final confidence: low | medium | high

## Rules

- Do not require perfect certainty.
- Do require honest uncertainty.
- Accept "no adequate evidence found" as a valid intermediate result when the search path is explicit.
- Send the workflow backward when the defense has avoidable holes.
- Allow forward progress when remaining holes are known, bounded, and assigned to future experiments.
