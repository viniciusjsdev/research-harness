role name:
Methodology Reviewer

task summary:
Avaliar a adequação metodológica da pesquisa temporária sobre comparação entre Fine-Tuning e Harness para uso de IA em contexto financeiro e industrial, com foco em localizar correlações entre domínios a partir de bases de dados.

input artifacts reviewed:
- `docs/nomenclature.md`
- `prompts/roles/methodology_reviewer.md`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/01_research_lead/output/response.md`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/02_literature_scout/output/response.md`

method fit assessment:
- A formulação “Fine-Tuning versus Harness” ainda está metodologicamente ampla demais para sustentar uma comparação científica direta.
- A pergunta precisa ser decomposta por tarefa, porque Fine-Tuning e Harness não são alternativas simétricas:
  - Fine-Tuning é uma técnica de adaptação de modelo.
  - Harness é uma arquitetura/processo que pode incluir RAG, tool-use, text-to-SQL, validação estatística, auditoria, logging e revisão humana.
- Para o objetivo “localizar correlações entre domínios”, o método central não pode ser apenas LLM. A tarefa exige:
  - modelagem estatística;
  - tratamento temporal;
  - controle de confundidores;
  - validação contra hipóteses nulas;
  - avaliação de falsas descobertas;
  - reprodutibilidade.
- Engineering feasibility:
  - Um Harness é plausivelmente viável para orquestrar consultas, recuperação, ferramentas estatísticas, validação e relatórios.
  - Fine-Tuning é plausivelmente viável para subtarefas como text-to-SQL, extração de variáveis, normalização terminológica e interpretação de documentos.
- Scientific validity:
  - Nenhuma das duas abordagens está validada, com base nos artefatos revisados, como superior para descoberta de correlações financeiro-industriais.
  - O desenho atual ainda não define tarefa, dataset, gold standard, métrica primária, métrica de erro estatístico ou baseline obrigatório.

dataset/substrate adequacy assessment:
- A adequação do substrato empírico é atualmente insuficiente.
- O Literature Scout não encontrou benchmark completo para descoberta de correlação entre domínios financeiro-industriais.
- Os clusters encontrados são adjacentes, não substitutos diretos:
  - financial RAG/QA;
  - text-to-SQL/BI;
  - agentes/tool-use;
  - ambiguidade em análise tabular;
  - concept drift;
  - domain adaptation em falha industrial;
  - explainability/governance.
- Para uma avaliação metodologicamente defensável, o substrato mínimo deve especificar:
  - fontes financeiras;
  - fontes industriais;
  - chaves de integração;
  - granularidade temporal;
  - defasagens admissíveis;
  - variáveis-alvo ou pares de variáveis esperados;
  - ground truth, oracle humano, ou protocolo de validação estatística;
  - política para dados ausentes, mudanças de fonte e revisões históricas.
- Sem isso, qualquer conclusão tenderá a medir capacidade de gerar narrativas ou consultas, não capacidade de descobrir correlações válidas.

metrics and baseline adequacy assessment:
- Métricas ainda não estão adequadamente definidas.
- Métricas necessárias para separar subtarefas:
  - Data access / SQL:
    - execução correta;
    - exact match ou equivalência semântica de SQL;
    - taxa de erro de schema;
    - taxa de consultas inválidas.
  - Recuperação / RAG:
    - recall de fontes relevantes;
    - precisão de recuperação;
    - groundedness;
    - taxa de citações incorretas.
  - Extração:
    - precisão, recall, F1;
    - erro de normalização de entidades/variáveis;
    - consistência interdocumental.
  - Correlação:
    - taxa de falso positivo;
    - controle de false discovery rate;
    - estabilidade out-of-sample;
    - robustez a janelas temporais;
    - sensibilidade a defasagens;
    - intervalo de confiança;
    - erro sob correlação espúria conhecida.
  - Operacional:
    - custo;
    - latência;
    - auditabilidade;
    - reprodutibilidade;
    - esforço humano de revisão.
