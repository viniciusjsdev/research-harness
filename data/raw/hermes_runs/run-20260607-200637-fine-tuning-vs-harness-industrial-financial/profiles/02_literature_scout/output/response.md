role name:
Literature Scout

task summary:
Revisar os artefatos de busca já gerados para a run `run-20260607-200637-fine-tuning-vs-harness-industrial-financial`, seguindo `AGENTS.md`, `docs/nomenclature.md` e `prompts/source_policy.md`, para mapear evidência preliminar sobre a comparação entre Fine-Tuning e abordagens de Harness/RAG/tool-use/text-to-SQL/BI em contextos financeiro e industrial, especialmente para descoberta de correlações entre domínios a partir de bases de dados.

input artifacts reviewed:
- `prompts/source_policy.md`
- `docs/nomenclature.md`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/01_research_lead/output/response.md`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/02_literature_scout/artifacts/literature/20260607-171835-fine-tuning-versus-retrieval-augmented-generation-financial-question-answering-t.json`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/02_literature_scout/artifacts/literature/20260607-171835-llm-agents-tool-use-data-analysis-text-to-sql-business-intelligence-benchmark.json`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/02_literature_scout/artifacts/literature/20260607-171835-industrial-fault-diagnosis-financial-impact-machine-learning-dataset.json`
- `data/raw/hermes_runs/run-20260607-200637-fine-tuning-vs-harness-industrial-financial/profiles/02_literature_scout/artifacts/literature/20260607-172244-llm-statistical-analysis-correlation-discovery-tabular-data-limitations.json`

exact sources searched:
- OpenAlex, via `scripts/search_literature.py`, as recorded in the generated JSON artifacts.
- arXiv, via `scripts/search_literature.py`, as recorded in the generated JSON artifacts.

exact queries used:
1. `fine-tuning versus retrieval augmented generation financial question answering tabular data`
2. `LLM agents tool use data analysis text-to-SQL business intelligence benchmark`
3. `industrial fault diagnosis financial impact machine learning dataset`
4. `LLM statistical analysis correlation discovery tabular data limitations`

search date:
- 2026-06-07
- Artifact timestamps:
  - 2026-06-07T20:18:35Z for queries 1, 2, and 3.
  - 2026-06-07T20:22:44Z for query 4.

candidate papers/sources table:

