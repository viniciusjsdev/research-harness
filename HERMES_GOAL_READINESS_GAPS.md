# Hermes Goal Readiness Gaps

Este documento explica o que ainda falta para usar
`HERMES_CODEX_KNOWLEDGE.md` como contrato principal de um Goal longo de
refinamento operacional do Hermes dentro deste research harness.

O arquivo atual ja e suficiente para iniciar uma rodada controlada. As lacunas
abaixo nao bloqueiam o primeiro teste, mas aumentam o risco de uma campanha
longa virar conversa solta, diagnostico pouco auditavel ou melhoria nao
verificavel.

## 1. Objetivo De Goal Explicito

Falta declarar o objetivo operacional do Goal em uma frase verificavel.

Sugestao:

```text
Refinar Hermes ate que ele execute uma run completa no research harness, usando
papeis oficiais, input/output por perfil, diagnostico de falhas e promocao
controlada de artefatos.
```

Motivo:

- Sem objetivo fechado, "treinar Hermes" pode significar conversar, testar
  prompts, criar skills, editar docs ou executar pesquisa.
- Um objetivo verificavel permite distinguir progresso real de interacao longa.
- O Goal precisa de uma definicao clara de sucesso para Codex saber quando
  continuar, pausar ou pedir decisao do usuario.

## 2. Criterios De Entrada

Falta declarar o que precisa estar verdadeiro antes de iniciar o Goal.

Sugestao:

- `hermes --version` funciona dentro da raiz do repo.
- Provider/modelo do Hermes esta configurado, ou a falta de provider esta
  registrada como bloqueio operacional.
- `scripts/init_hermes_run.py` cria uma run valida.
- `scripts/validate_hermes_run.py data/raw/hermes_runs/_template` passa.
- O usuario confirmou que Codex pode operar Hermes e registrar diagnosticos.

Motivo:

- Evita confundir falha de ambiente com falha do Hermes.
- Evita abrir uma campanha de refinamento quando o runtime ainda nao consegue
  chamar modelo.
- Permite que problemas de auth/provider fiquem fora do repo e fora da memoria
  duravel.

## 3. Criterios De Parada

Falta definir quando a campanha deve parar.

Sugestao:

- Parar quando uma run completa passa no validador sem erros.
- Parar quando duas ou tres rodadas consecutivas nao revelam falhas criticas
  novas.
- Parar quando Hermes repete sugestoes amplas sem evidencia nova.
- Parar quando a proxima melhoria exige decisao do usuario.
- Parar quando o bloqueio de provider/auth impedir progresso por rodadas
  consecutivas.

Motivo:

- Goals longos precisam de limite operacional.
- Sem criterio de parada, a conversa pode produzir muito texto e pouca melhoria.
- O criterio protege o repositorio contra mudancas especulativas.

## 4. Integracao Com A Base Verificavel

O arquivo atual ainda nao aponta explicitamente para os artefatos que tornam a
auditoria repetivel.

Arquivos que devem ser citados:

- `scripts/init_hermes_run.py`
- `scripts/validate_hermes_run.py`
- `docs/hermes_audit_checklist.md`
- `data/raw/hermes_runs/_template/00_metadata.json`

Motivo:

- A base verificavel ja existe e deve ser a primeira camada de controle.
- Sem esses links, Codex ou Hermes podem continuar validando manualmente o que
  ja pode ser checado por script.
- O validador ajuda a capturar erros reais, como papel fora da nomenclatura
  oficial.

## 5. Harmonizacao Do Caminho Hermes

O arquivo atual recomenda `HERMES_HOME=/mnt/c/Hermes/.hermes`. O ambiente pode
ter outros homes ou execucoes possiveis, como `~/Hermes/.hermes` ou `~/.hermes`.

