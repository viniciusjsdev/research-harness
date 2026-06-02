# Research Brief: Harness sem Fine-tuning para Análise Industrial-Financeira

Run ID: 2026-06-02-industrial-financial-harness-full-01
Date: 2026-06-02
Status: draft for review

## 1. Executive summary

O projeto deve ser reformulado de uma proposta centrada em fine-tuning de um LLM para uma proposta centrada em uma Estrutura Harness sem fine-tuning.

A versão mais defensável não afirma que o modelo “aprende” causalidade industrial-financeira nos pesos. Ela investiga se um Harness consegue orquestrar um LLM genérico, consultas estruturadas, RAG, ferramentas de cálculo, rastreamento de evidência e auditoria de assumptions para responder perguntas sobre impacto financeiro de eventos industriais.

Formulação curta:

> O projeto investiga se uma Estrutura Harness sem fine-tuning pode conectar eventos industriais a impactos financeiros de forma rastreável, calculável e auditável.

Formulação técnica:

> Este projeto propõe e avalia uma arquitetura Harness sem fine-tuning para decompor perguntas industrial-financeiras, recuperar evidências, consultar dados estruturados, executar cálculos verificáveis, explicitar assumptions e gerar respostas auditáveis sobre impactos financeiros de falhas, paradas e perdas de produtividade.

## 2. Research question

Pergunta principal:

> Uma Estrutura Harness sem fine-tuning consegue produzir respostas mais auditáveis, rastreáveis e computacionalmente viáveis do que abordagens centradas em LLM puro, RAG simples ou fine-tuning, em tarefas que conectam eventos industriais a impactos financeiros?

Pergunta operacional mínima:

> Dado um evento industrial, dados de produção e dados financeiros por produto/período, o sistema consegue estimar impacto em receita e margem, mostrando evidências, inferências, assumptions, open questions e trilha de cálculo?

## 3. Hypothesis

Hipótese principal:

> Para análise industrial-financeira, a especialização do sistema via Harness pode ser mais importante do que a especialização do modelo via fine-tuning, porque a tarefa exige dados atualizados, cálculo verificável, rastreabilidade e explicitação de incerteza.

Hipótese secundária:

> Fine-tuning pode ser útil como baseline ou comparação, mas não deve ser o centro metodológico quando a tarefa depende de evidência externa, dados tabulares e fórmulas reproduzíveis.

## 4. Contribuição metodológica real

A contribuição metodológica real não é “criar uma IA que entende indústria e finanças”. Essa frase é ampla demais e difícil de defender.

A contribuição real é:

> Um protocolo e uma arquitetura Harness para transformar perguntas industrial-financeiras em uma sequência auditável de decomposição, recuperação, consulta estruturada, cálculo, separação epistemológica e avaliação.

Contribuições específicas:

1. Decomposição de perguntas híbridas
   - Exemplo: “qual foi o impacto da falha da máquina X?” vira subtarefas sobre evento, período, máquina, linha, produto, tempo parado, produção perdida, preço, custo, margem e dados ausentes.

2. Separação epistemológica obrigatória
   - Toda resposta deve distinguir `Evidence`, `Inference`, `Assumption` e `Open question`.

3. Externalização do conhecimento
   - O conhecimento e os dados ficam em bases, documentos, consultas, grafos e ferramentas, não nos pesos do modelo.

4. Cálculo verificável fora do LLM
   - Receita, custo, margem e perda estimada devem ser calculados por ferramenta ou regra reproduzível, com trilha de cálculo.

5. Avaliação comparativa
   - Comparar Harness contra LLM zero-shot, RAG simples, SQL/BI determinístico, grafo, RAG+SQL e, opcionalmente, fine-tuning.

6. Métrica de auditabilidade
   - Avaliar se a resposta pode ser rastreada, recalculada e criticada, não apenas se parece semanticamente plausível.

## 5. Related work map: evidência preliminar

Busca executada em 2026-06-02, principalmente em OpenAlex. A busca foi mínima e preliminar, suficiente para orientar a reformulação, não para sustentar claims fortes de novidade.

Arquivos brutos:

- `data/raw/literature/2026-06-02-industrial-financial-harness-full/`

Resultados preliminares úteis:

