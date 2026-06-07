role name: Devil's Advocate

task summary:
Atacar a hipótese de que um Harness é mais defensável que Fine-Tuning como ponto de partida para descoberta e validação de correlações entre domínios financeiro e industrial, considerando qualidade analítica, rastreabilidade, custo, adaptabilidade, risco operacional e defensibilidade metodológica.

input artifacts reviewed:
- AGENTS.md fornecido no contexto da sessão.
- docs/nomenclature.md.
- prompts/source_policy.md.
- Research Lead summary.
- Literature Scout summary.
- Methodology Reviewer summary.

top rejection risks:
1. Categorias mal definidas:
   Fine-Tuning e Harness não são alternativas equivalentes. Fine-Tuning é uma técnica de adaptação de modelo; Harness é um arranjo metodológico, operacional e instrumental em torno do agente. Compará-los diretamente pode gerar uma falsa dicotomia.

2. Hipótese ampla demais:
   A hipótese combina múltiplos eixos — qualidade analítica, rastreabilidade, custo, adaptabilidade, risco operacional, defensibilidade — sem especificar tarefa, dados, horizonte temporal, métrica ou critério de vitória.

3. Ausência de evidência direta:
   O Literature Scout não encontrou paper diretamente comparando Fine-Tuning versus Harness para descoberta de correlações financeiro-industriais. A base atual é adjacente e preliminar, em parte metadata/abstract-only.

4. Risco de confundir correlação operacional com descoberta científica:
   Um Harness pode melhorar rastreabilidade e auditoria, mas isso não implica que ele descubra correlações mais válidas, menos espúrias ou mais úteis que outros métodos.

5. Falta de substrato experimental:
   Sem datasets definidos, variáveis-alvo, granularidade temporal, controles, baselines e ground truth, a hipótese não é testável de forma defensável.

6. Risco de supervalorizar LLMs:
   A descoberta de correlações tabulares, financeiras e industriais pode ser melhor resolvida por estatística clássica, econometria, séries temporais, causal discovery, feature engineering e modelos não-LLM.

7. Problema de validade externa:
   Mesmo que Harness vença em um caso, isso pode não generalizar entre setores industriais, tipos de dados financeiros, frequências temporais, regimes macroeconômicos ou níveis de ruído.

weakest assumptions:
1. Assumption:
   Rastreabilidade do Harness se traduz em maior validade analítica.

   Attack:
   Logs, recuperação, consultas e auditoria registram o processo, mas não garantem que as correlações encontradas sejam estatisticamente válidas, estáveis ou causalmente interpretáveis.

2. Assumption:
   Fine-Tuning é menos defensável para descoberta de correlações.

   Attack:
   Isso depende da formulação. Fine-Tuning pode ser inadequado para cálculo estatístico direto, mas pode ser útil para extração semântica, normalização de entidades, mapeamento de indicadores, classificação de eventos industriais, geração de features textuais ou interpretação de relatórios. O argumento precisa separar descoberta estatística de preparação e interpretação dos dados.

3. Assumption:
   Harness é ponto de partida superior porque combina ferramentas.

   Attack:
   Combinar ferramentas aumenta capacidade, mas também aumenta superfície de erro: falhas de recuperação, seleção enviesada de fontes, prompts instáveis, bugs em pipelines, leakage temporal, consultas incorretas e automação de decisões frágeis.

4. Assumption:
   A comparação pode ser feita no nível “Fine-Tuning versus Harness”.

   Attack:
   A comparação correta provavelmente é entre pipelines específicos:
   - estatística/econometria tradicional;
   - RAG + ferramentas estatísticas;
   - agente com ferramentas e logs;
   - modelo fine-tuned para extração ou classificação;
   - modelo fine-tuned + ferramentas;
   - pipeline híbrido com validação humana.

5. Assumption:
   Correlações financeiro-industriais são um problema primariamente de IA.

   Attack:
   Pode ser primariamente um problema de dados, identificação, causalidade, calendário, defasagens temporais, normalização setorial, regime econômico e controle de múltiplas hipóteses.

6. Assumption:
   Custo e adaptabilidade favorecem Harness.

   Attack:
   Um Harness robusto pode exigir manutenção contínua, integração com múltiplas fontes, observabilidade, versionamento, testes, controle de acesso, governança e validação. Fine-Tuning pode ser caro inicialmente, mas barato em inferência se o escopo for estreito e repetitivo.

