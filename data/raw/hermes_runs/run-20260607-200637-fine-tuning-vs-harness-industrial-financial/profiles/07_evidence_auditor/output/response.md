role name:
Evidence Auditor

task summary:
Auditar as claims produzidas até a etapa do Argument Arbiter na run `run-20260607-200637-fine-tuning-vs-harness-industrial-financial`, verificando se estão apoiadas por evidência real, se foram corretamente marcadas como Evidence, Inference, Assumption ou Open question, e se a decisão `revise_hypothesis` é compatível com a força da evidência disponível.

input artifacts reviewed:
- `AGENTS.md`
- `docs/nomenclature.md`
- `prompts/source_policy.md`
- `profiles/01_research_lead/output/response.md`
- `profiles/02_literature_scout/output/response.md`
- `profiles/03_methodology_reviewer/output/response.md`
- `profiles/04_devils_advocate/output/response.md`
- `profiles/05_angel_advocate/output/response.md`
- `profiles/06_argument_arbiter/output/response.md`

claim-by-claim audit:

1. Claim:
Fine-Tuning e Harness não são categorias simétricas.

Status:
Supported.

Evidence strength:
medium.

Evidence:
- `docs/nomenclature.md` define Harness como ambiente estruturado em torno do agente, com prompts, regras, source policy, schemas, scripts, versioned memory e templates.
- Methodology Reviewer, Devil's Advocate, Angel Advocate e Argument Arbiter convergem nessa distinção.
- Fine-Tuning foi tratado nos papéis anteriores como técnica de adaptação de modelo, não como arquitetura metodológica completa.

Audit:
A claim está adequadamente suportada como distinção conceitual dentro do harness. Não depende de paper externo. Pode ser mantida.

2. Claim:
Nenhum paper diretamente comparando Fine-Tuning versus Harness para descoberta de correlações financeiro-industriais foi encontrado nos artefatos OpenAlex/arXiv revisados.

Status:
Supported, with limits.

Evidence strength:
medium.

Evidence:
- Literature Scout registrou buscas em OpenAlex e arXiv com quatro queries explícitas.
- Literature Scout declarou search failure para a comparação exata.
- Source policy permite tratar ausência documentada como achado limitado.

Audit:
A claim é válida apenas como “não encontrado nos artefatos revisados”. Não pode ser convertida em “não existe literatura” ou “a proposta é nova”.

Required qualifier:
“Nos artefatos revisados de OpenAlex/arXiv, não foi encontrado paper diretamente correspondente.”

3. Claim:
A evidência disponível é preliminar e majoritariamente metadata/abstract-only.

Status:
Supported.

Evidence strength:
medium.

Evidence:
- Literature Scout marcou repetidamente os candidatos como abstract-only.
- Methodology Reviewer e Argument Arbiter incorporaram esse limite.
- Não houve revisão integral de métodos, datasets, métricas e resultados dos papers citados.

Audit:
A claim está corretamente formulada. Deve continuar explícita em qualquer etapa posterior.

4. Claim:
Não há suporte para alegação de superioridade geral de Harness sobre Fine-Tuning.

Status:
Supported.

Evidence strength:
strong.

Evidence:
- Literature Scout não encontrou benchmark direto.
- Methodology Reviewer declarou que nenhuma abordagem está validada como superior.
- Devil's Advocate rejeitou qualquer superioridade sem dataset, baselines e métricas.
- Angel Advocate explicitamente recusou alegar superioridade geral.
- Argument Arbiter exigiu remoção ou marcação de claims de superioridade.

Audit:
Claim bem suportada. Qualquer claim de superioridade deve ser removida ou marcada como hipótese não comprovada.

5. Claim:
Harness pode servir como camada metodológica auditável para exploração, validação e documentação de correlações entre bases financeiras e industriais.

Status:
Assumption-level / partially supported as methodological plausibility.

Evidence strength:
weak to medium.

Evidence:
- `docs/nomenclature.md` apoia a ideia de Harness como estrutura metodológica em torno do agente.
- AGENTS.md exige rastreabilidade, papéis, source policy, schemas e separação entre evidência e inferência.
- Methodology Reviewer e Angel Advocate argumentaram que logs, ferramentas estatísticas, validação temporal e auditoria são metodologicamente adequados.

Inference:
É plausível que um Harness seja adequado para organizar e auditar um processo de pesquisa.

Audit:
A parte “camada metodológica auditável” é suportada conceitualmente pelo próprio harness. A parte “para exploração, validação e documentação de correlações financeiro-industriais” ainda depende de um desenho experimental concreto. Não há evidência empírica de que o Harness funcione bem nessa tarefa específica.

