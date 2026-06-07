role name

Experiment Designer

task summary

Converter a hipótese revisada em um mínimo experimento viável, metodológico e exploratório, para testar se um Harness de pesquisa pode funcionar como camada auditável para exploração, validação e documentação de correlações entre bases financeiras e industriais, avaliando Fine-Tuning apenas como componente auxiliar em subtarefas concretas quando houver dados rotulados.

input artifacts reviewed

- Arbiter decision: revise_hypothesis
- Evidence Auditor recommendation: prosseguir somente com a hipótese revisada, como hipótese metodológica e exploratória, não como conclusão.
- Revised hypothesis:
  “Um Harness de pesquisa pode servir como camada metodologica auditavel para exploracao, validacao e documentacao de correlacoes entre bases financeiras e industriais; Fine-Tuning nao e alternativa direta ao Harness, mas pode ser avaliado como componente auxiliar em subtarefas especificas, como extracao de variaveis, normalizacao semantica ou classificacao de eventos.”
- Required constraints supplied by operator.
- AGENTS.md role and quality requirements provided in session context.
- Official role names from docs/nomenclature.md as provided in session context.

minimum viable experiment

Objetivo do MVE:

Testar, em escala reduzida, se um Harness de pesquisa melhora a auditabilidade e a disciplina metodológica na investigação de correlações entre séries financeiras e industriais, sem confundir essa função com desempenho preditivo ou com Fine-Tuning.

Unidade experimental:

Uma investigação controlada sobre um conjunto pequeno de relações candidatas entre indicadores industriais e variáveis financeiras, usando:

1. Um pipeline estatístico/BI sem LLM.
2. Um pipeline com Harness metodológico auditável.
3. Opcionalmente, uma subtarefa com modelo Fine-Tuned, somente se houver dados rotulados suficientes.

Escopo mínimo:

- 2 a 4 indicadores industriais candidatos.
- 2 a 4 variáveis financeiras candidatas.
- Horizonte temporal claramente definido.
- Uma janela de treino/exploração e uma janela temporal posterior de validação.
- Um conjunto pré-registrado de hipóteses/correlações candidatas antes da análise confirmatória.

Desenho experimental:

1. Pré-registro metodológico
   - Definir quais variáveis serão testadas.
   - Definir horizonte temporal.
   - Definir transformações permitidas.
   - Definir métricas estatísticas.
   - Definir critérios de suporte, enfraquecimento e falsificação antes da execução.
   - Definir quais análises são exploratórias e quais são confirmatórias.

2. Pipeline baseline sem LLM
   - Carregar dados candidatos.
   - Limpar e alinhar séries temporais.
   - Aplicar estatística/BI convencional:
     - correlação Pearson/Spearman;
     - regressão linear ou regularizada simples;
     - análise de defasagem temporal;
     - testes fora da amostra;
     - visualizações BI de tendência, dispersão e defasagem.
   - Registrar resultados com logs reproduzíveis.

3. Pipeline com Harness metodológico
   - Rodar os mesmos dados e análises, mas com estrutura explícita por papéis:
     - Research Lead: define escopo e pré-registro.
     - Literature Scout: documenta fontes e limitações preliminares.
     - Methodology Reviewer: revisa desenho, métricas e validade.
     - Devil's Advocate: procura vazamento temporal, comparações múltiplas, proxies espúrios e confundidores.
     - Angel Advocate: propõe defesa técnica honesta.
     - Argument Arbiter: decide pass, revise_search, revise_defense, revise_hypothesis ou pause.
     - Evidence Auditor: verifica se afirmações têm fonte ou estão marcadas como incerteza.
     - Experiment Designer: converte incertezas em testes.
     - Research Scribe: registra conclusões duráveis.
   - Medir separadamente:
     - validade estatística dos achados;
     - auditabilidade do processo.

4. Fine-Tuning opcional e restrito
   - Avaliar Fine-Tuning somente se existir dataset rotulado para subtarefa concreta.
   - Subtarefas elegíveis:
     - extração de variáveis em relatórios industriais ou financeiros;
     - normalização semântica de nomes de variáveis, setores ou eventos;
     - classificação de eventos econômicos/industriais em categorias pré-definidas.
   - Fine-Tuning não deve ser comparado como substituto do Harness.
   - Fine-Tuning deve ser comparado contra:
     - regras simples;
     - modelo base sem ajuste;
     - classificador estatístico tradicional, se aplicável.

