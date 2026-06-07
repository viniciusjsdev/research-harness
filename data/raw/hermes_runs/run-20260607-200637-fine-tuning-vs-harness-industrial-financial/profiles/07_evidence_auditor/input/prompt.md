# Hermes Role Input

Run ID: run-20260607-200637-fine-tuning-vs-harness-industrial-financial

Step: 7

Role: Evidence Auditor

Profile directory: profiles/07_evidence_auditor

Date: 2026-06-07

Operator: Codex

## Task

Voce esta no research-harness. Siga `AGENTS.md`.

Atue como `Evidence Auditor`.

Audite as claims produzidas ate agora. A decisao do Argument Arbiter foi
`revise_hypothesis`. Produza somente a saida deste papel. Nao edite arquivos.
Nao crie artefatos. Nao promova materiais.

## Context Provided

Arbiter decision:
`revise_hypothesis`

Revised hypothesis candidate:
“Um Harness de pesquisa pode servir como camada metodologica auditavel para
exploracao, validacao e documentacao de correlacoes entre bases financeiras e
industriais; Fine-Tuning nao e alternativa direta ao Harness, mas pode ser
avaliado como componente auxiliar em subtarefas especificas, como extracao de
variaveis, normalizacao semantica ou classificacao de eventos.”

Important limits from prior roles:

- No directly matching paper was found in the reviewed OpenAlex/arXiv artifacts.
- Evidence is preliminary and mostly metadata/abstract-only.
- No superiority claim is supported.
- No dataset/substrate has been selected yet.
- Statistical and non-LLM baselines are mandatory.
- The original hypothesis must be revised before any durable promotion.

## Constraints

- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Check whether claims are supported, overextended, unsupported, or only
  assumption-level.
- Do not add speculative claims.
- Mark abstract-only evidence as limited.
- Do not edit files.
- Do not promote artifacts.

## Expected Output

Return:

- role name
- task summary
- input artifacts reviewed
- claim-by-claim audit
- evidence strength: weak | medium | strong
- unsupported claims
- overextended interpretations
- unverifiable references
- required fixes before finalization
- Evidence
- Inference
- Assumption
- Open question
- recommendation for Experiment Designer