Required qualifier:
“Pode ser avaliado como camada metodológica auditável” é aceitável.
“Serve” ou “melhora” sem experimento é forte demais.

6. Claim:
Fine-Tuning não é alternativa direta ao Harness, mas pode ser componente auxiliar em subtarefas específicas.

Status:
Supported as conceptual reframing; assumption-level for task-specific usefulness.

Evidence strength:
medium.

Evidence:
- Methodology Reviewer tratou Fine-Tuning como técnica e Harness como processo/arquitetura.
- Literature Scout encontrou evidência adjacente em text-to-SQL, BI e extração, mas não em correlação financeiro-industrial end-to-end.
- Angel Advocate e Argument Arbiter convergiram na reformulação híbrida.

Audit:
A primeira parte é bem suportada: Fine-Tuning não é alternativa direta ao Harness. A segunda parte é plausível, mas ainda precisa de subtarefas definidas, dados de treino, labels e métricas.

Required qualifier:
“Pode ser avaliado como componente auxiliar” está adequado.
“É útil” ainda seria overclaim.

7. Claim:
Fine-Tuning pode ajudar em extração de variáveis, normalização semântica, text-to-SQL ou classificação de eventos.

Status:
Assumption-level, with adjacent support.

Evidence strength:
weak to medium.

Evidence:
- Literature Scout identificou candidatos de text-to-SQL/BI e informação estruturada.
- Methodology Reviewer considerou Fine-Tuning plausivelmente viável para subtarefas.
- Nenhum resultado completo de paper foi auditado para demonstrar ganho nesses subtasks no domínio financeiro-industrial específico.

Audit:
A claim é aceitável se formulada como hipótese de componente auxiliar. Não está provada para o objetivo central da run.

Required qualifier:
“Subtarefas candidatas para avaliação incluem...” em vez de “Fine-Tuning melhora...”.

8. Claim:
Descoberta de correlações financeiro-industriais exige estatística, validação temporal, controle de confundidores, controle de múltiplas comparações e baselines não-LLM.

Status:
Supported as methodological requirement.

Evidence strength:
medium to strong.

Evidence:
- AGENTS.md exige métricas, baselines, risco metodológico e mínimo experimento viável.
- Methodology Reviewer detalhou ameaças à validade estatística.
- Devil's Advocate listou riscos de leakage, drift, sazonalidade, defasagens, múltiplas hipóteses e correlação espúria.
- Argument Arbiter tornou esses controles obrigatórios antes de avanço.

Audit:
A claim é metodologicamente sólida. Embora não esteja ancorada em revisão completa de literatura estatística nesta run, é uma exigência científica razoável e consistente com o contrato do repositório.

9. Claim:
Baselines estatísticos e não-LLM são obrigatórios.

Status:
Supported.

Evidence strength:
strong.

Evidence:
- Methodology Reviewer declarou a obrigatoriedade.
- Devil's Advocate listou baselines estatísticos, ML não-LLM, BI, humanos e negativos.
- Angel Advocate aceitou esses baselines como condição.
- Argument Arbiter exigiu Pearson/Spearman, correlação defasada, Granger ou teste temporal apropriado, modelo estatístico/ML simples e pipeline sem LLM.

Audit:
Claim fortemente suportada dentro do fluxo. Deve ser preservada como requisito antes do Experiment Designer.

10. Claim:
Um Harness reduz falsos positivos ou melhora validade estatística.

Status:
Unsupported if stated as fact; assumption-level if stated as design goal.

Evidence strength:
weak.

Evidence:
- Devil's Advocate alertou que logs podem documentar erros sem corrigi-los.
- Angel Advocate concedeu que Harness não reduz falso positivo automaticamente.
- Argument Arbiter disse que a defesa é parcialmente plausível, mas abstrata.

Audit:
Essa claim não deve aparecer como conclusão. O máximo permitido é:
“Um Harness pode ser desenhado para impor controles contra falso positivo, mas isso precisa ser testado.”

11. Claim:
Rastreabilidade/auditabilidade aumenta defensibilidade.

Status:
Partially supported as inference; not equivalent to validity.

Evidence strength:
medium.

Evidence:
- AGENTS.md e docs/nomenclature.md sustentam um workflow estruturado, versionado e auditável.
- Devil's Advocate e Angel Advocate concordam que rastreabilidade não garante validade.
- Angel Advocate defende que trilhas de auditoria facilitam reconstrução, contestação e falsificação.

Audit:
Claim aceitável se limitada à auditabilidade/defensibilidade processual. Overextended se convertida em “resultados mais corretos”.

Required qualifier:
“Facilita auditoria e falsificação” em vez de “garante validade”.