dataset/substrate plan

Datasets candidatos, não verificados como disponíveis nesta etapa:

1. Indicadores industriais candidatos
   - Produção industrial por setor.
   - Índices de manufatura.
   - Utilização de capacidade industrial.
   - Dados de comércio, produção ou estoques setoriais.
   - Fontes candidatas:
     - agências estatísticas nacionais;
     - bancos centrais;
     - FRED;
     - OECD;
     - World Bank;
     - Eurostat;
     - IBGE, se o recorte for Brasil.

2. Variáveis financeiras candidatas
   - Índices setoriais de ações.
   - Taxas de juros.
   - Spreads de crédito.
   - Câmbio.
   - Commodities relevantes.
   - Volatilidade de mercado.
   - Fontes candidatas:
     - bancos centrais;
     - FRED;
     - Yahoo Finance ou Stooq, se apropriado;
     - bolsas ou provedores oficiais;
     - bases públicas de preços.

3. Substrato textual opcional para Fine-Tuning
   - Relatórios industriais.
   - Comunicados de empresas.
   - releases de indicadores econômicos.
   - notícias econômicas rotuladas.
   - documentos regulatórios.
   - Uso permitido somente se:
     - houver rótulos confiáveis;
     - a tarefa for definida antes;
     - o conjunto de teste for separado temporalmente ou por fonte.

Plano de seleção:

- Escolher primeiro dados tabulares públicos e reproduzíveis.
- Evitar dados proprietários na primeira execução.
- Registrar exatamente:
  - fonte;
  - URL ou identificador estável;
  - data de acesso;
  - frequência temporal;
  - período coberto;
  - transformações aplicadas;
  - limitações conhecidas.
- Tratar todos os datasets acima como candidatos até verificação de disponibilidade, qualidade e licenciamento.

metrics and baselines

Métricas de validade estatística:

- Correlação Pearson e Spearman.
- Intervalos de confiança.
- p-values ajustados para múltiplas comparações.
- Erro fora da amostra:
  - MAE;
  - RMSE;
  - MAPE, se apropriado.
- R² fora da amostra, se regressão for usada.
- Estabilidade temporal:
  - desempenho por janela;
  - degradação entre treino e validação;
  - mudança de coeficientes.
- Testes de defasagem:
  - correlação cruzada;
  - regressões com lags pré-definidos;
  - teste de causalidade de Granger somente como evidência limitada, não como prova causal.

Métricas de auditabilidade:

- Percentual de afirmações com fonte ou marcação explícita como inferência/assunção.
- Percentual de transformações de dados registradas.
- Existência de pré-registro antes da análise confirmatória.
- Número de decisões metodológicas rastreáveis.
- Número de riscos identificados antes da execução.
- Presença de controles documentados contra:
  - vazamento temporal;
  - drift;
  - múltiplas comparações;
  - correlações espúrias.
- Reprodutibilidade mínima:
  - outro operador consegue reconstruir fontes, transformações e análises a partir dos registros.

Baselines sem LLM obrigatórios:

1. Baseline estatístico simples
   - Correlação Pearson/Spearman.
   - Regressão linear com variáveis pré-definidas.
   - Validação temporal fora da amostra.

2. Baseline BI
   - Dashboard ou relatório tabular com:
     - séries temporais alinhadas;
     - matriz de correlação;
     - gráficos de dispersão;
     - análise de defasagens pré-definidas.
   - Sem uso de LLM para seleção ou interpretação automática.

3. Baseline nulo
   - Permutação temporal ou embaralhamento restrito.
   - Séries financeiras deslocadas de forma inválida como controle negativo.
   - Comparação contra variável industrial não relacionada, se disponível.

Baselines para Fine-Tuning, se usado:

- Regras manuais ou regex.
- Modelo base sem Fine-Tuning.
- Classificador tradicional, por exemplo logistic regression, SVM ou árvore simples, se a representação permitir.
- Fine-Tuned model somente na subtarefa rotulada.

