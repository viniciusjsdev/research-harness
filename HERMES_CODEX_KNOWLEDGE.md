# Hermes + Codex Knowledge Base

Este arquivo e uma base operacional para usar Codex e Hermes Agent juntos neste
research harness. Ele deve servir como referencia para consulta, execucao,
validacao e aprendizado progressivo do metodo.

## Proposito

O projeto e um harness generico de pesquisa. Hermes e o runtime/orquestrador
pretendido; Codex atua como operador, inspetor, implementador auxiliar e
validador tecnico quando solicitado.

Evidence:

- O contrato do repositorio define Hermes Agent como runtime pretendido.
- O repositorio exige rastreabilidade por run em `data/raw/hermes_runs/`.
- Tokens, auth e configuracoes privadas devem ficar fora do repositorio.

Inference:

- Hermes deve conduzir o fluxo de pesquisa baseado em papeis.
- Codex deve ajudar a instalar, configurar, inspecionar, testar e corrigir o
  harness sem inventar saidas do Hermes.

Assumption:

- O ambiente principal de execucao sera WSL2, com o projeto em `/mnt/d/...` e
  Hermes instalado/configurado fora do repo.

Open question:

- Qual provider/modelo sera usado como padrao para os testes longos de pesquisa.

## Goal Mode: Refinamento Operacional Do Hermes

Use esta secao quando o usuario pedir para Codex entrar em Goal treinando,
refinando ou validando Hermes neste research harness.

### Objetivo Do Goal

Refinar Hermes ate que ele execute uma run completa no research harness, usando
papeis oficiais, input/output por perfil, diagnostico de falhas e promocao
controlada de artefatos.

### Criterios De Entrada

Antes de iniciar o Goal, Codex deve confirmar que:

- Hermes e acessivel via WSL dentro da raiz deste repositorio.
- O caminho de execucao usado e exatamente:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes
```

- Esse comando abre Hermes dentro do repositorio compartilhado com Codex.
- O Hermes ja esta configurado para uso via conta no ambiente local, nao por
  API key armazenada no repo.
- `scripts/init_hermes_run.py` consegue criar uma run.
- `scripts/validate_hermes_run.py data/raw/hermes_runs/_template` passa.

Se houver problema de provider, auth, shell ou path, registrar como bloqueio de
ambiente ou falha de operador. Nao copiar tokens, auth stores ou configuracoes
privadas para o repositorio.

### Definicao De Treinamento

Treinar Hermes, neste harness, significa refinar operacionalmente prompts,
skills, logging, validadores, criterios de auditoria e protocolos de interacao
para que o comportamento observavel de Hermes melhore em runs futuras.

Isso nao significa treinar pesos de modelo. Tambem nao deve depender da memoria
persistente da maquina do usuario. Cada interacao com Hermes deve deixar claro,
a partir do que o repositorio entrega:

- o que Hermes e neste projeto;
- como Hermes deve funcionar dentro do harness;
- como usar os papeis oficiais;
- como salvar input/output por perfil;
- como interagir com `data/raw/hermes_runs/`, `reports/`, `memory/`, `skills/`,
  `prompts/` e `schemas/`;
- como separar evidencia, inferencia, assumptions e open questions;
- como diagnosticar falhas sem inventar saidas.

### Base Verificavel Obrigatoria

Durante o Goal, Codex deve usar e citar estes arquivos quando relevantes:

- `scripts/init_hermes_run.py`
- `scripts/validate_hermes_run.py`
- `docs/hermes_audit_checklist.md`
- `data/raw/hermes_runs/_template/00_metadata.json`
- `AGENTS.md`
- `docs/nomenclature.md`
- `docs/role_contracts.md`
- `docs/hermes_run_logging.md`

### Criterio De Parada

Parar quando uma run completa passa no validador sem erros, passando
corretamente por cada perfil, usando schemas quando aplicavel, e preservando os
aprendizados duraveis na memoria do repositorio.

Tambem parar quando:

- a proxima melhoria exigir decisao explicita do usuario;
- houver bloqueio de provider/auth que impeca progresso;
- Hermes repetir a mesma falha apos revisoes de prompt ou fluxo;
- as melhorias restantes forem cosmeticas e nao afetarem rastreabilidade,
  evidencia ou execucao.

### Medidas De Aprendizado Observavel

Hermes so deve ser considerado melhorado quando o comportamento observavel
melhorar. Medidas:

- Usa apenas papeis oficiais em metadata e outputs.
- Captura input/output por perfil durante a execucao.
- Nao inventa referencias, DOIs, autores, datasets ou metricas.
- Marca `Evidence`, `Inference`, `Assumption` e `Open question`.
- Aceita critica e revisa uma resposta sem esconder fraquezas.
- Produz skills com trigger claro, non-goals e workflow executavel.
- Passa em `scripts/validate_hermes_run.py`.
- Registra falhas reais em `reports/hermes_diagnostics.md`.

### Protocolo De Turnos Codex-Hermes

1. Codex cria run com `scripts/init_hermes_run.py`.
2. Codex escreve o prompt do papel em
   `profiles/<role>/input/prompt.md`.
3. Hermes executa somente aquele papel.
4. Codex salva a resposta bruta em
   `profiles/<role>/output/response.md`.
5. Codex audita a resposta usando `docs/hermes_audit_checklist.md`.
6. Codex salva revisao em `profiles/<role>/output/codex_review.md`.
7. Codex roda `scripts/validate_hermes_run.py`.
8. Somente artefatos aprovados sao promovidos para `reports/`, `memory/`,
   `skills/`, `prompts/` ou `schemas/`.

### Politica De Edicao Durante O Goal

- Codex pode criar run folders, inputs, outputs e diagnosticos de execucao.
- Codex pode editar validadores, checklist ou docs quando o usuario pedir.
- Codex nao deve transformar sugestao do Hermes em arquivo curado sem aprovacao
  explicita ou sem passar pela revisao definida.
- Memoria em `memory/` so deve mudar quando houver conhecimento duravel.

### Politica De Diagnostico

- Toda falha real do Hermes deve ser registrada em
  `reports/hermes_diagnostics.md`.
- Falha de shell, quoting, path ou operacao de Codex deve ser marcada como
  falha de operador, nao de Hermes.
- Bloqueios de provider/auth devem ser registrados como bloqueios de ambiente,
  sem copiar segredos.

## Layout Local Recomendado

O acesso operacional confirmado para Hermes e via WSL, dentro da raiz do
repositorio:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes
```

