# Hermes Role Input

Run ID: run-20260607-200637-fine-tuning-vs-harness-industrial-financial

Step: 4

Role: Devil's Advocate

Profile directory: profiles/04_devils_advocate

Date: 2026-06-07

Operator: Codex

## Task

Voce esta no research-harness. Siga `AGENTS.md`.

Atue como `Devil's Advocate`.

Objetivo temporario de pesquisa:
Comparar Fine-Tuning e Harness para uso de IA em contexto financeiro e
industrial, com foco em localizar correlacoes entre dominios a partir de bases
de dados.

Ataque a hipótese como um revisor tecnico estrito. Produza somente a saida
deste papel. Nao edite arquivos. Nao crie artefatos. Nao promova materiais.

## Context Provided

Research Lead summary:
- Pergunta: quando Fine-Tuning supera, iguala ou perde para Harness em qualidade
  analitica, rastreabilidade, custo, adaptabilidade, risco operacional e
  defensibilidade metodologica?
- Hipotese inicial: Harness pode ser mais defensavel como ponto de partida para
  descoberta/validacao de correlacoes porque combina recuperacao, consultas,
  ferramentas estatisticas, auditoria e logs.

Literature Scout summary:
- Nenhum paper diretamente comparando fine-tuning versus harness para descoberta
  de correlacao financeiro-industrial foi encontrado nos artifacts revisados.
- Evidencia e preliminar, majoritariamente metadata/abstract-only.
- Clusters adjacentes: financial RAG/QA, text-to-SQL/BI, LLM agents/tool-use,
  tabular ambiguity, concept drift, domain adaptation, XAI/governance.

Methodology Reviewer summary:
- Fine-Tuning e Harness nao sao categorias simetricas.
- O problema precisa ser decomposto por tarefa.
- Correlacao entre dominios exige estatistica, controles, validacao temporal,
  baselines e controle de falso positivo.
- Dataset/substrato, metricas e baselines ainda estao insuficientes.
- Baselines nao-LLM sao obrigatorios.

## Constraints

- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Do not invent contradictory evidence.
- If evidence is missing, state what evidence would be needed.
- Do not edit files.
- Do not promote artifacts.

## Expected Output

Return:

- role name
- task summary
- input artifacts reviewed
- top rejection risks
- weakest assumptions
- missing baselines
- confounders and edge cases
- falsification tests
- likely reviewer objections
- Evidence
- Inference
- Assumption
- Open question
- final recommendation: reject | weak reject | borderline | weak accept | accept
- instruction for Angel Advocate