- Baselines obrigatórios ainda estão ausentes ou apenas propostos.
- Baselines mínimos recomendados:
  - análise estatística tradicional sem LLM;
  - SQL/BI manual ou scripted;
  - prompting-only LLM;
  - RAG sem fine-tuning;
  - text-to-SQL sem fine-tuning específico;
  - fine-tuned text-to-SQL ou modelo adaptado ao domínio;
  - Harness com ferramentas estatísticas e logs;
  - modelo tabular/time-series clássico quando houver previsão;
  - baseline nulo ou permutação temporal para detectar correlações espúrias.
- Sem baselines não-LLM, a comparação confundirá automação linguística com descoberta estatística real.

threats to validity:
- Internal validity:
  - Correlações espúrias por múltiplas comparações.
  - Confundidores macroeconômicos, sazonais, regulatórios e operacionais.
  - Vazamento temporal se dados futuros forem usados direta ou indiretamente.
  - Ambiguidade de perguntas em linguagem natural sobre dados tabulares.
  - Erros de join, unidade, moeda, escala, frequência temporal ou schema.
  - LLMs podem inventar relações plausíveis sem suporte estatístico.
- External validity:
  - Resultados em financial QA podem não generalizar para correlação financeiro-industrial.
  - Resultados em text-to-SQL/BI podem não generalizar para descoberta estatística.
  - Resultados em fault diagnosis industrial podem não generalizar para impactos financeiros.
  - Benchmarks sintéticos podem superestimar desempenho em dados empresariais reais.
- Construct validity:
  - “Harness” ainda é construto amplo demais.
  - “Fine-Tuning” pode significar adaptação de domínio, instruction tuning, fine-tuning supervisionado, LoRA, text-to-SQL especializado ou outro procedimento.
  - “Localizar correlações” pode significar recuperar relações conhecidas, gerar hipóteses, detectar associação estatística ou inferir causalidade.
- Statistical conclusion validity:
  - Falta definição de poder estatístico.
  - Falta controle de múltiplos testes.
  - Falta protocolo para autocorrelação, defasagem e regime shift.
  - Falta critério para distinguir correlação, predição e causalidade.
- Reproducibility:
  - Pipelines baseados em LLM podem variar por modelo, versão, temperatura, prompt, contexto recuperado e ferramentas disponíveis.
  - Fine-tuning depende de dados de treino, split, hiperparâmetros, seed e contaminação de benchmark.
  - Harness depende de logs, versionamento de dados, prompts e execução das ferramentas.

confounders and controls:
- Confounder: qualidade do dataset.
  - Control: usar o mesmo dataset e mesmos splits para todas as abordagens.
- Confounder: capacidade do modelo base.
  - Control: comparar abordagens com o mesmo modelo base quando possível.
- Confounder: acesso desigual a ferramentas.
  - Control: definir claramente quais ferramentas cada condição pode usar.
- Confounder: RAG com fontes melhores que o corpus de fine-tuning.
  - Control: igualar o universo informacional disponível para cada condição.
- Confounder: fine-tuning treinado em dados próximos do teste.
  - Control: split temporal e deduplicação rigorosa.
- Confounder: avaliação por julgamento humano sem rubrica.
  - Control: rubrica pré-registrada e dupla avaliação quando possível.
- Confounder: mudança temporal nos domínios financeiro e industrial.
  - Control: validação walk-forward, janelas temporais e testes por regime.
- Confounder: múltiplas hipóteses testadas até encontrar correlação.
  - Control: correção por múltiplos testes, holdout confirmatório e registro das hipóteses exploratórias.
- Confounder: variáveis latentes comuns.
  - Control: incluir controles macroeconômicos, sazonalidade, setor, geografia, tamanho da empresa, energia, commodities ou outros fatores relevantes conforme o dataset.
- Confounder: granularidade incompatível.
  - Control: padronizar frequência temporal, unidades, moeda, deflatores e agregações antes da comparação.

