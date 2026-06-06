# Prompt: Source Policy

Use this policy whenever searching for, citing, or arguing from scientific literature.

## Preferred Source Order

Search these sources first when relevant:

1. OpenAlex
2. Semantic Scholar
3. arXiv
4. Crossref
5. PubMed or Europe PMC for biomedical topics
6. ACL Anthology for NLP topics
7. IEEE Xplore, ACM Digital Library, SpringerLink, ScienceDirect, or publisher pages when metadata points there
8. Official project pages, datasets, benchmarks, and code repositories linked from papers

General web search is allowed, but it should be used to find stable academic sources, project pages, datasets, code, or venue records.

## Negative Evidence Rule

Failure to find related work is not proof that no related work exists.

Not finding articles is still a valid research outcome. The system should accept it, preserve it, and use it carefully when the search trail is explicit.

When searches do not find relevant papers, record it as:

- searched sources
- exact queries used
- date of search
- inclusion criteria
- what was not found
- confidence level
- next searches that would reduce uncertainty

Create or update a search failure note using `templates/search_failure_note.md` when the absence of evidence matters to the argument.

Use absence of results as an argument only when the search was broad, source-diverse, and documented. Phrase it carefully:

```text
No directly matching work was found in the searched sources.
This suggests a possible gap, but does not prove novelty.
```

Acceptable uses:

- "The searched sources did not provide direct support for this claim."
- "The available evidence base appears thin for this exact framing."
- "This weakens the defense unless a new experiment is proposed."
- "This may indicate a research gap if broader search confirms it."

Unacceptable uses:

- "No one has done this."
- "This is novel."
- "The thesis is true because no contradiction was found."
- "The absence of papers proves the field has ignored this."

## Anti-Hallucination Rules

- Do not fabricate papers, authors, venues, metrics, URLs, or DOIs.
- Do not cite a paper unless there is a stable source for it.
- Do not claim that a paper supports a thesis unless the method/results actually support that claim.
- If only a title or abstract was reviewed, mark the evidence as preliminary.
- If a source cannot be accessed, cite only the metadata that was verified and mark limitations.