| # | Title | Authors available in artifact | Year | Venue/source | DOI or stable URL | Role classification | Relevance confidence | Relation to hypothesis | Limitation |
|---|---|---|---:|---|---|---|---|---|---|
| 1 | Optimizing Retrieval Strategies for Financial Question Answering Documents in Retrieval-Augmented Generation Systems | Sejong Kim; Hyunseo Song; Hyunwoo Seo; Hyunjun Kim | 2025 | arXiv | http://arxiv.org/abs/2503.15191v1 | Direct candidate: finance + RAG | High | Preliminary evidence that RAG in finance depends strongly on retrieval strategy, especially for 10-K reports with domain vocabulary and hierarchical tabular data. This is directly relevant to a Harness/RAG alternative to fine-tuning for financial QA. | Abstract-only evidence. Does not directly compare against fine-tuning. Finance-only, not industrial. Focus is QA/retrieval, not correlation discovery. |
| 2 | Meta-aware Learning in text-to-SQL Large Language Model | Wenda Zhang | 2025 | arXiv | http://arxiv.org/abs/2505.18929v1 | Direct candidate: fine-tuning/text-to-SQL/business database | Medium-high | Preliminary evidence that fine-tuning can integrate domain knowledge, schema, chain-of-thought traces, and metadata relationships for SQL generation in business applications. Relevant as a fine-tuning-side comparator against harness/tool-use. | Abstract-only evidence. Not specifically finance or industrial. No verified metrics from artifact. Needs full paper review before claims about superiority. |
| 3 | SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs | Yu Guo; Dong Jin; Shenghao Ye; Shuangwu Chen; Jian Yang; Xiaobin Tan | 2025 | arXiv / Findings ACL 2025 per DOI | DOI: 10.18653/v1/2025.findings-acl.443; URL: http://arxiv.org/abs/2505.13725v1 | Direct candidate: text-to-SQL fine-tuning/data synthesis | Medium-high | Preliminary evidence that text-to-SQL performance can be improved by synthetic data with SQL syntax constraints and SQL-to-question reverse translation. Relevant to evaluating whether fine-tuning/data generation improves structured-data access. | Abstract-only evidence. Does not address finance-industrial correlation discovery. Needs methods, datasets, and metrics checked. |
| 4 | Business Logic-Driven Text-to-SQL Data Synthesis for Business Intelligence | Jinhui Liu; Ximeng Zhang; Yanbo Ai; Zhou Yu | 2026 | arXiv | http://arxiv.org/abs/2601.14518v1 | Direct candidate: BI/text-to-SQL benchmark/data synthesis | Medium-high | Preliminary evidence that private BI settings need realistic, domain-specific synthetic evaluation data grounded in business personas, workflows, and business reasoning complexity. Relevant to Harness evaluation for enterprise analytics. | Future-dated 2026 artifact; must be treated cautiously and verified. Abstract-only evidence. Not finance/industrial-specific unless full paper confirms. |
| 5 | Agent Bain vs. Agent McKinsey: A New Text-to-SQL Benchmark for the Business Domain | Yue Li; Ran Tao; Derek Hommel; Yusuf Denizay Dönder; Sungyong Chang; David Mimno; Unso Eun Seo Jo | 2025 | arXiv | http://arxiv.org/abs/2510.07309v4 | Direct candidate: business-domain text-to-SQL benchmark | High | Preliminary evidence that business-domain text-to-SQL needs evaluation beyond simple data access, including complex responses such as predictions or recommendations. Relevant to a Harness for BI-style correlation/prediction tasks. | Future-dated 2025 artifact and abstract-only evidence. Does not directly compare fine-tuning versus harness. Needs benchmark details and task definitions. |
| 6 | The Rise and Potential of Large Language Model Based Agents: A Survey | Zhiheng Xi et al. | 2023 | arXiv / OpenAlex | DOI: 10.48550/arxiv.2309.07864; URL: https://openalex.org/W4386794445 | Background: LLM agents/tool-use/harness framing | Medium | Provides conceptual background for agentic systems that sense, decide, and act. Relevant to defining “Harness” as tool-using/orchestrated systems rather than model-only fine-tuning. | Survey-level and broad. Not specific to finance, industry, or correlation discovery. Abstract-only evidence from artifact. |
| 7 | AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges | Ranjan Sapkota; Konstantinos I. Roumeliotis; Manoj Karkee | 2025 | SuperIntelligence - Robotics - Safety & Alignment / OpenAlex | DOI: 10.70777/si.v2i3.15161; URL: https://openalex.org/W4412505619 | Background: taxonomy of agents | Low-medium | May help distinguish modular AI agents from broader agentic AI systems, relevant to operationalizing “Harness.” | Broad conceptual review. Not directly tied to datasets, finance, industrial analytics, or fine-tuning comparisons. Abstract-only evidence. |
| 8 | Are We Asking the Right Questions? On Ambiguity in Natural Language Queries for Tabular Data Analysis | Daniel Gomm; Cornelius Wolff; Madelon Hulsebos | 2025 | arXiv | http://arxiv.org/abs/2511.04584v4 | Contradictory/risk evidence: tabular QA ambiguity | High | Preliminary evidence that natural language interfaces to tabular data face ambiguity in user queries and that evaluations across 15 datasets may have uncontrolled ambiguity. Relevant as a methodological risk for Harness/text-to-SQL/BI systems. | Abstract-only evidence. Future-dated 2025 artifact. Does not directly evaluate finance/industrial correlation tasks. |
| 9 | Universal Embeddings of Tabular Data | Astrid Franz; Frederik Hoppe; Marianne Michaelis; Udo Göbel | 2025 | arXiv | http://arxiv.org/abs/2507.05904v1 | Related method: tabular/industrial data representation | Medium | Preliminary evidence that industrial relational data can be embedded for task-independent downstream analysis. Relevant to locating cross-domain relations from tables, possibly as a non-LLM or hybrid baseline. | Abstract-only evidence. Not about LLMs, fine-tuning, RAG, or finance. Needs validation details. |
| 10 | A survey on concept drift adaptation | João Gama; Indrė Žliobaitė; Albert Bifet; Mykola Pechenizkiy; Abdelhamid Bouchachia | 2014 | ACM Computing Surveys | DOI: 10.1145/2523813; URL: https://openalex.org/W2099419573 | Methodological risk/baseline: changing relations over time | High | Evidence that input-target relationships can change over time, directly relevant to financial-industrial correlation work where regimes, markets, sensors, and operations drift. | Not LLM-specific. Does not compare fine-tuning versus harness. Needs Methodology Reviewer to translate into evaluation design. |
| 11 | Changing Data Sources in the Age of Machine Learning for Official Statistics | Cedric De Boom; Michael Reusens | 2023 | arXiv | http://arxiv.org/abs/2306.04338v1 | Methodological risk: data source instability | Medium | Preliminary evidence that changing data sources create risks for ML-driven statistics. Relevant to correlation discovery across heterogeneous financial/industrial databases. | Abstract-only evidence. Official statistics context, not finance/industrial AI specifically. |
| 12 | Bearing fault diagnosis based on domain adaptation using transferable features under different working conditions | Zhe Tong; Wei Li; Bo Zhang; Meng Zhang | 2018 | arXiv | http://arxiv.org/abs/1806.01512v1 | Industrial ML candidate: domain adaptation/fault diagnosis | Medium-high | Preliminary evidence that industrial fault diagnosis suffers from distribution differences between training and test conditions and may use transfer/domain adaptation. Relevant to industrial-side model adaptation and domain shift. | Abstract-only evidence. Does not link to financial impact except general mention of financial losses. Not LLM/fine-tuning/harness. |
| 13 | A Survey on the Explainability of Supervised Machine Learning | Nadia Burkart; Marco F. Huber | 2021 | Journal of Artificial Intelligence Research | DOI: 10.1613/jair.1.12228; URL: https://openalex.org/W3101981467 | Governance/risk evidence | Medium | Evidence that black-box supervised ML explainability is important in sensitive areas such as finance. Relevant to defensibility, auditability, and governance in comparing fine-tuned models versus auditable harness pipelines. | General supervised ML survey, not LLM-specific. Abstract-only evidence from artifact. |
| 14 | Explainable Artificial Intelligence (XAI) 2.0: A manifesto of open challenges and interdisciplinary research directions | Luca Longo et al. | 2024 | Information Fusion | DOI: 10.1016/j.inffus.2024.102301; URL: https://openalex.org/W4391848979 | Governance/risk evidence | Medium | Preliminary evidence that black-box AI explainability remains an open challenge in real-world applications. Relevant to financial/industrial defensibility. | Broad XAI manifesto. Not directly about fine-tuning, RAG, or correlation discovery. Abstract-only evidence. |
| 15 | A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications | Pranab Sahoo; Ayush Singh; Sriparna Saha; Vinija Jain; Samrat Mondal; Aman Chadha | 2024 | arXiv / OpenAlex | DOI: 10.48550/arxiv.2402.07927; URL: https://openalex.org/W4391833078 | Background comparator: prompting without parameter updates | Medium | Preliminary evidence that prompts can adapt LLM behavior without changing model parameters. Relevant as a baseline against fine-tuning and as a component of Harness. | Survey-level. Not finance/industrial-specific. Does not address correlation discovery. |
| 16 | Tree of Reviews: A Tree-based Dynamic Iterative Retrieval Framework for Multi-hop Question Answering | Li Jiapeng; Liu Runze; Li Yabo; Zhou Tong; Li Mingling; Chen Xiang | 2024 | arXiv | http://arxiv.org/abs/2404.14464v1 | RAG risk/variant: dynamic retrieval for multi-hop QA | Low-medium | Preliminary evidence that retrieval-augmented reasoning can suffer from irrelevant retrieved paragraphs and cascading errors; relevant to Harness risk analysis. | Multi-hop QA, not finance/industrial/tabular/correlation. Abstract-only evidence. |
| 17 | An Exploration of Data Augmentation and Sampling Techniques for Domain-Agnostic Question Answering | Shayne Longpre; Yi Lu; Zhucheng Tu; Chris DuBois | 2019 | arXiv | http://arxiv.org/abs/1912.02145v1 | Indirect comparator: QA adaptation/data sampling | Low-medium | Shows that sampling/data augmentation strategies can matter in QA adaptation. Indirectly relevant to model adaptation. | Pre-LLM-era or not specifically RAG/fine-tuning comparison. Not finance/industrial. |
| 18 | Large language models for generative information extraction: a survey | Derong Xu; Wei Chen; Wenjun Peng; Chao Zhang; Tong Xu; Xiangyu Zhao; Xian Wu; Yefeng Zheng; Yan Wang; Enhong Chen | 2024 | Frontiers of Computer Science | DOI: 10.1007/s11704-024-40555-y; URL: https://openalex.org/W4404239715 | Related task: extraction from text into structure | Medium | Relevant if the Harness uses LLMs to extract structured variables from financial/industrial documents before statistical analysis. | Not about correlation discovery itself. Survey-level and abstract-only evidence. |

