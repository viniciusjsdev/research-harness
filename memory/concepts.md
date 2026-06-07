# Concepts

Use this file for durable concepts, definitions, and domain vocabulary.

## Template

```text
Concept:
Definition:
Why it matters:
Related concepts:
Sources:
```

## Harness As Methodological Layer

Definition:
A structured research process around an agent that coordinates roles, source discipline, schemas, scripts, logging, validation, auditability and promotion rules.

Why it matters:
This is not equivalent to a model adaptation technique. In financial-industrial correlation research, the Harness should be evaluated for methodological control and auditability, not as a direct substitute for statistical analysis.

Related concepts:
Research Harness, Evidence Auditor, Argument Arbiter, Experiment Designer, RAG, tool-use, text-to-SQL, BI baseline.

Sources:
`docs/nomenclature.md`; `run-20260607-200637-fine-tuning-vs-harness-industrial-financial`.

## Fine-Tuning As Auxiliary Component

Definition:
Model adaptation for a concrete labeled subtask, such as extraction, normalization, classification or text-to-SQL, when sufficient training data and evaluation metrics exist.

Why it matters:
Fine-Tuning should not be framed as a direct alternative to a Harness. It may be evaluated inside or beside a Harness only when the subtask, labels, baselines and metrics are explicit.

Related concepts:
Domain adaptation, supervised fine-tuning, text-to-SQL, extraction, classification, Harness As Methodological Layer.

Sources:
`run-20260607-200637-fine-tuning-vs-harness-industrial-financial`.