controls and failure cases

Controles contra vazamento temporal:

- Separar dados por tempo:
  - treino/exploração em janela anterior;
  - validação em janela posterior.
- Proibir uso de dados futuros em normalização, imputação ou seleção de variáveis.
- Calcular estatísticas de escala ou transformação somente na janela de treino quando aplicável.
- Para textos, garantir que documentos posteriores à data alvo não entrem no treino.

Controles contra drift:

- Avaliar desempenho por subperíodos.
- Comparar coeficientes ou rankings de correlação entre janelas.
- Medir queda de desempenho entre validação inicial e validação posterior.
- Marcar achados como instáveis se dependerem de uma única janela temporal.

Controles contra múltiplas comparações:

- Pré-definir número máximo de variáveis e lags.
- Corrigir p-values com Benjamini-Hochberg ou Bonferroni.
- Reportar número total de testes.
- Separar análise exploratória de análise confirmatória.
- Não selecionar apenas os melhores resultados sem penalização.

Controles contra correlação espúria:

- Usar controles negativos.
- Testar variáveis embaralhadas ou defasagens impossíveis.
- Verificar sensibilidade a transformações alternativas.
- Exigir plausibilidade econômica/industrial documentada como hipótese, não como prova.
- Comparar contra baseline nulo.
- Evitar linguagem causal salvo se houver desenho causal apropriado.

Failure cases explícitos:

- Dados candidatos não estão disponíveis ou não têm qualidade mínima.
- Frequências temporais não podem ser alinhadas sem distorção excessiva.
- Resultados estatísticos desaparecem após ajuste por múltiplas comparações.
- Correlações só aparecem com lags escolhidos retrospectivamente.
- Desempenho fora da amostra é pior que baseline nulo ou ingênuo.
- Harness aumenta documentação, mas não permite auditoria real das decisões.
- Fine-Tuning é avaliado sem rótulos confiáveis.
- Fine-Tuning melhora métrica local, mas não melhora rastreabilidade, validade ou utilidade da investigação.
- Evidência literária permanece apenas preliminar e insuficiente para sustentar claims fortes.

support criteria

A hipótese revisada recebe suporte limitado se todos os critérios abaixo forem observados:

1. Auditabilidade
   - O Harness registra fontes, decisões, transformações, riscos e incertezas de modo mais completo que o baseline estatístico/BI simples.
   - As afirmações finais distinguem Evidence, Inference, Assumption e Open question.
   - Um Evidence Auditor consegue verificar a origem da maioria das afirmações centrais.
   - O fluxo por papéis identifica pelo menos alguns riscos metodológicos antes da interpretação final.

2. Validade estatística
   - Pelo menos uma correlação ou relação candidata pré-registrada mantém sinal consistente na janela de validação.
   - O resultado sobrevive a ajuste por múltiplas comparações ou é corretamente rebaixado para achado exploratório.
   - O desempenho fora da amostra supera baseline nulo ou ingênuo em métrica pré-definida.
   - Os controles negativos não produzem resultados comparáveis aos achados principais.

3. Separação correta entre Harness e Fine-Tuning
   - Fine-Tuning, se avaliado, é restrito a uma subtarefa rotulada.
   - Fine-Tuning não é apresentado como alternativa ao Harness.
   - O valor do Harness é avaliado como governança metodológica/auditabilidade, não como substituição de análise estatística.

4. Utilidade operacional
   - O processo gera uma lista clara de achados suportados, achados enfraquecidos e perguntas abertas.
   - O processo permite decidir se vale ampliar a investigação.

weaken criteria

A hipótese revisada é enfraquecida se ocorrer um ou mais dos seguintes casos:

- O Harness melhora a organização textual, mas não melhora a rastreabilidade metodológica.
- As decisões críticas continuam implícitas ou não auditáveis.
- Os resultados estatísticos são frágeis, mas o Harness não impede interpretação excessiva.
- O baseline estatístico/BI sem LLM já fornece documentação suficiente para a finalidade do experimento.
- O fluxo por papéis adiciona custo sem identificar riscos novos.
- As correlações candidatas são instáveis entre janelas temporais.
- Os achados dependem fortemente de transformações ou lags escolhidos após observar os dados.
- Fine-Tuning melhora uma métrica de subtarefa, mas não contribui para a investigação principal.
- A literatura disponível permanece preliminar e não permite defender plausibilidade forte das relações testadas.

