# Nomenclature

This document defines the official terms used by the Research Harness.

## Harness

A harness is the structured research environment around the agent.

It includes:

- role prompts
- workflow rules
- source policy
- schemas
- scripts
- versioned memory
- report templates

The harness does not replace the agent. It guides the agent.

## Runtime

The runtime is the tool that executes the workflow.

For this project, Hermes Agent is the intended runtime, but the harness can evolve without Hermes installed.

## Versioned Memory

Versioned memory is durable project knowledge stored in `memory/`.

It includes:

- hypotheses
- decisions
- concepts
- reading log
- claims

This is different from the agent's private/local memory.

## Roles

Roles are technical lenses used by the same agent or by multiple agents.

They are not fictional personalities. Each role has a job, output standard, and failure mode.

| Role | Official Purpose |
| --- | --- |
| Research Lead | Owns the investigation flow and decides the next role. |
| Literature Scout | Searches scientific sources and records search provenance. |
| Methodology Reviewer | Reviews methods, metrics, datasets, baselines, and validity. |
| Devil's Advocate | Attacks the hypothesis like a strict reviewer. |
| Angel Advocate | Builds the strongest technically honest defense. |
| Argument Arbiter | Compares Devil's Advocate and Angel Advocate, then passes or sends the work back. |
| Evidence Auditor | Verifies that claims are supported by real sources or clearly marked as missing. |
| Experiment Designer | Converts uncertainty into minimum viable experiments. |
| Research Scribe | Updates versioned memory with durable conclusions. |

## Argument Review Loop

The Argument Review Loop is the core reasoning cycle.

```text
Research Lead
  -> Literature Scout
  -> Methodology Reviewer
  -> Devil's Advocate
  -> Angel Advocate
  -> Argument Arbiter
      -> pass
      -> revise_search
      -> revise_defense
      -> revise_hypothesis
      -> pause
  -> Evidence Auditor
  -> Experiment Designer
  -> Research Scribe
```

The loop does not require perfection. It requires a solid, honest argumentative base.

## Search Failure

A search failure is a first-class research finding.

It means:

```text
The harness searched specific sources with specific queries and did not find adequate evidence.
```

It does not mean:

```text
No prior work exists.
The idea is novel.
The thesis is true.
```

When search failure matters, use `templates/search_failure_note.md`.

## Evidence Language

Use these labels consistently:

- `Evidence`: verified source or observed result.
- `Inference`: reasoning drawn from evidence.
- `Assumption`: necessary condition not yet proven.
- `Open question`: unresolved uncertainty.
- `Search failure`: documented absence of adequate evidence in searched sources.

## Decision Language

Use these Argument Arbiter decisions:

- `pass`: solid enough to move forward.
- `revise_search`: literature base is too weak or search trail is incomplete.
- `revise_defense`: defense does not answer major objections.
- `revise_hypothesis`: hypothesis framing is too weak, broad, or unsupported.
- `pause`: not worth advancing until external conditions change.
