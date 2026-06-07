# Hermes Role Input

Run ID: run-20260607-200637-fine-tuning-vs-harness-industrial-financial

Step: 9

Role: Research Scribe

Profile directory: profiles/09_research_scribe

Date: 2026-06-07

Operator: Codex

## Task

Voce esta no research-harness. Siga `AGENTS.md`.

Atue como `Research Scribe`.

Proponha atualizacoes de memoria duravel e itens a nao promover a partir desta
run. Nao edite arquivos. Nao crie artefatos. Nao promova materiais.

## Context Provided

Run decision:
`revise_hypothesis`

Revised hypothesis:
Harness should be treated as an auditable methodological layer for exploratory
and confirmatory correlation work across financial and industrial datasets;
Fine-Tuning is not a direct alternative to Harness and should only be evaluated
as an auxiliary component for concrete labeled subtasks.

Evidence Auditor:
- Empirical claims are weak.
- Methodological/conceptual claims are medium.
- Procedural conclusion `revise_hypothesis` is strong.
- No superiority or novelty claim should be promoted.

Experiment Designer:
- Proposed MVE comparing Harness against statistical/BI baseline without LLM.
- Statistical validity and auditability must be measured separately.
- Controls required: temporal leakage, drift, multiple comparisons, spurious
  correlations.
- Fine-Tuning is optional and only for labeled subtasks.

## Constraints

- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Only durable conclusions belong in memory.
- Do not dump raw conversation into memory.
- Do not store secrets, tokens, private data, PDFs, or unapproved extracted text.
- Do not promote raw outputs without review.
- Do not edit files.

## Expected Output

Return:

- role name
- task summary
- input artifacts reviewed
- proposed memory updates
- target memory files
- rationale for each update
- items intentionally not promoted
- Evidence
- Inference
- Assumption
- Open question
- final run status recommendation