weak matches and near misses:
- `Survey of the State of the Art in Natural Language Generation` is broad NLG background and only weakly related.
- `Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology` is a strong example of a tool-using autonomous agent in a high-stakes domain, but biomedical/oncology rather than finance/industrial.
- `AI deception: A survey of examples, risks, and potential solutions` is relevant to AI risk governance but not specifically to the research objective.
- `When LLMs meet cybersecurity: a systematic literature review` is mostly off-domain.
- `Generative AI in Medical Practice` and `Generative AI for Transformative Healthcare` are off-domain healthcare sources; may only be useful as analogical risk literature.
- `Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data`, `Data Encoding for Byzantine-Resilient Distributed Optimization`, and `Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data` are not relevant to the current objective despite keyword overlap.
- `The role of artificial intelligence in achieving the Sustainable Development Goals`, `Deep Learning: A Comprehensive Overview`, `Ensemble deep learning`, and `Particle Swarm Optimization Algorithm and Its Applications` are too broad for the specific comparison.

search failures or evidence gaps:
- Search failure:
  No directly matching paper was found in these artifacts that compares “fine-tuning versus harness” for financial-industrial cross-domain correlation discovery from databases. This suggests the exact framing may be under-supported in the searched sources, but it does not prove novelty.
- Evidence gap:
  The artifacts do not provide a direct benchmark comparing:
  - fine-tuned LLMs
  - RAG
  - tool-using agents
  - text-to-SQL pipelines
  - statistical/BI baselines
  on the same financial-industrial correlation-discovery task.