falsify criteria

A hipótese revisada deve ser considerada falsificada, para este MVE, se qualquer condição abaixo ocorrer:

1. Falsificação da utilidade metodológica do Harness
   - O Harness não melhora auditabilidade em relação ao baseline sem LLM segundo as métricas pré-definidas.
   - As decisões, fontes e transformações não podem ser reconstruídas por outro operador.
   - O Harness falha em separar evidência de inferência e assunção.
   - O Harness promove ou preserva conclusões estatísticas inválidas sem sinalizar fragilidade.

2. Falsificação da validade exploratória
   - Nenhuma relação pré-registrada supera baseline nulo ou ingênuo fora da amostra.
   - Todos os achados desaparecem após controle de múltiplas comparações.
   - Controles negativos geram resultados tão fortes quanto os resultados principais.
   - Evidência de vazamento temporal é encontrada e não pode ser corrigida.

3. Falsificação da tese sobre Fine-Tuning como componente auxiliar
   - Não existe dado rotulado suficiente para a subtarefa escolhida e, ainda assim, Fine-Tuning seria necessário para sustentar a proposta.
   - Fine-Tuning só funciona quando treinado/testado com vazamento temporal ou rótulos inconsistentes.
   - Fine-Tuning não supera baseline simples na subtarefa rotulada.
   - O experimento só parece promissor quando Fine-Tuning é tratado indevidamente como substituto do Harness.

resource estimate

Escopo mínimo recomendado:

- Duração: 3 a 7 dias úteis para uma primeira execução limpa.
- Pessoas/papéis:
  - Research Lead: 0,5 dia.
  - Literature Scout: 0,5 a 1 dia, com literatura tratada como preliminar.
  - Methodology Reviewer: 0,5 dia.
  - Devil's Advocate: 0,5 dia.
  - Angel Advocate: 0,5 dia.
  - Argument Arbiter: 0,25 dia.
  - Evidence Auditor: 0,5 dia.
  - Experiment Designer: 0,5 dia.
  - Research Scribe: 0,25 dia.
- Engenharia/dados:
  - 1 a 2 dias para obtenção, limpeza e alinhamento de dados.
  - 0,5 a 1 dia para baseline estatístico/BI.
  - 0,5 a 1 dia para documentação auditável e checagens.
- Fine-Tuning:
  - 0 dias se não houver dados rotulados adequados.
  - 1 a 3 dias adicionais se houver dataset rotulado pequeno e tarefa bem definida.
- Computação:
  - Baseline estatístico/BI: laptop comum ou ambiente Python/R local.
  - Fine-Tuning: opcional; pode exigir GPU ou API externa, dependendo do modelo e tamanho do dataset.
- Risco principal:
  - Maior risco está em qualidade/alinhamento dos dados e em evitar interpretações excessivas, não em modelagem avançada.

next implementation steps

1. Research Lead
   - Definir escopo mínimo:
     - período temporal;
     - 2 a 4 indicadores industriais candidatos;
     - 2 a 4 variáveis financeiras candidatas;
     - lags permitidos;
     - critérios confirmatórios.

2. Literature Scout
   - Buscar literatura preliminar sobre relações entre os indicadores escolhidos.
   - Registrar fontes, queries, data de busca e limitações.
   - Não tratar literatura como evidência forte até full-paper review.

3. Methodology Reviewer
   - Revisar desenho de validação temporal.
   - Confirmar que não há vazamento temporal.
   - Confirmar correção para múltiplas comparações.
   - Confirmar separação entre análise exploratória e confirmatória.

4. Pipeline de dados
   - Verificar disponibilidade real dos datasets candidatos.
   - Registrar fonte, período, frequência e licença.
   - Alinhar frequência temporal.
   - Definir tratamento de missing values antes de testar correlações.

5. Baseline sem LLM
   - Executar análise estatística/BI.
   - Registrar matriz de correlação, regressões simples, validação temporal e controles negativos.

