# Prompt: New Research Idea

You are analyzing a new scientific R&D idea. Convert the raw idea into a structured research object.

## Input

- Raw idea
- Optional domain
- Optional constraints
- Optional prior papers or notes

## Tasks

1. Rewrite the idea as a precise research question.
2. State the main hypothesis.
3. List assumptions that must be true.
4. Identify technical subproblems.
5. Identify likely methods.
6. Identify datasets, benchmarks, or experimental substrates.
7. Propose evaluation metrics.
8. Generate search keywords and Boolean queries.
9. Identify novelty risks.
10. Identify minimum viable experiments.

## Output

Return:

- concise summary
- structured JSON compatible with `schemas/idea.schema.json`
- open questions
- next action checklist

## Rules

- Mark uncertainty explicitly.
- Do not claim novelty without literature evidence.
- Separate assumptions from evidence.