missing baselines:
1. Baselines estatísticos obrigatórios:
   - correlação de Pearson/Spearman/Kendall com correção para múltiplas comparações;
   - regressão linear/regularizada;
   - VAR/VECM quando séries temporais forem cointegradas;
   - Granger causality com validação temporal;
   - cross-correlation com defasagens;
   - modelos ARIMA/SARIMAX;
   - modelos de painel se houver múltiplas firmas/setores;
   - bootstrap/permutation tests;
   - false discovery rate control.

2. Baselines de machine learning não-LLM:
   - random forest;
   - gradient boosting/XGBoost/LightGBM;
   - elastic net;
   - causal forests quando apropriado;
   - change point detection;
   - anomaly detection;
   - clustering temporal/setorial;
   - modelos de feature selection.

3. Baselines de informação e recuperação:
   - busca lexical/SQL direta;
   - dashboards BI tradicionais;
   - pipelines ETL + notebooks;
   - knowledge graph sem LLM;
   - regras de domínio escritas por especialistas.

4. Baselines LLM específicos:
   - zero-shot prompting;
   - few-shot prompting;
   - RAG simples;
   - agente com ferramentas estatísticas;
   - Fine-Tuning para extração/classificação;
   - Fine-Tuning + RAG;
   - Fine-Tuning + tools;
   - Harness com e sem agente autônomo.

5. Baselines humanos:
   - analista financeiro/industrial usando SQL/notebook;
   - equipe de BI usando dashboard;
   - especialista de domínio revisando hipóteses;
   - processo manual auditável.

6. Baselines negativos:
   - dados embaralhados temporalmente;
   - pares de variáveis sem relação plausível;
   - período fora da amostra;
   - variáveis placebo;
   - setores não relacionados;
   - séries simuladas com correlação conhecida.

confounders and edge cases:
1. Leakage temporal:
   O modelo ou pipeline pode acessar informação posterior ao período analisado, produzindo correlações artificialmente fortes.

2. Regime shifts:
   Correlações financeiro-industriais podem mudar em crises, choques de commodities, mudanças regulatórias, pandemia, guerra, inflação ou política monetária.

3. Frequências incompatíveis:
   Dados industriais mensais/trimestrais e dados financeiros diários/intradiários podem gerar artefatos quando agregados incorretamente.

4. Estacionariedade:
   Séries não estacionárias podem produzir correlações espúrias.

5. Defasagens:
   Relações reais podem aparecer com delays variáveis. Uma comparação sem modelagem de lag pode penalizar métodos injustamente.

6. Seleção de variáveis:
   Um Harness com recuperação ampla pode testar muitas hipóteses e inflar falso positivo. Fine-Tuning também pode internalizar vieses de seleção do corpus.

7. Ambiguidade semântica:
   Termos industriais e financeiros podem ter significados diferentes entre setores, países, idiomas e períodos.

8. Granularidade setorial:
   Correlações agregadas por setor podem desaparecer ou inverter no nível de firma, planta, produto ou região.

9. Survivorship bias:
   Bases financeiras podem conter apenas empresas sobreviventes ou com cobertura suficiente.

10. Publication/reporting bias:
   Relatórios financeiros e industriais podem enfatizar certos eventos e omitir outros.

11. Prompt instability:
   Um Harness baseado em LLM pode variar respostas com pequenas mudanças de prompt, temperatura, modelo ou contexto recuperado.

12. Tool failure:
   Queries SQL erradas, joins incorretos, timezone incorreto, deduplicação falha ou parsing de documentos podem produzir resultados convincentes e falsos.

13. Fine-Tuning overfit:
   Um modelo fine-tuned pode memorizar padrões históricos e falhar sob drift.

14. Auditability illusion:
   Logs detalhados podem tornar uma conclusão falsa mais persuasiva sem torná-la correta.

15. Human-in-the-loop bias:
   Revisores podem aceitar correlações plausíveis narrativamente, mesmo se estatisticamente frágeis.

falsification tests:
1. Teste de validade fora da amostra:
   Treinar/configurar em um período e validar em períodos posteriores não vistos. A hipótese enfraquece se o Harness encontra correlações que não persistem fora da amostra.

2. Teste placebo:
   Rodar o Harness em variáveis embaralhadas, setores sem relação plausível ou séries simuladas independentes. A hipótese falha se ele produzir muitas correlações “explicáveis” mas falsas.

3. Teste de múltiplas hipóteses:
   Medir taxa de falso positivo após correção FDR/Bonferroni ou testes por permutação. A hipótese falha se o Harness não controlar adequadamente a inflação de descobertas.

4. Teste contra baseline estatístico simples:
   Comparar contra correlação defasada + regressão regularizada + validação temporal. A hipótese enfraquece se o Harness não melhora precisão, recall, estabilidade ou interpretabilidade em relação ao baseline.