1. FinQA
   - Chen et al., 2021, “FinQA: A Dataset of Numerical Reasoning over Financial Data”, DOI: https://doi.org/10.18653/v1/2021.emnlp-main.300
   - Relevância: apoia a existência de benchmark para raciocínio numérico financeiro sobre dados financeiros.
   - Limitação: não valida, por si só, ligação entre falha industrial e impacto financeiro.

2. RAG
   - Lewis et al., 2020, “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”, OpenAlex: https://openalex.org/W3098425262
   - Relevância: fundamenta recuperação externa como alternativa/complemento a conhecimento paramétrico.
   - Limitação: RAG textual não resolve sozinho cálculo tabular, SQL, causalidade ou auditabilidade.

3. Toolformer / uso de ferramentas
   - Schick et al., 2023, “Toolformer: Language Models Can Teach Themselves to Use Tools”, DOI: https://doi.org/10.48550/arxiv.2302.04761
   - Relevância: evidencia a linha de LLMs usando ferramentas externas.
   - Limitação: não é específico para decisão industrial-financeira.

4. Text-to-SQL / BIRD
   - Li et al., 2023, “Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs”, DOI: https://doi.org/10.48550/arxiv.2305.03111
   - Relevância: sugere baseline e métrica para consulta estruturada em banco de dados.
   - Limitação: text-to-SQL correto não garante interpretação financeira correta.

5. Datasets industriais de falha
   - “Condition Monitoring of Bearing Damage in Electromechanical Drive Systems by Using Motor Current Signals of Electric Motors: A Benchmark Data Set for Data-Driven Classification”, 2016, DOI: https://doi.org/10.36001/phme.2016.v3i1.1577
   - Relevância: exemplo de benchmark industrial para diagnóstico/classificação de falha.
   - Limitação: não inclui impacto financeiro empresarial.

Search failures / limitações da busca:

- A busca direta por trabalhos que combinem falha industrial, produção perdida, receita, margem e Harness LLM sem fine-tuning não encontrou evidência diretamente equivalente nesta rodada.
- Isso é apenas evidência negativa limitada; não prova novidade.
- O script `scripts/search_literature.py` sofreu HTTP 429 ao consultar arXiv e falhas de parsing em alguns resultados OpenAlex com campos nulos. Foi usado fallback via consulta OpenAlex direta.

## 6. Evidence

Evidence supplied by user:

- O projeto busca cruzar dados industriais e financeiros para apoiar decisão empresarial.
- O caso motivador é estimar impacto financeiro de falhas, paradas e perda de produtividade.
- O projeto inclui dados financeiros: receita, EBITDA, custos, despesas e margens.
- O projeto inclui dados industriais: sensores, falhas, máquinas, paradas, produtividade, unidades perdidas e manutenção.
- A formulação atual menciona FinQA, FailureSensorIQ e relatórios de RI da Gerdau.
- A formulação atual propõe bancos relacionais e Data Warehouse.
- A formulação atual propõe fine-tuning de Mistral-7B-Instruct-v0.3 com LoRA/QLoRA.
- A nova direção desejada é estudar Harness sem fine-tuning.

Evidence from preliminary literature search:

- FinQA existe como dataset de raciocínio numérico sobre dados financeiros.
- RAG existe como abordagem para combinar geração com recuperação externa.
- Toolformer e trabalhos correlatos sustentam a ideia geral de LLMs usando ferramentas externas.
- Benchmarks text-to-SQL como BIRD podem apoiar avaliação de consulta estruturada.
- Existem benchmarks industriais de condição/falha, mas a busca preliminar não verificou um dataset público pareado com impacto financeiro.

Evidence not yet verified:

- A adequação real de FailureSensorIQ para este projeto.
- A granularidade dos relatórios de RI da Gerdau para validar eventos específicos de máquina.
- A existência de dataset público que conecte falha industrial a receita, margem ou EBITDA.
- A existência de trabalhos diretamente equivalentes ao Harness industrial-financeiro sem fine-tuning.

## 7. Inference

- O problema exige mais do que linguagem natural: exige consulta estruturada, cálculo, checagem de unidades, períodos e rastreabilidade.
- Fine-tuning não é a intervenção mais alinhada ao objetivo se a prioridade é auditabilidade e dados atualizados.
- RAG textual simples é insuficiente para tarefas que dependem de tabelas, fórmulas e relações entre eventos e indicadores financeiros.
- Grafos podem ajudar a estruturar relações entre máquina, falha, linha, produto, custo e receita, mas não substituem cálculo nem validação.
- A tese deve evitar causalidade forte e usar formulações como “estimativa de impacto sob assumptions explícitas”.
- A maior incerteza metodológica é disponibilidade de dados pareados industrial-financeiros.