minimum methodological revisions:
1. Redefinir a pergunta como comparação por arquitetura e tarefa, não como superioridade genérica.
   - Exemplo: “Qual configuração produz correlações estatisticamente válidas, auditáveis e reprodutíveis em dados financeiro-industriais heterogêneos?”

2. Operacionalizar “Fine-Tuning”.
   - Especificar modelo base.
   - Especificar tipo de fine-tuning.
   - Especificar dados de treino.
   - Especificar tarefa: text-to-SQL, extração, classificação, QA ou geração de hipóteses.

3. Operacionalizar “Harness”.
   - Especificar componentes:
     - RAG;
     - SQL;
     - ferramentas estatísticas;
     - logs;
     - validação;
     - prompts;
     - revisão humana.
   - Definir quais etapas são automáticas e quais são avaliadas.

4. Separar subtarefas.
   - Acesso aos dados.
   - Entendimento de schema.
   - Extração/normalização.
   - Geração de consultas.
   - Teste estatístico.
   - Explicação.
   - Auditoria.

5. Escolher substrato empírico mínimo.
   - Dataset público, sintético controlado ou combinação de ambos.
   - Deve conter relações conhecidas ou protocolo para validação independente.
   - Deve permitir testar correlações reais e correlações espúrias.

6. Definir baselines obrigatórios.
   - Pelo menos um baseline não-LLM estatístico/BI.
   - Pelo menos um baseline prompting-only.
   - Pelo menos um RAG/tool-use.
   - Pelo menos um fine-tuned/adapted component, se dados de treino forem suficientes.

7. Definir métricas primárias e secundárias.
   - Métrica primária não deve ser apenas qualidade textual.
   - Deve incluir validade estatística, falso positivo, reprodutibilidade e auditabilidade.

8. Usar validação temporal.
   - Principalmente se dados financeiros, industriais, macroeconômicos ou operacionais forem séries temporais.

9. Incorporar controles contra múltiplas comparações e p-hacking.
   - Registrar hipóteses exploratórias versus confirmatórias.
   - Usar holdout confirmatório.

10. Marcar explicitamente que a literatura atual é preliminar.
   - Não concluir superioridade de Fine-Tuning ou Harness até haver evidência comparativa ou experimento próprio.

Evidence:
- Evidence:
  O Research Lead definiu a pergunta como comparação entre Fine-Tuning e Harness para IA em contexto financeiro e industrial, com foco em localizar correlações entre domínios a partir de bases de dados.
- Evidence:
  O Literature Scout declarou que não encontrou evidência direta para a comparação exata nos artefatos revisados.
- Evidence:
  O Literature Scout classificou a evidência como preliminar e majoritariamente baseada em metadados/abstracts.
- Evidence:
  O Literature Scout identificou clusters adjacentes: financial RAG/question answering, text-to-SQL/BI, agentes/tool-use, ambiguidade em análise tabular, concept drift, mudança de fontes de dados, domain adaptation em diagnóstico industrial e explainability/governance.
- Evidence:
  O Literature Scout afirmou que nenhum artefato estabelece superioridade geral de Fine-Tuning ou Harness.
- Evidence:
  O Literature Scout afirmou que nenhum artefato fornece benchmark completo de descoberta de correlação financeiro-industrial.
- Evidence:
  `docs/nomenclature.md` define Methodology Reviewer como o papel que revisa métodos, métricas, datasets, baselines e validade.
- Evidence:
  `prompts/roles/methodology_reviewer.md` instrui este papel a avaliar qualidade científica e experimental, identificar confundidores e ameaças à validade, e distinguir feasibility de evidência científica.

Inference:
- Inference:
  A hipótese inicial favorecendo Harness como ponto de partida é metodologicamente plausível, mas ainda não empiricamente demonstrada.
- Inference:
  Harness tende a ser mais auditável que Fine-Tuning isolado quando o objetivo inclui provenance, SQL executável, testes estatísticos e logs.