5. Teste de reprodutibilidade:
   Reexecutar o mesmo Harness com seed, modelo, prompt e contexto controlados. A hipótese falha se resultados variam substancialmente sem justificativa metodológica.

6. Teste de ablação:
   Remover componentes do Harness: RAG, ferramenta estatística, logs, agente, validação humana. A hipótese enfraquece se a vantagem vier apenas de um componente simples, como uma consulta SQL ou notebook estatístico.

7. Teste Fine-Tuning bem especificado:
   Comparar contra Fine-Tuning aplicado a subtarefas apropriadas, como extração de eventos, normalização de entidades ou classificação de relatórios. A hipótese falha se a comparação usar um Fine-Tuning mal escolhido ou artificialmente fraco.

8. Teste de drift:
   Avaliar em períodos com mudança de regime econômico/industrial. A hipótese enfraquece se o Harness não detectar ou não se adaptar ao drift melhor que alternativas.

9. Teste de auditoria cega:
   Dar conclusões a revisores sem revelar método. A hipótese enfraquece se a suposta defensibilidade do Harness depende mais do formato do relatório do que da qualidade estatística.

10. Teste de custo total:
   Medir custo de implementação, manutenção, inferência, revisão humana, retrabalho e governança. A hipótese falha se o Harness for mais caro ou menos operacionalizável que Fine-Tuning ou pipelines tradicionais para o mesmo desempenho.

likely reviewer objections:
1. “A comparação é conceitualmente inválida: Fine-Tuning é uma técnica; Harness é uma arquitetura/processo.”

2. “O objetivo mistura descoberta de correlação, validação estatística, explicabilidade, governança e custo operacional sem uma métrica primária.”

3. “Não há dataset, tarefa, janela temporal, granularidade, variáveis ou ground truth.”

4. “A hipótese privilegia Harness antes de demonstrar que LLMs são necessários para o problema.”

5. “O trabalho ignora baselines estatísticos e econométricos que são mais naturais para correlação entre domínios.”

6. “A defesa parece baseada em plausibilidade operacional, não em evidência empírica.”

7. “Rastreabilidade não é o mesmo que validade; logs podem documentar erros.”

8. “Não está claro como controlar múltiplas comparações e correlações espúrias.”

9. “A ausência de trabalhos diretamente comparativos não prova novidade nem vantagem do Harness.”

10. “Fine-Tuning foi apresentado de forma estreita demais; ele pode compor um pipeline híbrido e não precisa competir isoladamente com Harness.”

11. “A proposta não distingue tarefas tabulares, textuais, multimodais, séries temporais e extração documental.”

12. “A hipótese não define em que condições Harness perde.”

13. “O risco operacional do Harness pode ser maior, não menor, se agentes executarem consultas, transformações e interpretações com autonomia insuficientemente controlada.”

14. “Sem avaliação prospectiva, a descoberta de correlações pode ser apenas curve fitting retrospectivo.”

Evidence:
- Evidence: AGENTS.md define que o repositório deve tratar cada objetivo como objeto temporário de análise e exige avaliação de novidade, viabilidade técnica, risco metodológico, datasets, métricas, baselines, trabalhos relacionados, evidência contraditória, defensibilidade e mínimo experimento viável.
- Evidence: docs/nomenclature.md define Harness como ambiente estruturado em torno do agente, incluindo role prompts, workflow rules, source policy, schemas, scripts, versioned memory e report templates; também afirma que o Harness não substitui o agente, mas o guia.
- Evidence: docs/nomenclature.md define Devil's Advocate como o papel que ataca a hipótese como um revisor estrito.
- Evidence: prompts/source_policy.md estabelece que falha em encontrar trabalhos relacionados não prova inexistência, novidade ou veracidade da tese.
- Evidence: O Literature Scout summary afirma que nenhum paper diretamente comparando Fine-Tuning versus Harness para descoberta de correlação financeiro-industrial foi encontrado nos artifacts revisados.
- Evidence: O Literature Scout summary afirma que a evidência é preliminar, majoritariamente metadata/abstract-only, e concentrada em clusters adjacentes como financial RAG/QA, text-to-SQL/BI, LLM agents/tool-use, tabular ambiguity, concept drift, domain adaptation, XAI/governance.
- Evidence: O Methodology Reviewer summary afirma que Fine-Tuning e Harness não são categorias simétricas.
- Evidence: O Methodology Reviewer summary afirma que correlação entre domínios exige estatística, controles, validação temporal, baselines e controle de falso positivo.
- Evidence: O Methodology Reviewer summary afirma que dataset/substrato, métricas e baselines ainda são insuficientes e que baselines não-LLM são obrigatórios.

