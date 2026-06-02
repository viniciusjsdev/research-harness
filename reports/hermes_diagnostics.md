# Hermes Diagnostics

## 2026-06-02 - Oneshot Skill Request Not Followed

Evidence:

- Hermes was launched from the harness workspace with:

```bash
export HERMES_HOME="$HOME/Hermes/.hermes"
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes --oneshot "<prompt>"
```

- First prompt asked Hermes to read the harness and return a generic `SKILL.md`
  proposal for reframing research projects centered too heavily on a technique,
  tool, or specific solution.
- Constraint in the first prompt: do not edit files; return a `SKILL.md`
  proposal and objective criteria for evaluating the skill.
- Hermes instead returned a repository summary and ended with:

```text
Estou pronto para continuar como Research Lead ou no papel que você quiser.
```

- Second prompt explicitly requested:

```text
Retorne somente uma proposta de SKILL.md. Nao resuma o repositorio. Nao diga que esta pronto.
```

- Hermes instead returned:

```text
Você quer que eu retorne o quê exatamente?
```

Inference:

- Hermes failed to follow a direct artifact-generation instruction in
  non-interactive `--oneshot` mode.
- The failure is not a domain-bias failure yet, because Hermes did not reach the
  skill content stage.
- The immediate risk is that Codex cannot reliably use short non-interactive
  Hermes calls for skill drafting without a tighter interaction protocol.

Assumption:

- The prompt text reached Hermes, because Hermes responded semantically to the
  task context rather than failing with a CLI/provider error.
- The failure may be related to Hermes session/task-completion behavior in
  `--oneshot`, not to the harness instructions themselves.

Open question:

- Would the same prompt succeed in the interactive Hermes terminal where the
  user can paste the prompt and Hermes can maintain a visible conversation?
- Would a shorter prompt that avoids "read the harness" and supplies the exact
  desired output skeleton reduce ambiguity?

Remediation:

- Prefer interactive Hermes for skill-generation tasks until `--oneshot` is
  proven reliable for artifact generation.
- When using `--oneshot`, request a very small artifact first, such as only the
  YAML frontmatter and section headings.
- If Hermes asks for clarification after an explicit prompt, record the failure
  and either switch to interactive mode or ask the user for permission to use a
  stricter prompt.