Esse caminho abre Hermes no repositorio que Codex tambem esta operando. A
configuracao do provider ja existe no ambiente local via conta; nao registrar
API keys, tokens ou auth files no repositorio.

Para verificacoes sem conversa longa:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes --version
hermes config path
hermes config env-path
hermes status
```

Regra importante:

- Use o `HERMES_HOME` confirmado pelo ambiente local.
- O `cd` para a raiz do repo define o projeto em que Hermes vai operar.
- O repo nunca deve receber tokens, credenciais, auth stores ou arquivos privados.

## Comandos Basicos

Abrir Hermes dentro do projeto:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes
```

Abrir a tela interativa de providers/modelos:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes model
```

Autenticar Codex como provider do Hermes:

```bash
hermes auth add openai-codex
```

Se o browser/OAuth nao funcionar bem no WSL:

```bash
hermes auth add openai-codex --manual-paste
```

Verificar auth:

```bash
hermes auth list openai-codex
hermes auth status openai-codex
```

Ver configuracao:

```bash
hermes config show
hermes config path
hermes config env-path
```

Abrir configuracao:

```bash
EDITOR=nano hermes config edit
```

Executar diagnostico:

```bash
hermes doctor
```

## Responsabilidades

### Hermes

Hermes deve:

- Ler `AGENTS.md` e seguir o contrato do harness.
- Executar o loop oficial de pesquisa.
- Produzir saidas por papel/perfil no run ativo.
- Manter rastreabilidade de entradas, saidas e artefatos.
- Separar evidencia de inferencia.
- Evitar overclaiming e referencias inventadas.

### Codex

Codex deve:

- Operar Hermes quando o usuario pedir.
- Gerar comandos, diagnosticar ambiente e revisar resultados.
- Nao inventar saidas do Hermes.
- Nao criar artefatos "em nome do Hermes" sem instrucao explicita.
- Implementar arquivos somente quando o usuario pedir diretamente.
- Verificar se Hermes respeitou `AGENTS.md`, schemas, papeis e logging.

### Usuario

O usuario define:

- O objetivo de pesquisa temporario.
- O nivel de rigor esperado para a rodada.
- Se Codex deve apenas operar Hermes ou tambem criar arquivos.
- Quando uma saida bruta deve virar relatorio curado.

## Fluxo Padrao De Execucao

1. Definir objetivo de pesquisa em uma frase.
2. Criar um run em `data/raw/hermes_runs/run-YYYYMMDD-HHMMSS/`.
3. Acionar os papeis oficiais na ordem apropriada.
4. Registrar input/output por papel em:

```text
data/raw/hermes_runs/<run-id>/profiles/<role>/{input,output,artifacts}/
```

5. Consolidar achados sem apagar contradicoes.
6. Rodar Evidence Auditor antes de promover conclusoes.
7. Criar experimento minimo com Experiment Designer.
8. Atualizar `memory/` apenas com conhecimento duravel.
9. Colocar artefatos finais curados em `reports/`.

## Loop Oficial

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

## Estrutura De Validacao

Cada rodada deve ser validada em quatro camadas.

### 1. Validacao De Processo

Checklist:

- Existe run-id unico.
- Cada papel ativado tem input proprio.
- Cada papel ativado tem output proprio.
- Nao ha copia retrospectiva unica usada para simular logs por papel.
- O run usa os papeis oficiais de `docs/nomenclature.md`.

### 2. Validacao De Evidencia

Checklist:

- Cada paper usado tem titulo, autores, ano e URL/DOI quando disponivel.
- Claims sem fonte estao marcados como `Assumption` ou `Open question`.
- Falhas de busca relevantes foram documentadas.
- Resultados ausentes nao foram tratados como prova forte de novidade.

### 3. Validacao De Metodo

Checklist:

- A hipotese e falsificavel.
- Existe baseline.
- Existem metricas claras.
- Confounders principais foram listados.
- O experimento minimo e pequeno o suficiente para ser executavel.

### 4. Validacao De Output

Checklist:

- O relatorio final separa Evidence, Inference, Assumption e Open question.
- O texto nao inventa referencias.
- As conclusoes sao proporcionais a evidencia.
- O proximo passo e operacional, nao apenas opinativo.

## Padrao De Prompt Para Hermes

Use prompts curtos e visiveis.

Template:

```text
Voce esta no research-harness. Siga AGENTS.md.