## 8. Assumption

- Há mapeamento possível entre evento industrial, produto, linha, período e indicador financeiro.
- Perda de produção pode ser estimada a partir de tempo de parada e taxa esperada de produção.
- Perda de produção pode ser convertida em receita ou margem usando preço médio e custo variável.
- O impacto financeiro pode ser estimado sem afirmar causalidade forte.
- Um Harness pode reduzir alucinação ao obrigar evidência, cálculo e assumptions explícitas.
- Um benchmark sintético ou semi-sintético pode ser aceitável para o primeiro experimento.
- Métricas de auditabilidade podem ser operacionalizadas.

Assumption crítica:

> Nem toda unidade não produzida representa receita perdida. Pode haver estoque, recuperação posterior de produção ou demanda insuficiente. Portanto, receita perdida deve ser tratada como estimativa sob assumption, não como fato.

## 9. Open question

Dados:

- Existe dataset público com eventos industriais e impacto financeiro pareados?
- FailureSensorIQ contém apenas falha/sensor ou também consequência econômica?
- Relatórios da Gerdau são granulares o suficiente para validação operacional?
- Será necessário criar dataset sintético, semi-sintético ou usar dados privados?

Metodologia:

- O problema deve ser formulado como causalidade, correlação ou cálculo contrafactual simples?
- EBITDA deve ser removido do primeiro experimento?
- Como impedir que o LLM infira causalidade além da evidência?

Avaliação:

- Qual será o gabarito das respostas?
- A validação será por regra calculada, especialista, simulação ou comparação com relatório real?
- Como medir qualidade de assumptions?
- Como medir fidelidade semântica sem subjetividade excessiva?

## 10. Contradictory evidence / contradições internas

1. Fine-tuning versus auditabilidade
   - O projeto quer explicabilidade, mas fine-tuning internaliza conhecimento e dificulta rastrear origem de afirmações.

2. Causalidade versus granularidade
   - O projeto fala em causa e efeito, mas fontes financeiras públicas tendem a ser agregadas demais para eventos de máquina.

3. FinQA + FailureSensorIQ não formam automaticamente um benchmark híbrido
   - Um benchmark financeiro e um benchmark industrial separados não validam a tarefa integrada.

4. EBITDA pode ser métrica inadequada no primeiro nível
   - EBITDA é agregado e influenciado por múltiplos fatores. Receita e margem por produto/período são alvos iniciais mais defensáveis.

5. RAG textual versus dados relacionais
   - RAG é útil para documentos, mas consultas tabulares devem usar SQL/Data Warehouse.

6. Grafos ajudam relações, não resolvem cálculo
   - Grafo pode representar relações, mas não substitui cálculo financeiro e checagem de assumptions.

## 11. Technical approach

Arquitetura Harness proposta:

```text
User Question
  -> Question Decomposer
  -> Evidence Planner
  -> Data Retriever
       - SQL/Data Warehouse
       - RAG documental
       - grafo de conhecimento, se houver
  -> Computation Engine
       - produção perdida
       - receita estimada
       - custo/margem estimados
  -> Assumption Tracker
  -> Evidence Auditor
  -> Response Formatter
  -> Evaluation Logger
```

Saída obrigatória:

```text
Answer
Evidence
Inference
Assumption
Open question
Calculation trace
Confidence
Missing data
```

## 12. Metrics and baselines

Baselines:

1. LLM zero-shot
2. LLM + RAG textual simples
3. LLM + SQL/Data Warehouse
4. BI/regra determinística sem LLM
5. Grafo de conhecimento
6. Harness completo sem fine-tuning
7. Fine-tuning + RAG, opcional, como baseline secundário

Critérios de avaliação:

- correção factual;
- correção de cálculo;
- rastreabilidade de números e afirmações;
- separação entre Evidence, Inference, Assumption e Open question;
- taxa de alucinação;
- capacidade de recusa quando faltam dados;
- qualidade e necessidade das assumptions;
- robustez a dados incompletos;
- precisão de consultas SQL;
- utilidade decisória;
- latência;
- custo por pergunta;
- reprodutibilidade.

