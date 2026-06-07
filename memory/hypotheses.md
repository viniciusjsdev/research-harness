# Hypotheses

Use this file for active, paused, rejected, or completed research hypotheses.

## HYP-0001: Research Ideation Harness

Status: active

Idea:
Build a harness that helps transform early research ideas into structured hypotheses, related-paper searches, adversarial critiques, defense arguments, and next experiments.

Research question:
Can a structured agentic workflow improve the quality and speed of early-stage scientific R&D ideation?

Initial assumptions:

- A repeatable workflow can reduce shallow literature comparison.
- Versioned research memory improves continuity across sessions.
- Adversarial review can expose weak assumptions before implementation.

Open questions:

- Which academic search providers should be first-class?
- What evidence scoring rubric is strict enough for technical review?
- How much generated memory should be automatically committed versus manually curated?

Next actions:

- Define schemas for ideas, papers, claims, and comparisons.
- Create prompts for ideation, literature search, adversarial review, and defense.
- Test the workflow on one real research idea.

## HYP-0002: Harness sem Fine-tuning para Análise Industrial-Financeira

Status: under review

Idea:
Reformular uma solução de IA industrial-financeira originalmente centrada em fine-tuning de LLM para uma Estrutura Harness sem fine-tuning, capaz de cruzar eventos industriais com impactos financeiros por meio de recuperação de evidência, consultas estruturadas, cálculo verificável e explicitação de assumptions.

Research question:
Uma Estrutura Harness sem fine-tuning consegue produzir respostas mais auditáveis, rastreáveis e computacionalmente viáveis do que LLM puro, RAG simples ou fine-tuning em tarefas que conectam eventos industriais a impactos financeiros?

Initial assumptions:

- Eventos industriais podem ser mapeados a produto, período e variáveis financeiras.
- Perda de produção pode ser convertida em impacto financeiro sob assumptions explícitas.
- A tarefa inicial pode ser validada com benchmark controlado antes de dados reais completos.
- Fine-tuning não é necessário para testar o valor metodológico do Harness.

Open questions:

- Existe dataset público pareado industrial-financeiro?
- FailureSensorIQ é adequado como substrato industrial?
- Relatórios de RI da Gerdau têm granularidade suficiente para validação ou apenas contexto agregado?
- EBITDA deve ser removido do primeiro experimento?
- Qual baseline determinístico é forte o suficiente para desafiar o Harness?

Next actions:

- Ampliar Literature Scout com fontes acadêmicas e benchmarks específicos.
- Definir schema do micro-benchmark.
- Construir dataset sintético mínimo com gabarito calculável.
- Comparar LLM zero-shot, RAG simples, LLM+SQL, BI/regra determinística e Harness completo.

## HYP-0003: Harness como Camada Metodológica para Correlação Financeiro-Industrial

Status: revise_hypothesis

Idea:
Avaliar Harness como camada metodológica auditável para exploração, validação e documentação de correlações entre bases financeiras e industriais. Fine-tuning não deve ser tratado como alternativa direta ao Harness; deve ser avaliado apenas como componente auxiliar para subtarefas rotuladas, como extração de variáveis, normalização semântica, text-to-SQL ou classificação de eventos.

Research question:
Um Harness com recuperação controlada, consultas estruturadas, ferramentas estatísticas, logs, validação temporal e revisão humana melhora a auditabilidade e a disciplina metodológica de uma investigação de correlações financeiro-industriais quando comparado a um baseline estatístico/BI sem LLM?

Current evidence status:

- Evidence: a run Hermes completa em `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/` decidiu `revise_hypothesis`.
- Evidence: o Evidence Auditor classificou claims empíricos de superioridade como fracos ou não suportados.
- Evidence: o Argument Arbiter rejeitou a formulação binária "Fine-Tuning versus Harness" como comparação direta.
- Inference: a formulação revisada é mais defensável como hipótese metodológica exploratória.

Initial assumptions:

- O valor inicial do Harness está em auditabilidade, rastreabilidade, validação e controle metodológico, não em substituir estatística.
- Correlação financeiro-industrial exige controles contra leakage temporal, drift, múltiplas comparações e correlação espúria.
- Fine-tuning só deve entrar no MVE se houver subtarefa supervisionada com dados rotulados suficientes.

Open questions:

- Quais bases financeiras e industriais públicas serão usadas no MVE?
- Qual baseline estatístico/BI sem LLM será escolhido?
- Como auditabilidade será medida quantitativamente?
- Existe subtarefa rotulada que justifique fine-tuning nesta investigação?

Next actions:

- Selecionar um substrato público, sintético ou híbrido com séries financeiras e industriais alinháveis temporalmente.
- Definir baseline estatístico/BI sem LLM.
- Pré-registrar variáveis, lags, janelas e critérios de falsificação.
- Medir validade estatística separadamente de auditabilidade.