Inference:
- Inference: A hipótese atual é fraca para revisão técnica porque está formulada em nível conceitual amplo, não em uma comparação experimental operacionalizável.
- Inference: A maior ameaça não é que Harness esteja errado, mas que a comparação esteja mal posta.
- Inference: O Harness pode ser defensável para governança, auditoria e orquestração, mas isso ainda não demonstra superioridade em descoberta válida de correlações.
- Inference: Fine-Tuning não deve ser julgado como alternativa monolítica; ele pode ser uma etapa dentro de um Harness ou pipeline híbrido.
- Inference: A falta de evidência direta torna prematura qualquer recomendação forte a favor de Harness.
- Inference: Um pipeline estatístico tradicional pode superar tanto Fine-Tuning quanto Harness se o problema for majoritariamente tabular/temporal.
- Inference: A tese só se torna defensável se for reformulada como comparação entre pipelines específicos por subtarefa.

Assumption:
- Assumption: O objetivo de “localizar correlações entre domínios” envolve dados estruturados ou semiestruturados com componente temporal.
- Assumption: O uso financeiro e industrial exige rastreabilidade, auditoria e defensibilidade por causa de risco operacional e decisão de negócio.
- Assumption: Fine-Tuning seria usado para melhorar o comportamento do modelo em tarefas específicas, não para substituir testes estatísticos formais.
- Assumption: Harness incluiria ferramentas externas, consultas, recuperação, estatística, logs e validação humana ou automatizada.
- Assumption: A comparação futura pretende informar uma decisão prática de arquitetura, não apenas uma discussão conceitual.

Open question:
- Open question: Qual é exatamente a tarefa: descoberta exploratória, validação de hipótese, previsão, explicação, monitoramento de risco, extração documental ou geração de relatórios?
- Open question: Quais bases financeiras e industriais serão usadas?
- Open question: Há ground truth de correlações conhecidas ou o experimento dependerá de validação retrospectiva?
- Open question: Qual é a unidade de análise: firma, setor, cadeia de suprimentos, commodity, região, planta, produto ou indicador macro?
- Open question: Qual é a granularidade temporal: diária, semanal, mensal, trimestral ou anual?
- Open question: Como serão tratados lags, estacionariedade, sazonalidade e regime shifts?
- Open question: Quais métricas definirão “melhor”: precisão estatística, descoberta útil, custo, tempo, auditabilidade, estabilidade, recall de hipóteses plausíveis, redução de falso positivo ou aceitação por especialistas?
- Open question: Fine-Tuning será avaliado sozinho ou como componente de pipeline?
- Open question: Harness será avaliado com quais ferramentas e quais controles de execução?
- Open question: Como impedir que o Harness gere muitas hipóteses e depois selecione narrativas plausíveis post hoc?
- Open question: O domínio exige explicação causal ou apenas correlação preditiva?
- Open question: Qual evidência contraditória seria suficiente para abandonar a hipótese?

final recommendation: weak reject

Rationale:
A hipótese é plausível como intuição operacional, mas ainda não é defensável como tese de pesquisa. O principal motivo para weak reject é a assimetria conceitual entre Fine-Tuning e Harness, somada à ausência de evidência direta, ausência de substrato experimental e falta de baselines estatísticos obrigatórios. O caminho correto não é rejeitar definitivamente a ideia, mas exigir reformulação antes de defesa.

A formulação revisada deveria trocar:
“Harness é mais defensável que Fine-Tuning para descoberta de correlações financeiro-industriais”

por algo mais testável, como:
“Para descoberta exploratória e validação auditável de correlações em dados financeiro-industriais temporais, um pipeline Harness com recuperação, consultas controladas, testes estatísticos, logs e revisão humana reduz falso positivo e melhora rastreabilidade em comparação com prompting simples, Fine-Tuning isolado e baselines estatísticos, sob métricas pré-registradas.”

Mesmo essa versão ainda precisaria provar vantagem contra baselines não-LLM.

instruction for Angel Advocate:
Defenda a hipótese somente depois de estreitar o escopo. Não tente provar que Harness é universalmente superior a Fine-Tuning. A defesa mais forte deve argumentar que Harness é uma camada metodológica mais adequada para descoberta exploratória auditável, enquanto Fine-Tuning pode ser útil como componente auxiliar para subtarefas específicas. Responda diretamente às objeções sobre falsa dicotomia, baselines estatísticos, controle de falso positivo, validação temporal, drift, custo total e ausência de evidência direta. Use linguagem cautelosa: “mais defensável como ponto de partida sob certas condições”, não “melhor em geral”.
