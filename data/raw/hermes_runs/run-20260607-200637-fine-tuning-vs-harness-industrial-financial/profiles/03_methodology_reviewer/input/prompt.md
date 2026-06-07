# Hermes Role Input

Run ID: run-20260607-200637-fine-tuning-vs-harness-industrial-financial

Step: 3

Role: Methodology Reviewer

Profile directory: profiles/03_methodology_reviewer

Date: 2026-06-07

Operator: Codex

## Task

Voce esta no research-harness. Siga `AGENTS.md`.

Atue como `Methodology Reviewer`.

Objetivo temporario de pesquisa:
Comparar Fine-Tuning e Harness para uso de IA em contexto financeiro e
industrial, com foco em localizar correlacoes entre dominios a partir de bases
de dados.

Produza somente a saida deste papel. Nao edite arquivos. Nao crie artefatos.
Nao promova materiais.

## Context Provided

Research Lead output:
`profiles/01_research_lead/output/response.md`

Literature Scout output:
`profiles/02_literature_scout/output/response.md`

Key Literature Scout findings:

- Direct evidence for the exact comparison is missing in the reviewed artifacts.
- Evidence is preliminary and mostly metadata/abstract-only.
- Adjacent clusters found:
  - financial RAG/question answering;
  - text-to-SQL/BI benchmarks and data synthesis;
  - LLM agents/tool-use;
  - tabular query ambiguity;
  - concept drift/changing data sources;
  - industrial fault diagnosis/domain adaptation;
  - explainability/governance.
- No artifact establishes that fine-tuning or harness is superior overall.
- No artifact provides a complete financial-industrial correlation discovery
  benchmark.

## Constraints

- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Do not invent references, datasets, metrics, or results.
- Distinguish engineering feasibility from scientific validity.
- Treat missing baselines or datasets as risks.
- Do not edit files.
- Do not promote artifacts.

## Expected Output

Return:

- role name
- task summary
- input artifacts reviewed
- method fit assessment
- dataset/substrate adequacy assessment
- metrics and baseline adequacy assessment
- threats to validity
- confounders and controls
- minimum methodological revisions
- Evidence
- Inference
- Assumption
- Open question
- recommendation for Devil's Advocate
