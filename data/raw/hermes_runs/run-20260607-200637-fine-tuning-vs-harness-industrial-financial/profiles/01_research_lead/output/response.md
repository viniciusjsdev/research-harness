role name:
Research Lead

task summary:
Conduzir a etapa inicial de planejamento da run `run-20260607-200637-fine-tuning-vs-harness-industrial-financial`, tratando o objetivo de pesquisa como objeto temporário de análise: comparar Fine-Tuning e Harness para uso de IA em contexto financeiro e industrial, com foco em localizar correlações entre domínios a partir de bases de dados.

input artifacts reviewed:
- `AGENTS.md`
- Hermes Role Input da etapa 1
- Objetivo temporário de pesquisa fornecido pelo operador
- Contexto e restrições da run
- Nomenclatura oficial de papéis indicada em `AGENTS.md`

precise research question:
Em aplicações financeiras e industriais que buscam localizar correlações entre domínios a partir de bases de dados, quando uma abordagem baseada em Fine-Tuning supera, iguala ou perde para uma abordagem baseada em Harness — incluindo RAG, tool-use, text-to-SQL, BI ou pipelines orquestrados — em termos de qualidade analítica, rastreabilidade, custo, adaptabilidade, risco operacional e defensibilidade metodológica?

working hypothesis:
Assumption:
Para o objetivo específico de descobrir, explicar e validar correlações entre domínios financeiro-industriais, uma abordagem de Harness provavelmente será mais defensável como ponto de partida do que Fine-Tuning isolado, porque pode combinar recuperação de dados, consultas estruturadas, ferramentas estatísticas, text-to-SQL, validação de fontes, auditoria e experimentos reprodutíveis.

Assumption:
Fine-Tuning pode ser útil em componentes específicos, por exemplo: normalização de terminologia setorial, classificação de documentos, extração estruturada, interpretação de relatórios ou adaptação linguística ao domínio. Porém, ainda precisa ser comparado contra alternativas como RAG, prompting estruturado, tool-use e modelos tabulares/estatísticos tradicionais.

Assumption:
A hipótese não deve ser tratada como conclusão até que a Literature Scout documente evidência real, trabalhos relacionados, benchmarks e lacunas.

Evidence:
- O objetivo informado pelo operador é comparar Fine-Tuning e Harness para uso de IA em contexto financeiro e industrial.
- O foco declarado é localizar correlações entre domínios a partir de bases de dados.
- `AGENTS.md` exige análise fria e estruturada, separando evidência de inferência e evitando apego ao domínio temporário.
- `AGENTS.md` exige avaliar novidade, viabilidade técnica, risco metodológico, datasets, métricas, baselines, trabalhos relacionados, evidência contraditória, defensibilidade sob peer review e experimento mínimo viável.
- `AGENTS.md` exige que literatura e citações não sejam inventadas.
- Nenhuma referência bibliográfica, dataset, benchmark, DOI, métrica ou resultado empírico foi fornecido nesta etapa.

Inference:
- A comparação não deve ser formulada como “Fine-Tuning versus Harness” de modo binário ou genérico demais; a avaliação precisa distinguir tarefas específicas:
  - descoberta de correlação
  - integração de bases heterogêneas
  - extração de variáveis
  - consulta analítica
  - explicação causal ou correlacional
  - geração de relatórios
  - auditoria e rastreabilidade
- “Harness” deve ser operacionalizado como uma arquitetura ou processo experimental que pode incluir RAG, tool-use, text-to-SQL, BI, consultas SQL, notebooks, validação estatística e logs auditáveis.
- “Fine-Tuning” deve ser operacionalizado por tipo:
  - fine-tuning supervisionado para tarefas textuais
  - adaptação de domínio
  - instruction tuning
  - fine-tuning de modelos pequenos especializados
  - eventual ajuste de modelos para geração de consultas ou extração de entidades
- A pergunta central deve evitar presumir que IA descobre correlações de forma confiável sozinha. Correlação entre domínios exige estatística, controle de confundidores, avaliação temporal e validação contra baselines.
- O eixo financeiro-industrial introduz riscos metodológicos específicos: séries temporais, defasagens, sazonalidade, causalidade espúria, regimes de mercado, granularidade incompatível, dados confidenciais e vieses de disponibilidade.

Assumption:
- “Contexto financeiro e industrial” pode incluir bases como indicadores de mercado, demonstrações financeiras, produção industrial, supply chain, commodities, energia, manufatura, logística, manutenção, vendas B2B ou macroeconomia, mas o escopo exato ainda não foi fixado.
- “Localizar correlações entre domínios” pode significar correlação estatística exploratória, descoberta de sinais preditivos, mapeamento semântico entre variáveis, ou apoio a inteligência de negócio. Esses sentidos precisam ser desambiguados.
- O usuário espera que a run execute o loop oficial completo, não apenas uma opinião inicial.
- A run deve produzir materiais por papel/perfil nas etapas apropriadas, mas esta etapa específica solicitou não editar arquivos nem criar artefatos.

Open question:
- Quais domínios específicos serão comparados? Ex.: financeiro corporativo versus manutenção industrial, mercado financeiro versus produção industrial, crédito versus supply chain, commodities versus manufatura.
- Quais tipos de dados serão considerados? Ex.: tabulares, séries temporais, relatórios textuais, sensores industriais, ERPs, demonstrações financeiras, notícias, documentos regulatórios.
- O objetivo é descobrir correlações novas, explicar correlações conhecidas, automatizar BI, prever variáveis, ou apoiar decisão executiva?
- Qual é a unidade de avaliação? Dataset público, caso sintético, prova de conceito interna, benchmark acadêmico ou revisão conceitual?
- Quais métricas serão usadas?
  - precisão de extração?
  - acurácia de consultas?
  - qualidade estatística das correlações?
  - recall de hipóteses úteis?
  - custo?
  - latência?
  - auditabilidade?
  - taxa de alucinação?
  - reprodutibilidade?