- Inference:
  Fine-Tuning pode ser mais adequado para componentes delimitados do pipeline, mas não deve ser tratado como solução end-to-end para descoberta de correlações.
- Inference:
  A comparação só será defensável se tratar descoberta de correlação como tarefa estatística, não como tarefa puramente linguística.
- Inference:
  A maior lacuna metodológica é a ausência de dataset/benchmark e baseline comum entre as condições.
- Inference:
  O próximo papel deve atacar a hipótese pelo risco de ela estar comparando categorias desiguais: técnica de adaptação de modelo versus arquitetura operacional.

Assumption:
- Assumption:
  “Harness” nesta run significa uma arquitetura/processo orquestrado com RAG, tool-use, text-to-SQL, ferramentas estatísticas e auditabilidade, não apenas o repositório research-harness.
- Assumption:
  “Localizar correlações” exige validação estatística, controle de confundidores e avaliação temporal.
- Assumption:
  Os artefatos do Literature Scout representam corretamente as buscas feitas, mas não substituem revisão integral dos papers.
- Assumption:
  O objetivo final é produzir uma comparação útil para decisão metodológica, não apenas uma revisão narrativa.
- Assumption:
  O uso financeiro-industrial envolve dados heterogêneos, possivelmente tabulares, temporais, textuais e com restrições de governança.

Open question:
- Open question:
  Qual é a unidade exata de avaliação: descoberta de correlação, geração de hipótese, text-to-SQL, QA financeiro, BI, previsão ou explicação?
- Open question:
  Quais bases de dados serão usadas?
- Open question:
  Haverá ground truth de correlações conhecidas ou apenas avaliação exploratória?
- Open question:
  O objetivo é correlação estatística, relação causal, sinal preditivo ou associação semântica entre variáveis?
- Open question:
  Quais restrições regulatórias, de privacidade e auditoria devem ser incluídas?
- Open question:
  O Fine-Tuning será avaliado como sistema completo ou apenas como componente dentro de um Harness?
- Open question:
  O Harness poderá usar modelos fine-tuned, ou a comparação exige separação estrita entre as abordagens?
- Open question:
  Como serão tratados drift, sazonalidade, defasagens e mudanças de fonte?
- Open question:
  Qual métrica terá prioridade se houver trade-off entre validade estatística, custo, latência e auditabilidade?

recommendation for Devil's Advocate:
Devil's Advocate deve atacar a hipótese principalmente nestes pontos:

1. Categoria conceitual:
   - Fine-Tuning e Harness não são alternativas equivalentes.
   - A comparação pode estar mal formulada desde a origem.

2. Falta de evidência direta:
   - A literatura revisada não sustenta superioridade de Harness nem de Fine-Tuning para correlação financeiro-industrial.

3. Falta de benchmark:
   - Sem dataset comum, métricas comuns e baseline comum, a comparação pode virar opinião arquitetural.

4. Validade estatística:
   - LLMs podem gerar correlações plausíveis, mas estatisticamente inválidas.
   - Correlação financeiro-industrial é vulnerável a sazonalidade, regime shift, autocorrelação, defasagens e múltiplas comparações.

5. Baselines tradicionais:
   - A hipótese deve ser rejeitada ou revisada se não vencer SQL/BI + estatística tradicional.
   - Automação via LLM não implica descoberta melhor.

6. Risco de overclaiming:
   - Financial QA, text-to-SQL e industrial fault diagnosis são literaturas adjacentes, não evidência direta para cross-domain correlation discovery.

7. Defensibilidade:
   - Qualquer claim de superioridade deve exigir experimento controlado ou revisão de literatura mais forte.

Recomendação metodológica para o fluxo:
- Prosseguir para Devil's Advocate, mas com orientação forte para considerar `revise_hypothesis` ou `revise_search` se a hipótese continuar formulada como “Fine-Tuning versus Harness” em sentido geral.