12. Claim:
A literatura adjacente justifica um MVE.

Status:
Inference, not direct evidence.

Evidence strength:
weak to medium.

Evidence:
- Literature Scout encontrou clusters adjacentes: financial RAG/QA, text-to-SQL/BI, agents/tool-use, tabular ambiguity, concept drift, industrial domain adaptation, XAI/governance.
- Nenhum cluster responde diretamente à hipótese central.

Audit:
A claim é razoável como inferência programática: há material suficiente para desenhar um experimento mínimo. Não é suporte para conclusão de desempenho.

13. Claim:
A ausência de paper direto sugere lacuna de pesquisa.

Status:
Overextended unless carefully qualified.

Evidence strength:
weak.

Evidence:
- Source policy diz que ausência de resultados não prova inexistência, novidade ou verdade da tese.
- Literature Scout pesquisou apenas OpenAlex e arXiv nos artefatos revisados, com quatro queries.

Audit:
Pode-se dizer:
“Os artefatos revisados não trouxeram suporte direto para essa formulação.”
Não se deve dizer:
“Há uma lacuna comprovada” ou “a ideia é nova”.

14. Claim:
A hipótese original deve ser revisada.

Status:
Supported.

Evidence strength:
strong.

Evidence:
- Methodology Reviewer mostrou que a pergunta é ampla e carece de dataset, métrica e baseline.
- Devil's Advocate recomendou weak reject.
- Angel Advocate aceitou reformulação.
- Argument Arbiter decidiu `revise_hypothesis`.

Audit:
A decisão do Argument Arbiter é bem suportada. A hipótese revisada deve substituir a formulação binária original.

evidence strength:
weak overall for empirical claims.
medium for conceptual/methodological claims.
strong for the procedural conclusion `revise_hypothesis`.

unsupported claims:
- Que Harness é superior a Fine-Tuning para descoberta de correlações financeiro-industriais.
- Que Harness melhora validade estatística ou reduz falso positivo sem protocolo formal.
- Que Fine-Tuning é útil para esta tarefa sem subtarefa, dados de treino, labels e métrica.
- Que a abordagem é nova.
- Que evidência adjacente de RAG financeiro, text-to-SQL/BI ou agentes sustenta diretamente a hipótese central.
- Que LLMs são necessários ou superiores para localizar correlações entre bases financeiras e industriais.
- Que auditabilidade implica correção analítica.
- Que a ausência de papers diretos em OpenAlex/arXiv prova lacuna consolidada na literatura.

overextended interpretations:
- Tratar financial QA/RAG como evidência para descoberta de correlação financeiro-industrial.
- Tratar text-to-SQL/BI como evidência de validade estatística de correlações.
- Tratar industrial fault diagnosis/domain adaptation como evidência de relação entre eventos industriais e impacto financeiro.
- Tratar XAI/governance como prova de que Harness é metodologicamente superior.
- Tratar logs e rastreabilidade como controle suficiente contra p-hacking, leakage, drift ou falso positivo.
- Tratar Fine-Tuning isolado como concorrente direto de uma arquitetura completa de Harness.
- Tratar “não encontrado nos artefatos” como “não existe trabalho relacionado”.

unverifiable references:
- Não identifiquei referência claramente inventada nos resumos revisados.
- Porém, a maioria das referências citadas pelo Literature Scout foi auditada apenas por metadados/abstracts nos artefatos, não por revisão integral dos papers.
- Métodos, datasets, métricas e resultados dos papers citados permanecem não verificados para uso como suporte forte.
- Papers com URLs/DOIs estáveis podem ser citados apenas com limitações explícitas: “metadata/abstract-only evidence”.
- Qualquer claim sobre desempenho, superioridade, benchmark ou resultado específico desses papers deve aguardar leitura do texto completo.

required fixes before finalization:
1. Substituir a hipótese original binária por formulação assimétrica:
   Harness como camada metodológica/auditável; Fine-Tuning como possível componente auxiliar.

2. Remover claims de superioridade, novidade ou aplicabilidade ampla.

3. Marcar toda evidência de literatura atual como preliminar e abstract-only, salvo onde full paper for revisado.

4. Definir substrato experimental mínimo:
   - dataset financeiro;
   - dataset industrial;
   - chave ou regra de alinhamento;
   - granularidade temporal;
   - janelas e defasagens;
   - critério de validação.

5. Definir tarefa exata:
   - descoberta exploratória de correlação;
   - validação confirmatória;
   - previsão;
   - text-to-SQL;
   - extração/normalização;
   - classificação de eventos;
   - ou BI assistido.

