# GitHub, CI e trabalho em equipe

Equipe de 7: 3 back-end, 3 front-end, 1 QA (DEC-006), com revisão cruzada. O QA não é o único responsável pela qualidade.

## Conteúdo
- Fluxo de branches e commits
- Revisão cruzada por área
- Definição de pronto
- GitHub Actions (CI)
- Dependabot, template de PR, CODEOWNERS
- Releases

## Fluxo de branches e commits (de `CONTRIBUTING.md`)

1. Atualize a `main`; crie branch curta para **uma** tarefa; commits pequenos; abra PR (rascunho se preciso); peça ao menos uma revisão; atualize a documentação quando o comportamento mudar.
2. Branches: `feat/coleta-tce-2019`, `feat/interface-filtros`, `fix/conversao-moeda`, `test/validacao-curitiba-2019`, `docs/requisitos-modulo-1`.
3. Commits: `feat:`, `fix:`, `test:`, `docs:`, `refactor:` + descrição no imperativo.

## Revisão cruzada

- Coleta/extração: revisada por **outro** integrante do back-end.
- Fórmulas e valores: exigem **evidência da fonte** na descrição do PR.
- Interface: revisada por outro integrante do front-end.
- QA recebe entregas pequenas em dias úteis (DEC-007); PRs de fim de semana ficam como rascunho.

## Definição de pronto

Atende aos critérios de aceitação; foi **executada ou testada**; não contém dados inventados; recebeu revisão; tem documentação suficiente para outra pessoa entender.

## GitHub Actions (CI)

Modelos prontos em `assets/github/` (copiar para `.github/` do repositório):

- `workflows/ci.yml`: roda a suíte `unittest` em Ubuntu e Windows (o usuário final está no Windows), Python 3.11 e 3.12, com cache de pip. Não acessa a internet para testes do TCE (os testes usam dublês).
- Teste da interface em jsdom pode virar um segundo job (instalar Node + `jsdom`), opcional.
- Torne o job **obrigatório** na proteção da branch `main` (Settings > Branches): exigir PR, 1 aprovação e CI verde.

## Dependabot, template de PR, CODEOWNERS

- `assets/github/dependabot.yml`: atualiza `pip` e `github-actions` semanalmente.
- `assets/github/pull_request_template.md`: checklist com evidência da fonte, testes, docs e segurança.
- `CODEOWNERS` (criar em `.github/`): atribuir por pasta, por exemplo `src/coleta/ @back-1`, `static/ @front-1`, `tests/ @qa`, `docs/ @todos`. Preencha com os usuários reais.

## Releases

Versione com tags (`v0.8.0`), mantenha `CHANGELOG.md` (formato já usado: versão, data, itens). O ZIP distribuído **não** inclui `data/raw/*`. Antes de release: suíte verde, `docs/` atualizados, evidências em `docs/evidencias/`, e a lista do que **não** foi verificado (ex.: `.bat` em Windows real).

## Skills de agente úteis neste fluxo

Combine esta skill com skills de revisão de código e segurança (`owasp-security`, revisores de PR) e de teste (`pytest`/`unittest`), mas as regras do projeto aqui prevalecem sobre qualquer padrão genérico.