- Evidence gap:
  The finance-related RAG result is about financial question answering over documents such as 10-K reports, not correlation discovery across financial and industrial datasets.
- Evidence gap:
  The industrial result most relevant to fault diagnosis is about bearing fault diagnosis/domain adaptation, not linking industrial events to financial outcomes.
- Evidence gap:
  The text-to-SQL/BI results are relevant to database access and enterprise analytics, but the artifacts do not establish whether they discover statistically valid correlations or merely answer structured queries.
- Evidence gap:
  No artifact establishes that LLMs alone are reliable for statistical correlation discovery. The available tabular-analysis ambiguity paper points instead to evaluation and query-specification risks.
- Evidence gap:
  No verified metrics, datasets, or baselines were extracted from full papers in this step. Most evidence is metadata/abstract-only and must be treated as preliminary.

Evidence:
- Evidence:
  The Research Lead framed the question as comparing Fine-Tuning and Harness for AI in financial and industrial contexts, focused on locating correlations between domains from databases.
- Evidence:
  The reviewed search artifacts were generated from OpenAlex and arXiv using four exact queries listed above.
- Evidence:
  The finance/RAG query returned a directly relevant arXiv result: `Optimizing Retrieval Strategies for Financial Question Answering Documents in Retrieval-Augmented Generation Systems`, whose abstract states that RAG performance in finance depends on retrieval and that 10-K reports include domain-specific vocabulary and multi-hierarchical tabular data.
- Evidence:
  The text-to-SQL/BI query returned several relevant candidates: `Meta-aware Learning in text-to-SQL Large Language Model`, `SQLForge`, `Business Logic-Driven Text-to-SQL Data Synthesis for Business Intelligence`, and `Agent Bain vs. Agent McKinsey`.
- Evidence:
  The industrial query returned `Bearing fault diagnosis based on domain adaptation using transferable features under different working conditions`, whose abstract states that bearing failure can cause financial losses or casualties and that variable working conditions cause distribution differences between training and test sets.
- Evidence:
  The tabular/statistical query returned `Are We Asking the Right Questions? On Ambiguity in Natural Language Queries for Tabular Data Analysis`, whose abstract states that natural language interfaces to tabular data must handle query ambiguity and reports analysis across 15 datasets.
- Evidence:
  The artifact set contains governance/methodology sources on explainability, concept drift, changing data sources, and XAI that are relevant to defensibility and validity but not direct comparisons of fine-tuning versus harness.
- Evidence:
  Several results are broad, off-domain, or weak matches; they should not be promoted as support for the central hypothesis.

Inference:
- Inference:
  The strongest directly relevant cluster from the reviewed artifacts is not “fine-tuning versus harness” as a binary comparison, but three adjacent literatures:
  1. RAG for financial document QA.
  2. text-to-SQL/BI agents and data synthesis for business analytics.
  3. methodological risks in tabular analysis, concept drift, ambiguity, and domain shift.