6. Definir baselines obrigatórios:
   - pipeline estatístico/BI sem LLM;
   - correlação Pearson/Spearman/Kendall;
   - correlação com defasagem;
   - teste temporal apropriado, como Granger se aplicável;
   - modelo estatístico ou ML tabular simples;
   - prompting-only;
   - RAG/tool-use simples;
   - componente fine-tuned apenas se houver subtarefa supervisionada adequada;
   - placebo/permutação temporal.

7. Definir controles:
   - split temporal;
   - holdout confirmatório;
   - correção para múltiplas comparações;
   - controle de leakage;
   - análise de drift;
   - estabilidade por janela;
   - ablação dos componentes do Harness.

8. Separar métricas por subtarefa:
   - SQL execution accuracy;
   - erro de schema/join;
   - precisão/recall/F1 de extração;
   - taxa de falso positivo;
   - false discovery rate;
   - estabilidade out-of-sample;
   - auditabilidade;
   - reprodutibilidade;
   - custo total;
   - esforço humano de revisão.

Evidence:
- AGENTS.md exige análise estruturada, separação entre Evidence, Inference, Assumption e Open question, e proíbe inventar referências.
- docs/nomenclature.md define Harness e os papéis oficiais, incluindo Evidence Auditor.
- prompts/source_policy.md estabelece que ausência de resultados não prova novidade, inexistência ou veracidade.
- Literature Scout registrou buscas em OpenAlex e arXiv, mas não encontrou paper diretamente correspondente à comparação exata.
- Literature Scout marcou a evidência como preliminar e majoritariamente metadata/abstract-only.
- Methodology Reviewer declarou que Fine-Tuning e Harness não são categorias simétricas.
- Methodology Reviewer declarou que dataset/substrato, métricas e baselines estão insuficientes.
- Devil's Advocate recomendou weak reject por falsa dicotomia, ausência de evidência direta, falta de dataset e risco metodológico.
- Angel Advocate aceitou reformular a tese e recusou alegar superioridade geral.
- Argument Arbiter decidiu `revise_hypothesis`.

Inference:
- A formulação original não é auditavelmente defensável como comparação científica direta.
- A hipótese revisada é mais honesta porque transforma Fine-Tuning em componente possível, não rival direto do Harness.
- A evidência atual é suficiente para desenhar um MVE, mas insuficiente para qualquer claim de desempenho.
- A contribuição mais defensável neste estágio é metodológica: estruturar um protocolo auditável de comparação.
- O risco principal é confundir plausibilidade arquitetural com validação empírica.

Assumption:
- “Harness” nesta run significa camada/processo metodológico com recuperação, ferramentas, logs, validação estatística e auditoria.
- “Fine-Tuning” significa adaptação de modelo para subtarefas delimitadas, não um sistema completo de descoberta estatística.
- O domínio financeiro-industrial envolverá dados heterogêneos e provavelmente temporais.
- Existe ou pode ser construído um substrato mínimo público, sintético ou híbrido para avaliação.
- A tarefa de “localizar correlações” exige validação estatística, não apenas geração de hipóteses plausíveis.

Open question:
- Quais datasets financeiros e industriais serão usados?
- Qual é a unidade de análise: firma, setor, planta, produto, commodity, região ou indicador macro?
- A relação buscada é correlação contemporânea, defasada, sinal preditivo, relação causal ou hipótese exploratória?
- Haverá ground truth, oracle humano, dados sintéticos com correlações conhecidas ou validação retrospectiva?
- Fine-Tuning será avaliado em qual subtarefa supervisionada?
- O Harness poderá incluir um modelo fine-tuned ou a comparação exige separação estrita?
- Qual métrica primária decidirá sucesso ou falha?
- Qual nível de falso positivo é aceitável?
- Que resultado falsificaria a hipótese revisada?
- A literatura deve ser ampliada para Semantic Scholar, Crossref, ACL/ACM/IEEE/publisher pages antes de qualquer claim de lacuna?

recommendation for Experiment Designer:
Prosseguir somente com a hipótese revisada e tratá-la como hipótese metodológica exploratória, não como conclusão.

O Experiment Designer deve:
1. Definir um MVE com dataset/substrato explícito.
2. Incluir pelo menos um baseline estatístico/BI sem LLM.
3. Avaliar Fine-Tuning apenas em subtarefas concretas, se houver dados rotulados suficientes.
4. Medir validade estatística separadamente de auditabilidade.
5. Incluir controles contra leakage temporal, drift, múltiplas comparações e correlação espúria.
6. Definir critérios de falsificação antes da execução.
7. Manter todos os claims de literatura como preliminares até revisão de full papers.