Sugestao:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes --version
hermes config path
hermes config env-path
hermes status
```

E declarar:

```text
Use o HERMES_HOME confirmado pelo ambiente local. Nao copie auth, tokens ou
config privada para o repositorio.
```

Motivo:

- O caminho certo pode variar por maquina, instalacao ou perfil.
- Fixar um caminho errado faz Hermes parecer quebrado quando o problema e so
  home/config.
- O repo precisa documentar como confirmar o ambiente sem expor segredos.

## 6. Definicao Precisa De "Treinar Hermes"

Falta deixar explicito que "treinar Hermes" aqui nao significa treinar pesos do
modelo.

Definicao sugerida:

```text
Treinar Hermes, neste harness, significa refinar operacionalmente prompts,
skills, logging, validadores, criterios de auditoria e protocolos de interacao
para que o comportamento observavel de Hermes melhore em runs futuras.
```

Motivo:

- Evita ambiguidade tecnica.
- Mantem o trabalho dentro do escopo do repositorio.
- Define aprendizado como comportamento observavel, nao como estado interno
  presumido do modelo.

## 7. Medidas De Aprendizado Observavel

Falta explicitar como saber que Hermes melhorou.

Medidas sugeridas:

- Usa apenas papeis oficiais em metadata e outputs.
- Captura input/output por perfil durante a execucao.
- Nao inventa referencias, DOIs, autores, datasets ou metricas.
- Marca evidencia, inferencia, assumption e open question.
- Aceita critica e revisa uma resposta sem esconder fraquezas.
- Produz skills com trigger claro, nao-goals e workflow executavel.
- Passa em `scripts/validate_hermes_run.py`.
- Registra falhas reais em `reports/hermes_diagnostics.md`.

Motivo:

- "Hermes aprendeu" precisa significar algo verificavel.
- Essas medidas se conectam ao contrato do repo e ao validador.
- A campanha fica auditavel por evidencias, nao por impressao subjetiva.

## 8. Protocolo De Conversa Codex-Hermes

O arquivo atual tem bons prompts, mas falta um protocolo de turnos para uma
campanha longa.

Sugestao:

1. Codex cria run com `scripts/init_hermes_run.py`.
2. Codex escreve o prompt do papel em `profiles/<role>/input/prompt.md`.
3. Hermes executa somente aquele papel.
4. Codex salva a resposta bruta em `profiles/<role>/output/response.md`.
5. Codex audita a resposta usando `docs/hermes_audit_checklist.md`.
6. Codex salva revisao em `profiles/<role>/output/codex_review.md`.
7. Codex roda `scripts/validate_hermes_run.py`.
8. Somente artefatos aprovados sao promovidos para `reports/`, `memory/`,
   `skills/`, `prompts/` ou `schemas/`.

Motivo:

- Evita prompts longos demais e respostas misturadas.
- Preserva a anti-retrospective-copy rule.
- Torna cada papel auditavel em isolamento.

## 9. Politica De Edicao Durante O Goal

Falta declarar quando Codex deve editar arquivos durante o Goal.

Sugestao:

- Codex pode criar run folders, inputs, outputs e diagnosticos de execucao.
- Codex pode editar validadores, checklist ou docs quando o usuario pedir.
- Codex nao deve transformar sugestao do Hermes em arquivo curado sem aprovacao
  explicita ou sem passar pela revisao definida.
- Memoria em `memory/` so deve mudar quando houver conhecimento duravel.

Motivo:

- Protege o repo de artefatos gerados prematuramente.
- Mantem a diferenca entre output bruto e conclusao curada.
- Evita que Codex finja que uma proposta propria foi uma saida Hermes.

## 10. Relacao Com Diagnosticos

O arquivo atual mostra o formato de diagnostico, mas pode ligar isso ao Goal.

Sugestao:

- Toda falha real do Hermes deve ser registrada em
  `reports/hermes_diagnostics.md`.
- Falha de shell, quoting, path ou operacao de Codex deve ser marcada como
  falha de operador, nao de Hermes.
- Bloqueios de provider/auth devem ser registrados como bloqueios de ambiente,
  sem copiar segredos.

Motivo:

- Diagnosticos viram evidencia para melhorar o harness.
- Separar falha de Hermes de falha de operador evita conclusoes falsas.
- Provider/auth e um risco operacional recorrente e deve ser tratado fora do
  repo.

## Conclusao

`HERMES_CODEX_KNOWLEDGE.md` ja pode orientar um primeiro Goal controlado. Para
uma campanha longa, ele deve ser complementado com:

- objetivo verificavel;
- criterios de entrada;
- criterios de parada;
- integracao explicita com scripts e checklist;
- harmonizacao do caminho Hermes;
- definicao operacional de "treinar Hermes";
- metricas de aprendizado observavel;
- protocolo de turnos Codex-Hermes;
- politica de edicao e promocao;
- tratamento claro de diagnosticos.

Esses pontos transformam a base de conhecimento em um contrato operacional para
refinar Hermes sem perder rastreabilidade, disciplina de evidencia ou controle
do repositorio.