- Inference:
  A Harness approach may be easier to defend methodologically than fine-tuning alone if the task requires auditable database access, retrieval provenance, SQL execution, statistical tests, and logs; however, this remains a hypothesis, not a conclusion proven by the reviewed sources.
- Inference:
  Fine-tuning appears more directly supported for subcomponents such as text-to-SQL, metadata/schema learning, and domain-specific SQL reasoning than for end-to-end correlation discovery.
- Inference:
  Industrial-financial cross-domain correlation discovery likely needs explicit statistical baselines and time-aware validation because concept drift, source changes, working-condition shifts, and query ambiguity can produce invalid or non-reproducible conclusions.
- Inference:
  The most defensible next methodological framing is not “Which is better: fine-tuning or harness?” but “Which architecture best supports validated, auditable correlation discovery under heterogeneous data, domain shift, and business/industrial constraints?”

Assumption:
- Assumption:
  The JSON artifacts accurately reflect the OpenAlex/arXiv searches performed by Codex.
- Assumption:
  The abstracts included in the artifacts are sufficient for preliminary triage but not sufficient for final claims about methods, results, or comparative performance.
- Assumption:
  “Harness” in this run refers to an orchestrated architecture or research/evaluation pipeline including RAG, tool-use, text-to-SQL, statistical validation, provenance, and logs, rather than only this repository’s workflow harness.
- Assumption:
  “Financial and industrial context” includes enterprise databases, financial documents/reports, production/maintenance datasets, and business intelligence workflows unless later narrowed by the Research Lead.
- Assumption:
  “Locate correlations” requires statistical validation, not merely natural-language explanation or SQL retrieval.

Open question:
- Open question:
  Is the intended comparison architectural, empirical, or operational?
  - architectural: fine-tuned model versus orchestrated harness design
  - empirical: benchmark performance on datasets
  - operational: auditability, cost, latency, governance, maintainability
- Open question:
  What dataset substrate will define the minimum viable experiment?
  - public financial filings plus industrial production indicators
  - synthetic BI database
  - maintenance/fault dataset with cost labels
  - macroeconomic/industrial production/market data
- Open question:
  Which task should be evaluated?
  - financial QA
  - text-to-SQL accuracy
  - correlation discovery
  - hypothesis generation
  - causal explanation
  - dashboard/BI automation
- Open question:
  What baselines are mandatory?
  - manual SQL/BI
  - classical statistics
  - AutoML/tabular ML
  - prompting-only LLM
  - RAG-only
  - fine-tuned text-to-SQL
  - agent/harness with tools
- Open question:
  Which metrics matter most?
  - SQL execution accuracy
  - factuality
  - correlation validity
  - false discovery rate
  - statistical power
  - reproducibility
  - auditability
  - cost
  - latency
  - human review burden
- Open question:
  Are correlation claims required to handle time lag, seasonality, autocorrelation, concept drift, and confounders?
- Open question:
  Should Methodology Reviewer treat finance and industry as two domains to be joined, or as two application contexts evaluated separately?

recommendation for Methodology Reviewer:
- Treat the current evidence base as preliminary and abstract-level.
- Do not accept any claim that fine-tuning or harness is superior overall.
- Evaluate the problem as a task decomposition:
  1. data ingestion and provenance
  2. schema understanding
  3. variable extraction
  4. SQL/database access
  5. statistical correlation testing
  6. confounder/time-series controls
  7. explanation/reporting
  8. auditability and reproducibility
- Require an empirical comparison matrix with at least:
  - fine-tuned text-to-SQL or domain-adapted LLM
  - RAG/prompting baseline
  - tool-using Harness with SQL/statistical tools
  - non-LLM statistical/BI baseline
- Require the next role to distinguish:
  - evidence for data access/query generation
  - evidence for domain adaptation
  - evidence for valid statistical discovery
  - evidence for governance/auditability
- Recommend additional searches before final argument:
  - `FinQA retrieval augmented generation fine-tuning financial question answering`
  - `TAT-QA large language model financial tabular question answering fine-tuning`
  - `Spider text-to-SQL fine-tuning retrieval augmented generation benchmark`
  - `business intelligence text-to-SQL benchmark large language model`
  - `LLM tabular data analysis benchmark statistical reasoning`
  - `industrial maintenance financial loss predictive maintenance dataset machine learning`
  - `correlation discovery time series financial industrial production machine learning`
  - `spurious correlations financial time series machine learning validation`
- Methodology Reviewer should likely recommend `revise_search` unless the next stage is explicitly scoped as a preliminary methodology design rather than a literature-supported conclusion.
