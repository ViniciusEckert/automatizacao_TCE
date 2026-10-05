# Back-end Flask — padrões do projeto

## Conteúdo
- Estrutura atual
- Contrato de erros JSON
- Como adicionar uma rota
- Injeção de dependência e testes
- Plano de blueprints
- Logging e configuração

## Estrutura atual

`app.py` expõe `create_app(analise_service=None, dossie_diretorio=None)` (application factory) e instancia `app = create_app()` no fim. Serviços ficam em `app.config` (`ANALISE_SERVICE`, `DOSSIE_SALARIAL_STORE`, `AUTOMACAO_SALARIAL`), o que permite trocar por dublês nos testes. Limite de upload: `MAX_CONTENT_LENGTH = 48 MB`. Execução: `debug=False, use_reloader=False` (decisão: o reloader reiniciava por eventos do watchdog).

Grupos de rotas hoje (todas em `app.py`):

| Grupo | Prefixo | Exemplos |
|---|---|---|
| Telas | `/`, `/avancado` | `inicio.html`, `index.html` |
| Automação (caminho simples) | `/api/automacao/` | `financeiro`, `exemplo-financeiro`, `tabelas`, `preparar-tabela`, `salarios` |
| Catálogo TCE | `/api/municipios`, `/api/entidades/<id>`, `/api/anos/<m>/<e>` | listas para os selects |
| Financeiro detalhado | `/api/analisar`, `/api/analisar-historico`, `/api/exportar`, `/api/amostras/curitiba*` | |
| Salarial | `/api/salarios/...` | `inspecionar-pdf`, `extrair-revisao`, `dossies`, `analisar`, `importar-documento`, `exportar-excel`, `relatorio-pdf`, `fontes`, `amostras/*` |
| Materiais | `/api/materiais/inspecionar-planilha` | |

Rota fina: valida entrada, chama o serviço, serializa. **Nenhuma regra de negócio ou cálculo na rota.**

## Contrato de erros JSON (manter)

Toda falha devolve JSON com `erro` (mensagem legível) e, quando aplicável, `tipo`:

| Exceção | HTTP | `tipo` | Observação |
|---|---:|---|---|
| `ValueError` | 400 | `validacao` | entrada inválida; mensagem pode ir ao usuário |
| `TCEConsultaIndisponivel` | 422 | `relatorio_indisponivel` | em `/api/automacao/` usa mensagem amigável + `detalhe` |
| `TCEError` | 502 | `fonte_externa` | idem; inclui `caminho` e `metodo` |
| `RequestEntityTooLarge` | 413 | `validacao` | "excede o limite total de 48 MB" |
| `HTTPException` | original | `http` | **preserva status e cabeçalhos** (404 e 405 não viram 500) |
| `Exception` | 500 | — | `app.logger.exception` com método e caminho; mensagem genérica |

Regras: nunca vazar traceback ao cliente; ausência confirmada de relatório é 422 (não 500); falha de conexão/coleta é distinta de relatório inexistente; mensagem de `/api/automacao/` é em linguagem de usuário, o detalhe técnico vai em `detalhe`.

## Como adicionar uma rota

1. Escreva o serviço em `src/...` (função pura ou classe) com testes unitários.
2. Na rota: `dados = request.get_json(silent=True) or {}`; valide tipos e campos; levante `ValueError` com mensagem clara.
3. Uploads: `request.files.get("arquivo")`; se `None`, `ValueError("Envie ... no campo 'arquivo'.")`. Sanitize nomes com `secure_filename`.
4. Arquivos para download: o projeto devolve JSON com `arquivo: {nome, conteudo_base64}` (o front baixa via Blob). Mantenha esse formato nas rotas `automacao`.
5. Teste com `create_app(...).test_client()` e dublês de serviço; cubra sucesso, entrada inválida e falha da fonte.
6. Documente a rota em `docs/` e no CHANGELOG.

## Injeção de dependência e testes

`AnaliseService(cliente_factory=TCEClient, raw_store=None, salvar_brutos=True)` recebe a fábrica do cliente: nos testes passe uma classe falsa que devolve CSV sintético (veja `ClienteFalso` em `tests/test_service.py`). Para persistência use `TemporaryDirectory`. Nunca acesse a internet em teste.

## Plano de blueprints (refatoração sugerida, sem mudar contrato)

`app.py` concentra ~20 KB de rotas. Quebrar mantendo URLs idênticas:

```text
src/web/
  __init__.py        # create_app, registra blueprints e error handlers
  telas.py           # /, /avancado, /favicon.ico
  automacao.py       # /api/automacao/*
  financeiro.py      # /api/municipios, /api/entidades, /api/anos, /api/analisar*
  salarial.py        # /api/salarios/*
  erros.py           # handlers de erro (contrato acima)
```

Passos: (1) mover handlers de erro; (2) mover um grupo por PR; (3) rodar os 93 testes a cada PR; (4) manter `from app import create_app` funcionando para os testes e `iniciar.py`.

## Logging e configuração

- `app.logger` com método e caminho em toda falha; avisos de fonte externa em `warning`, inesperados com `exception`.
- Configuração por `app.config`; dados do usuário em `%LOCALAPPDATA%/AnaliseMunicipal/tabelas_salariais` (Windows) ou `~/.local/share/AnaliseMunicipal/...`. Não gravar dentro da pasta do ZIP.
- Sem segredos no repositório (`.env*` ignorado, `.env.example` permitido).