## 13. Adversarial critique

A ideia pode falhar se:

- não houver dados pareados para validar o problema real;
- o Harness continuar inferindo causalidade indevida;
- o benchmark sintético for artificial demais;
- o sistema não superar uma regra determinística simples;
- a avaliação de “fidelidade semântica” for subjetiva;
- a proposta tentar cobrir receita, margem, EBITDA, eficiência, sensores, grafos e RAG ao mesmo tempo;
- a contribuição parecer apenas integração de ferramentas, não metodologia avaliável.

## 14. Angel Advocate defense

A direção Harness é defensável porque:

- problemas empresariais exigem rastreabilidade e atualização de dados;
- cálculos financeiros devem ser reproduzíveis;
- assumptions são inevitáveis e precisam aparecer explicitamente;
- fine-tuning não garante consulta correta, cálculo correto ou recusa adequada;
- Harness permite comparar modularmente RAG, SQL, grafos e ferramentas;
- a arquitetura pode ser avaliada por critérios objetivos de cálculo, evidência e recusa.

## 15. Argument Arbiter review

Decision: `revise_hypothesis`

Justificativa:

A direção Harness sem fine-tuning é promissora, mas a hipótese precisa ser delimitada. A versão atual ainda corre risco de prometer causalidade forte, impacto em EBITDA e validação com dados reais sem demonstrar disponibilidade de dados pareados.

Instruções de revisão:

- Reformular “causa e efeito” para “estimativa de impacto sob assumptions explícitas”.
- Começar com receita e margem, não EBITDA.
- Tratar Gerdau RI como contexto financeiro agregado, não validação direta de máquina, até prova contrária.
- Definir benchmark mínimo com gabarito calculável.
- Manter fine-tuning apenas como baseline opcional, não como objeto central.

Confidence:

- Metodologia reformulada: medium.
- Novidade: low, porque a busca foi preliminar.
- Viabilidade com dados reais: medium-low.
- Viabilidade do MEV controlado: medium-high.

## 16. Minimum viable experiment

Construir micro-benchmark com 30–50 perguntas.

Dados mínimos:

1. Tabela de eventos industriais
   - event_id
   - machine_id
   - line_id
   - product_id
   - start_time
   - end_time
   - downtime_hours
   - failure_type
   - expected_units_per_hour
   - actual_units_produced
   - lost_units

2. Tabela financeira por produto/período
   - product_id
   - period
   - average_price
   - variable_cost_per_unit
   - gross_margin_per_unit

3. Tabela de mapeamento
   - machine_id
   - line_id
   - product_id
   - plant_id

4. Documentos textuais pequenos
   - relatório financeiro resumido;
   - nota operacional;
   - documento de assumptions.

Perguntas-teste:

- Qual foi a perda estimada de receita da falha E17?
- Qual evento teve maior impacto estimado em margem?
- A falha da máquina M3 pode explicar queda de receita no período P?
- Quais valores são evidência e quais são assumptions?
- Há dados suficientes para estimar impacto em EBITDA?
- Se o preço médio estiver ausente, o sistema deve responder ou recusar?

Critério de sucesso:

O Harness deve superar LLM zero-shot e RAG simples em correção de cálculo, rastreabilidade, explicitação de assumptions, menor alucinação e capacidade de recusa.

Critério de falha:

A hipótese enfraquece se o Harness não superar regra SQL/BI simples, se continuar inferindo causalidade indevida, se exigir intervenção manual excessiva ou se não houver gabarito avaliável.

## 17. Decision recommendation

Recomendação:

> Prosseguir, mas com hipótese revisada e MEV restrito.

Não defender como:

> “Uma IA entende causa e efeito entre indústria e finanças.”

Defender como:

> “Um Harness sem fine-tuning orquestra evidências, dados estruturados e cálculo verificável para estimar impacto financeiro-operacional sob assumptions explícitas.”

Próximo passo recomendado:

1. Literature Scout ampliado para trabalhos diretamente relacionados.
2. Definir schema do benchmark mínimo.
3. Criar dataset sintético pequeno.
4. Implementar baselines: regra determinística, LLM zero-shot, RAG simples, Harness.
5. Avaliar antes de qualquer discussão sobre fine-tuning.