- Quais baselines são obrigatórios?
  - análise estatística tradicional
  - BI/manual SQL
  - RAG sem fine-tuning
  - prompting sem RAG
  - text-to-SQL
  - modelos tabulares tradicionais
  - AutoML
- O termo “Harness” no objetivo significa especificamente este research-harness, um harness de avaliação, ou uma arquitetura de orquestração de IA?
- A comparação deve considerar restrições regulatórias financeiras e industriais, como explicabilidade, governança, privacidade e auditoria?
- Há datasets permitidos para experimento mínimo, ou a etapa inicial deve propor candidatos públicos?

role sequence for this run:
1. Research Lead
   - Refinar a pergunta, escopo, hipótese inicial, papéis, critérios e instruções.
2. Literature Scout
   - Buscar evidência em fontes acadêmicas e técnicas sobre Fine-Tuning, RAG, tool-use, text-to-SQL, BI analytics, descoberta de correlações, IA em finanças e IA industrial.
3. Methodology Reviewer
   - Avaliar desenho metodológico, métricas, baselines, riscos de validade, dados e possibilidade de experimento mínimo.
4. Devil's Advocate
   - Atacar a hipótese, especialmente quanto a novidade, utilidade de LLMs para correlação, risco de correlação espúria, falta de baselines e claims vagos.
5. Angel Advocate
   - Construir a defesa tecnicamente honesta da hipótese, usando apenas evidências encontradas e reconhecendo limitações.
6. Argument Arbiter
   - Comparar objeções e defesas, mapear lacunas e decidir entre:
     - `pass`
     - `revise_search`
     - `revise_defense`
     - `revise_hypothesis`
     - `pause`
7. Evidence Auditor
   - Verificar se todas as alegações usadas como evidência têm fonte real ou estão marcadas como inferência, hipótese, suposição ou lacuna.
8. Experiment Designer
   - Converter incertezas remanescentes em um mínimo experimento viável.
9. Research Scribe
   - Atualizar memória versionada apenas com conclusões duráveis, se a run chegar a esse ponto e se houver achados estáveis.

constraints and required artifacts:
- Não editar arquivos nesta etapa.
- Não criar artefatos nesta etapa.
- Não promover artefatos nesta etapa.
- Usar somente papéis oficiais de `docs/nomenclature.md`.
- Separar `Evidence`, `Inference`, `Assumption` e `Open question`.
- Não inventar referências, autores, DOI, URLs, métricas, resultados ou datasets.
- Não alegar novidade sem evidência de literatura.
- Tratar Fine-Tuning, Harness, RAG, tool-use, text-to-SQL, BI e correlação financeiro-industrial como objetos de análise, não como conclusões.
- Em etapas futuras da run, cada papel ativado deve registrar entrada e saída no perfil correspondente dentro de:
  `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/<role>/{input,output,artifacts}/`
- Não criar árvores paralelas de perfis.
- Não gravar segredos, tokens, dados privados ou credenciais.
- Não commitar PDFs brutos ou texto privado extraído sem aprovação explícita.
- Trabalhos usados como evidência devem capturar, quando disponíveis:
  - título
  - autores
  - ano
  - venue ou fonte
  - DOI ou URL estável
  - claim central
  - método
  - datasets ou amostra
  - métricas
  - principais achados
  - limitações
  - relação com a hipótese ativa
- Falhas de busca devem ser documentadas com:
  - fontes pesquisadas
  - queries exatas
  - data da busca
  - critérios de inclusão
  - nível de confiança
  - próximas buscas úteis

next role instruction:
Literature Scout deve executar uma busca disciplinada e documentada para mapear evidência real sobre a comparação entre Fine-Tuning e abordagens de Harness/RAG/tool-use/text-to-SQL/BI em tarefas de análise financeira, industrial e descoberta de correlações em bases de dados.

Instruções específicas para Literature Scout:
- Não tentar provar a hipótese; buscar evidência favorável, contrária e indireta.
- Separar claramente:
  - estudos sobre Fine-Tuning em domínio financeiro
  - estudos sobre Fine-Tuning em domínio industrial/manufatura
  - estudos sobre RAG/tool-use/agents/harnesses para análise de dados
  - estudos sobre text-to-SQL e BI com LLMs
  - estudos sobre descoberta de correlação, causalidade ou relações entre variáveis em bases tabulares/séries temporais
  - benchmarks ou avaliações comparando adaptação de modelo versus recuperação/ferramentas
- Usar fontes acadêmicas preferenciais:
  - OpenAlex
  - Semantic Scholar
  - arXiv
  - Crossref
  - ACL Anthology se NLP for relevante
  - PubMed ou Europe PMC apenas se surgirem casos biomédicos análogos, não como foco principal
  - páginas oficiais de datasets, benchmarks ou código quando relevantes
- Registrar queries exatas e fontes pesquisadas.
- Não inferir que ausência de resultados prova novidade.
- Quando encontrar trabalhos relevantes, capturar metadados completos e limitações.
- Procurar explicitamente evidência contraditória, por exemplo:
  - Fine-Tuning superando RAG/tool-use em tarefas específicas
  - RAG/harness falhando por baixa qualidade de recuperação
  - LLMs falhando em raciocínio estatístico ou análise tabular
  - text-to-SQL com erros em bases complexas
  - correlações espúrias em dados financeiros ou industriais
- Entregar saída estruturada para a próxima etapa, permitindo que Methodology Reviewer avalie datasets, métricas, baselines e validade.
