# Claims

Use this file to track important claims that the project may defend, weaken, or reject.

## Template

```text
Claim ID:
Text:
Type: empirical | methodological | theoretical | engineering | limitation
Status: proposed | supported | weakened | contradicted | rejected
Evidence:
Counterevidence:
Confidence: low | medium | high
Open questions:
```

## CLAIM-0001

Text:
Harness is empirically superior to Fine-Tuning for financial-industrial correlation discovery.

Type: empirical

Status: weakened

Evidence:

- Evidence Auditor in `run-20260607-200637-fine-tuning-vs-harness-industrial-financial` found no support for superiority claims.

Counterevidence:

- Literature Scout did not find a directly matching comparison in the reviewed OpenAlex/arXiv artifacts.
- Argument Arbiter decided `revise_hypothesis`, not `pass`.

Confidence: medium

Open questions:

- Would a controlled MVE show any advantage in auditability or statistical validity?

## CLAIM-0002

Text:
Harness can be evaluated as an auditable methodological layer for financial-industrial correlation research, while Fine-Tuning should be treated as an optional component for labeled subtasks.

Type: methodological

Status: proposed

Evidence:

- Argument Arbiter and Evidence Auditor supported the revised framing conceptually in `run-20260607-200637-fine-tuning-vs-harness-industrial-financial`.
- Experiment Designer proposed an MVE that measures statistical validity separately from auditability.

Counterevidence:

- No empirical MVE has been executed yet.
- Literature evidence remains preliminary and mostly metadata/abstract-only.

Confidence: medium

Open questions:

- Which dataset, baseline and auditability metric should instantiate the first MVE?
