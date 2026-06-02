# Reading Log

Curate papers here after search results have been reviewed. Raw search outputs belong in `data/raw/`.

## Template

```text
Paper ID:
Title:
Authors:
Year:
Venue:
DOI/URL:
Status: unread | skimmed | read | rejected
Why it matters:
Core claim:
Method:
Datasets/sample:
Metrics:
Findings:
Limitations:
Supports:
Contradicts:
Notes:
```

## 2026-06-02 Preliminary sources for HYP-0002

Paper ID: FINQA-2021
Title: FinQA: A Dataset of Numerical Reasoning over Financial Data
Authors: Chen et al. (metadata from OpenAlex; full author list not yet curated)
Year: 2021
Venue: EMNLP
DOI/URL: https://doi.org/10.18653/v1/2021.emnlp-main.300
Status: skimmed
Why it matters: Candidate evidence for financial numerical reasoning benchmark.
Core claim: Provides a dataset for numerical reasoning over financial data.
Method: Dataset/benchmark paper.
Datasets/sample: Financial documents/tables; details require full read.
Metrics: Not yet curated.
Findings: Not yet curated.
Limitations: Does not by itself cover industrial failure or operational-financial linkage.
Supports: Financial QA component of HYP-0002.
Contradicts: Does not support claims about industrial causality.
Notes: Preliminary metadata-level evidence only.

Paper ID: RAG-2020
Title: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
Authors: Lewis et al. (metadata from OpenAlex; full author list not yet curated)
Year: 2020
Venue: not yet curated
DOI/URL: https://openalex.org/W3098425262
Status: skimmed
Why it matters: Foundational source for retrieval-augmented generation.
Core claim: Combines retrieval with generation for knowledge-intensive tasks.
Method: RAG architecture/evaluation; details require full read.
Datasets/sample: Not yet curated.
Metrics: Not yet curated.
Findings: Not yet curated.
Limitations: RAG does not automatically solve structured calculation or auditability.
Supports: Retrieval layer of HYP-0002.
Contradicts: Does not support RAG-only sufficiency for the proposed task.
Notes: Preliminary metadata-level evidence only.

Paper ID: TOOLFORMER-2023
Title: Toolformer: Language Models Can Teach Themselves to Use Tools
Authors: Schick et al. (metadata from OpenAlex; full author list not yet curated)
Year: 2023
Venue: arXiv / related venue metadata not yet curated
DOI/URL: https://doi.org/10.48550/arxiv.2302.04761
Status: skimmed
Why it matters: Supports the general line of LLMs using external tools.
Core claim: Language models can learn/use external tools.
Method: Tool-use approach; details require full read.
Datasets/sample: Not yet curated.
Metrics: Not yet curated.
Findings: Not yet curated.
Limitations: Not specific to industrial-financial decision support.
Supports: Tool/calc orchestration premise of HYP-0002.
Contradicts: Does not prove Harness superiority.
Notes: Preliminary metadata-level evidence only.

Paper ID: BIRD-2023
Title: Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs
Authors: Li et al. (metadata from OpenAlex; full author list not yet curated)
Year: 2023
Venue: arXiv / benchmark paper metadata not yet curated
DOI/URL: https://doi.org/10.48550/arxiv.2305.03111
Status: skimmed
Why it matters: Candidate baseline/evaluation reference for text-to-SQL and database-grounded questions.
Core claim: Evaluates LLMs as database interfaces over large-scale DB-grounded text-to-SQL tasks.
Method: Benchmark paper; details require full read.
Datasets/sample: BIRD benchmark; details require full read.
Metrics: Not yet curated.
Findings: Not yet curated.
Limitations: SQL correctness is not the same as financial impact reasoning.
Supports: SQL/Data Warehouse evaluation component of HYP-0002.
Contradicts: Does not support claims about industrial-financial causal estimation.
Notes: Preliminary metadata-level evidence only.

Paper ID: BEARING-BENCHMARK-2016
Title: Condition Monitoring of Bearing Damage in Electromechanical Drive Systems by Using Motor Current Signals of Electric Motors: A Benchmark Data Set for Data-Driven Classification
Authors: Not yet curated
Year: 2016
Venue: PHM Society European Conference
DOI/URL: https://doi.org/10.36001/phme.2016.v3i1.1577
Status: skimmed
Why it matters: Example of industrial condition/fault benchmark.
Core claim: Provides benchmark data for bearing damage condition monitoring/classification.
Method: Dataset/benchmark paper; details require full read.
Datasets/sample: Motor current signals for electromechanical drive systems.
Metrics: Not yet curated.
Findings: Not yet curated.
Limitations: Does not include financial impact data.
Supports: Industrial fault/condition-monitoring substrate for HYP-0002.
Contradicts: Does not support financial impact validation.
Notes: Preliminary metadata-level evidence only.

