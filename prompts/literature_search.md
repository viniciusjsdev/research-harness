# Prompt: Literature Search

You are performing a technical literature search for an active hypothesis.

Follow `prompts/source_policy.md`.

## Tasks

1. Derive search queries from the hypothesis.
2. Search preferred academic sources first, then general web sources if needed.
3. Group papers by role:
   - foundational
   - direct competitor
   - supporting evidence
   - contradictory evidence
   - method source
   - dataset or benchmark source
4. Extract exact bibliographic metadata.
5. Record exact sources and queries used.
6. Identify missing areas that require further search.
7. If no directly relevant papers are found, document that as limited negative evidence, not proof of novelty.

## Output

For each paper:

- title
- authors
- year
- venue/source
- DOI or stable URL
- why it was selected
- relation to the active hypothesis
- confidence in relevance
- source searched
- query used

## Rules

- Do not fabricate papers or citations.
- Prefer DOI, arXiv ID, OpenAlex ID, PubMed ID, or Semantic Scholar URL when available.
- If a result is only weakly related, mark it as weak.
- Absence of results must include the searched sources and queries.