Objetivo temporario:
<objetivo>

Atue como <Role oficial>.
Produza somente a saida deste papel.
Separe Evidence, Inference, Assumption e Open question.
Registre qualquer incerteza explicitamente.
```

Para tarefas de critica:

```text
Atue como Devil's Advocate.
Ataque a hipotese tecnicamente.
Procure falta de novidade, metricas fracas, baselines ausentes, confounders e
criterios de falsificacao.
Nao proponha defesa ainda.
```

Para defesa:

```text
Atue como Angel Advocate.
Construa a melhor defesa tecnicamente honesta.
Reconheca fraquezas e proponha experimentos que reduzam incerteza.
Nao exagere a evidencia.
```

Para arbitragem:

```text
Atue como Argument Arbiter.
Compare as objecoes e defesas.
Mapeie objecao -> defesa.
Use apenas uma decisao: pass, revise_search, revise_defense,
revise_hypothesis ou pause.
```

## Padrao De Diagnostico

Quando Hermes falhar, registrar em `reports/hermes_diagnostics.md`:

```markdown
## <Data> - <Falha curta>

Evidence:

- Prompt enviado.
- Resposta recebida.
- Comando usado.

Inference:

- Por que isso e uma falha ou risco.

Assumption:

- Causa provavel, se incerta.

Open question:

- O que reduziria a incerteza.

Remediation:

- Ajuste de prompt, fluxo ou repositorio.
```

Nao classificar erro de quoting, shell ou operacao do Codex como falha do
Hermes.

## Aprendizados Operacionais

### Aprendizado 1: Projeto e runtime sao coisas diferentes

Evidence:

- Hermes roda no projeto quando iniciado a partir da raiz do repo.
- Config/auth ficam em `HERMES_HOME`.

Inference:

- Para "usar Hermes dentro do projeto", entre no diretorio do projeto e rode
  `hermes`; nao mova config/auth para o repo.

### Aprendizado 2: Provider/modelo deve ser configurado pelo Hermes

Evidence:

- `hermes model` abre a tela interativa de providers/modelos.
- `hermes auth add openai-codex` adiciona credencial Codex.

Inference:

- Evitar edicao manual de token em YAML. Usar auth manager do Hermes.

### Aprendizado 3: Runs precisam de logging real por papel

Evidence:

- O contrato do repo proibe copiar um log consolidado depois para satisfazer
  role/profile logging.

Inference:

- Cada papel precisa receber input e produzir output durante a execucao real do
  run.

### Aprendizado 4: Codex nao substitui Hermes

Evidence:

- O harness e centrado no metodo e runtime Hermes.

Inference:

- Codex pode operar, revisar, corrigir e implementar quando pedido, mas nao deve
  fingir que uma resposta Codex foi saida Hermes.

## Ideias Soltas Para Testes Futuros

Estas ideias sao objetos temporarios de analise. Elas nao definem a identidade
do projeto.

### Ideia 1: Ferramenta de triagem de papers duplicados

Hipotese:

- Um agente pode detectar papers semanticamente duplicados ou quase duplicados
  em uma revisao bibliografica melhor que regras por titulo.

Teste minimo:

- Usar 30 a 50 papers de uma busca OpenAlex/Semantic Scholar.
- Criar pares positivos e negativos.
- Comparar embeddings, heuristicas de metadados e julgamento do agente.

Metricas:

- Precision, recall, F1, falsos agrupamentos criticos.

### Ideia 2: Auditor automatico de claims em relatorios cientificos

Hipotese:

- Um fluxo Evidence Auditor consegue reduzir claims sem fonte em relatorios
  gerados por agentes.

Teste minimo:

- Gerar dois relatorios sobre o mesmo tema: um sem auditoria e outro com
  Evidence Auditor.
- Contar claims verificaveis, claims sem fonte e claims contraditos.

Metricas:

- Taxa de claims suportados, taxa de claims incertos marcados corretamente,
  taxa de referencias invalidas.

### Ideia 3: Devil's Advocate como redutor de overclaiming

Hipotese:

- Uma etapa Devil's Advocate antes da defesa reduz conclusoes exageradas sem
  reduzir utilidade do plano experimental.

Teste minimo:

- Rodar o mesmo objetivo com e sem Devil's Advocate.
- Comparar conclusoes, riscos identificados e qualidade do experimento minimo.

Metricas:

- Numero de riscos reais encontrados, severidade media, cobertura de baselines,
  avaliacao humana cega.

### Ideia 4: Comparacao de providers para revisao metodologica

Hipotese:

- Diferentes providers/modelos variam significativamente na capacidade de
  identificar falhas metodologicas.

Teste minimo:

- Criar 10 propostas curtas com falhas conhecidas.
- Rodar Methodology Reviewer com providers diferentes.
- Comparar falhas recuperadas.

Metricas:

- Recall de falhas conhecidas, falsas criticas, custo, latencia.

### Ideia 5: Harness para MVE de pesquisa

Hipotese:

- Um pipeline Research Lead -> Experiment Designer gera experimentos minimos
  mais executaveis do que prompts livres.

Teste minimo:

- Usar 10 ideias iniciais vagas.
- Comparar plano livre versus plano com roles oficiais.

Metricas:

- Clareza da hipotese, custo estimado, tempo ate primeiro resultado, existencia
  de baseline e metrica.

### Ideia 6: Search failure como evidencia negativa limitada

Hipotese:

- Registrar falhas de busca melhora a defensibilidade de claims de novidade.

Teste minimo:

- Rodar Literature Scout com e sem `templates/search_failure_note.md`.
- Avaliar se o relatorio final comunica melhor a incerteza.

Metricas:

- Cobertura de fontes buscadas, transparencia de queries, calibracao da
  conclusao de novidade.

## Criterios Para Um Teste Bem-Sucedido

Um teste futuro deve ser considerado bem-sucedido quando:

- Hermes executa dentro da raiz do repo.
- O run tem estrutura valida em `data/raw/hermes_runs/`.
- Os papeis oficiais foram usados corretamente.
- Evidencia e inferencia estao separadas.
- O output final e verificavel.
- Erros, falhas de busca e incertezas sao preservados.
- Nenhum segredo foi escrito no repositorio.

## Comando De Smoke Test

Depois de configurar provider/auth:

```bash
cd /mnt/d/Projetos/Github_ViniciusJ/research-harness
hermes -z "Leia AGENTS.md e responda em 5 bullets quais regras operacionais voce deve seguir neste repo."
```

Saida esperada:

- Hermes reconhece que o repo e um research harness generico.
- Hermes menciona roles oficiais.
- Hermes menciona logging por run/perfil.
- Hermes separa evidencia de inferencia ou reconhece a obrigacao.
- Hermes nao pede para salvar auth ou token no repositorio.

## Proximas Execucoes Planejadas

1. Validar instalacao e provider com `hermes doctor`.
2. Rodar smoke test de leitura de `AGENTS.md`.
3. Criar primeiro run controlado com uma ideia simples.
4. Verificar se Hermes escreve logs por papel no local correto.
5. Registrar falhas em `reports/hermes_diagnostics.md`.
6. Promover apenas conclusoes duraveis para `memory/`.