6. Harness metodológico
   - Executar o mesmo caso usando fluxo por papéis oficiais.
   - Registrar entradas e saídas por papel.
   - Medir auditabilidade separadamente da validade estatística.

7. Fine-Tuning opcional
   - Verificar se existe dataset rotulado.
   - Se não existir, declarar Fine-Tuning fora do escopo do MVE.
   - Se existir, escolher uma subtarefa concreta e comparar contra baseline simples.

8. Evidence Auditor
   - Verificar se cada claim tem fonte, resultado computado ou marcação explícita como inferência/assunção.
   - Bloquear conclusões fortes quando a evidência for preliminar.

9. Argument Arbiter
   - Comparar suporte, enfraquecimento e falsificação.
   - Decidir entre:
     - pass;
     - revise_search;
     - revise_defense;
     - revise_hypothesis;
     - pause.

Evidence

- A decisão do Argument Arbiter foi revise_hypothesis.
- O Evidence Auditor recomendou prosseguir somente com a hipótese revisada e tratá-la como metodológica e exploratória, não como conclusão.
- A hipótese revisada separa explicitamente Harness de Fine-Tuning: Fine-Tuning não é alternativa direta ao Harness, mas pode ser componente auxiliar em subtarefas específicas.
- As restrições exigem baseline estatístico/BI sem LLM.
- As restrições exigem medir validade estatística separadamente de auditabilidade.
- As restrições exigem controles contra vazamento temporal, drift, múltiplas comparações e correlações espúrias.
- As restrições exigem critérios de falsificação definidos antes da execução.
- As restrições exigem que literatura seja tratada como preliminar até full-paper review.

Inference

- O experimento deve avaliar primariamente governança metodológica e auditabilidade, não performance de LLM.
- O baseline sem LLM é necessário para distinguir valor metodológico do Harness de análises estatísticas convencionais.
- A validade estatística dos achados pode falhar mesmo que o Harness seja útil como camada auditável.
- A auditabilidade do Harness pode falhar mesmo que alguma correlação estatística pareça promissora.
- Fine-Tuning só é experimentalmente relevante se houver dados rotulados e subtarefa objetiva.
- A hipótese revisada será mais defensável se os resultados forem apresentados como suporte limitado, enfraquecimento ou falsificação, não como prova geral.

Assumption

- Será possível encontrar pelo menos alguns dados públicos candidatos para variáveis financeiras e industriais.
- Será possível construir uma divisão temporal treino/validação adequada.
- As fontes candidatas terão frequência temporal compatível ou ajustável sem distorção excessiva.
- O operador aceitará uma primeira execução pequena, exploratória e metodológica.
- Métricas simples de auditabilidade serão suficientes para comparar Harness versus baseline sem LLM no MVE.
- Dados rotulados para Fine-Tuning podem não existir; nesse caso, Fine-Tuning deve ser excluído ou apenas especificado como futura etapa condicionada.

Open question

- Quais indicadores industriais e variáveis financeiras específicas serão escolhidos?
- Qual recorte geográfico será usado: Brasil, EUA, União Europeia, global ou setor específico?
- Qual horizonte temporal mínimo será considerado aceitável?
- Qual frequência será usada: diária, mensal, trimestral?
- Quais datasets públicos têm qualidade e licença adequadas?
- Existe dataset rotulado real para alguma subtarefa de Fine-Tuning?
- Quem será o auditor independente da reprodutibilidade e auditabilidade?
- Qual limiar quantitativo será adotado para dizer que auditabilidade melhorou?
- O objetivo final é suporte acadêmico, decisão interna de P&D ou protótipo operacional?

instruction for Research Scribe

Registrar que a hipótese deve permanecer revisada, exploratória e metodológica. Não registrar como conclusão que o Harness descobre correlações válidas nem que Fine-Tuning é necessário. Registrar como conclusão durável apenas o desenho experimental: comparar Harness contra baseline estatístico/BI sem LLM, medir validade estatística separadamente de auditabilidade, usar controles contra vazamento temporal, drift, múltiplas comparações e correlações espúrias, e avaliar Fine-Tuning somente em subtarefas rotuladas quando dados existirem.
