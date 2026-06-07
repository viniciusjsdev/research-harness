# Hermes Role Input

Run ID: run-20260607-200637-fine-tuning-vs-harness-industrial-financial

Step: 8

Role: Experiment Designer

Profile directory: profiles/08_experiment_designer

Date: 2026-06-07

Operator: Codex

## Task

Voce esta no research-harness. Siga `AGENTS.md`.

Atue como `Experiment Designer`.

Converta a hipotese revisada em um minimo experimento viavel. Produza somente a
saida deste papel. Nao edite arquivos. Nao crie artefatos. Nao promova
materiais.

## Context Provided

Arbiter decision:
`revise_hypothesis`

Evidence Auditor recommendation:
Proceed only with the revised hypothesis and treat it as methodological and
exploratory, not as a conclusion.

Revised hypothesis:
“Um Harness de pesquisa pode servir como camada metodologica auditavel para
exploracao, validacao e documentacao de correlacoes entre bases financeiras e
industriais; Fine-Tuning nao e alternativa direta ao Harness, mas pode ser
avaliado como componente auxiliar em subtarefas especificas, como extracao de
variaveis, normalizacao semantica ou classificacao de eventos.”

Required constraints:

- Include at least one statistical/BI baseline without LLM.
- Evaluate Fine-Tuning only for concrete subtasks if labeled data exists.
- Measure statistical validity separately from auditability.
- Include controls against temporal leakage, drift, multiple comparisons and
  spurious correlations.
- Define falsification criteria before execution.
- Treat literature evidence as preliminary until full-paper review.

## Constraints

- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Do not invent datasets as if already verified; mark candidates as candidates.
- Success criteria must be observable.
- Failure conditions must be explicit.
- Do not edit files.
- Do not promote artifacts.

## Expected Output

Return:

- role name
- task summary
- input artifacts reviewed
- minimum viable experiment
- dataset/substrate plan
- metrics and baselines
- controls and failure cases
- support criteria
- weaken criteria
- falsify criteria
- resource estimate
- next implementation steps
- Evidence
- Inference
- Assumption
- Open question
- instruction for Research Scribe
