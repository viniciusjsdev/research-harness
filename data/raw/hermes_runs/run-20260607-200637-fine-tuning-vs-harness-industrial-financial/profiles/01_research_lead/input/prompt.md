# Hermes Role Input

Run ID: run-20260607-200637-fine-tuning-vs-harness-industrial-financial

Step: 1

Role: Research Lead

Profile directory: profiles/01_research_lead

Date: 2026-06-07

Operator: Codex

## Task

Voce esta no research-harness. Siga `AGENTS.md`.

Objetivo temporario de pesquisa:
Comparar Fine-Tuning e Harness para uso de IA em contexto financeiro e
industrial, com foco em localizar correlacoes entre dominios a partir de bases
de dados.

Atue como `Research Lead`.

Produza somente a saida deste papel. Nao edite arquivos. Nao crie artefatos.

## Context Provided

- O repositorio e um harness generico de pesquisa.
- Esta run valida se Hermes consegue executar o loop completo usando papeis
  oficiais, input/output por perfil e promocao controlada.
- A ideia fornecida pelo usuario e temporaria e nao deve virar identidade
  permanente do repositorio.
- Fine-tuning, Harness, RAG, tool-use, text-to-SQL, BI e correlacao
  financeiro-industrial devem ser tratados como possiveis objetos de analise,
  nao como conclusoes ja provadas.

## Constraints

- Follow `AGENTS.md`.
- Use official role names from `docs/nomenclature.md`.
- Separate `Evidence`, `Inference`, `Assumption`, and `Open question`.
- Do not invent references, URLs, DOIs, authors, metrics, datasets, or results.
- Do not claim novelty without literature evidence.
- Do not edit files.
- Do not promote artifacts.

## Expected Output

Return:

- role name
- task summary
- input artifacts reviewed
- precise research question
- working hypothesis
- Evidence
- Inference
- Assumption
- Open question
- role sequence for this run
- constraints and required artifacts
- next role instruction
