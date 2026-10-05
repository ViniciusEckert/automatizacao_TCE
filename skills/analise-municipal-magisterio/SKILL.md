---
name: analise-municipal-magisterio
description: Skill completa do projeto "Análise Municipal / Jornada Magistério" - sistema local em Python/Flask + JavaScript puro que automatiza a análise financeira (TCE-PR, LRF, RCL ajustada, despesa com pessoal, FUNDEB/MDE) e salarial (tabela de carreira municipal x PSPN, progressões, defasagem) do magistério e gera Excel/PDF. Use SEMPRE que a tarefa tocar este repositório ou seus conceitos, em qualquer área - back-end Flask e rotas, front-end/HTML/CSS/JS e design da interface, coleta SIM-AM/TCE-PR, ETL e extração por rótulo, cálculos, parser de PDF/DOCX/DOC/HTML salarial, dossiê municipal, exportação Excel (openpyxl) e PDF (reportlab), testes unittest/jsdom e QA, segurança de uploads, persistência/banco, GitHub Actions/CI/PR, Iniciar.bat e empacotamento Windows - mesmo que o usuário não cite o nome do projeto. Use também para revisar PRs, corrigir bugs, criar novas funcionalidades ou propor refatorações neste sistema.
---

# Análise Municipal — Jornada Magistério

Sistema local (Python 3.11+, Flask, JS puro, Windows para o usuário final) usado por um analista para responder: **a prefeitura tem condições financeiras de reajustar o magistério, e como a tabela salarial municipal se compara ao piso nacional (PSPN)?** O software **organiza e calcula**; quem interpreta e decide é o analista.

Fonte da verdade: o código e `docs/` do repositório (versão de referência desta skill: **v0.8.0, 93 testes**). Se algo aqui conflitar com o repositório, vale o repositório — e a divergência deve ser reportada.

## Roteador: leia a referência da sua tarefa

Carregue só o que a tarefa precisa. Quando a tarefa cruza áreas (comum), leia todas as envolvidas.

| Se a tarefa é sobre... | Leia |
|---|---|
| Rotas, serviços, erros HTTP, uploads, blueprints | `references/backend-flask.md` |
| Tela, HTML/CSS/JS, textos, acessibilidade, aparência | `references/frontend.md` + `assets/DESIGN.md` |
| TCE-PR, RCL, DTP, limites, FUNDEB, histórico | `references/financeiro-lrf-tce.md` |
| Extração, conversão numérica, modelos de dados, rastreabilidade | `references/dados-etl.md` |
| PSPN, jornada, centavos, progressões, defasagem | `references/salarial-regras.md` |
| Ler PDF/DOCX/DOC/HTML/planilha salarial, bugs do parser | `references/parser-documentos.md` |
| Gerar/alterar Excel ou PDF | `references/exportacao-excel-pdf.md` |
| Upload, caminhos, subprocessos, dados sigilosos | `references/seguranca-uploads.md` |
| Arquivos x banco, SQLite/SQLAlchemy, migração | `references/persistencia-e-banco.md` |
| Escrever/rodar testes, QA, regressão | `references/testes-e-qa.md` + `assets/templates/teste_unittest_modelo.py` |
| Branches, PR, CI, Dependabot, CODEOWNERS, release | `references/github-ci-equipe.md` + `assets/github/` |
| Iniciar.bat, Windows, PyInstaller | `references/execucao-windows.md` |
| "Por que é assim?", "podemos assumir X?" | `references/decisoes-e-pendencias.md` |

Atalhos por tipo de pedido:
- **Novo município/relatório/campo financeiro** -> financeiro + dados-etl + testes-e-qa.
- **Bug no parser salarial** -> parser-documentos + salarial-regras + testes-e-qa (escreva primeiro o teste que reproduz).
- **Nova tela ou ajuste visual** -> frontend + DESIGN.md (+ skill `frontend-design`, se disponível).
- **Nova rota/exportação** -> backend-flask + exportacao-excel-pdf + seguranca-uploads.
- **Nova dependência ou banco** -> decisoes-e-pendencias (DEC-030) + persistencia-e-banco; justifique com sintoma concreto.

## Princípios inegociáveis

Eles existem porque o erro mais caro neste domínio é um número plausível e errado que o analista leva para uma decisão.

1. **Não inventar fórmula, regra ou dado** (DEC-004). Premissa não confirmada vira *parâmetro* visível + aviso, nunca constante escondida.
2. **Falhar de forma clara é melhor que ter sucesso parcial silencioso** (DEC-023). Linha salarial com valores que não pôde ser lida interrompe a importação e cita a linha.
3. **Bruto é intocável.** CSV do TCE e documentos municipais são preservados como recebidos (com SHA-256); correção acontece numa camada tratada posterior.
4. **Extrair por rótulo, nunca por posição de linha** (DEC-012). O layout do TCE já mudou entre 2020 e 2021.
5. **Cada número precisa de origem rastreável**: relatório, ano, período, `coletado_em`, valor bruto -> valor tratado.
6. **Falha isolada por exercício** (DEC-013/014): um ano ou o FUNDEB indisponível não apaga os anos válidos; vira `erros[]`/`avisos[]`.
7. **Nada de conclusão jurídica ou de "tem direito a reajuste"** no software. Jornada, vigência, enquadramento e disponibilidade financeira ficam sob revisão humana.
8. **Cafezal do Sul e Curitiba são amostras/layout, não esquema universal** (DEC-027, DEC-031). Nunca hardcodar nada de um município.
9. **O front não calcula.** Cálculo vive em `src/calculos` e `src/salarial`, nunca em rota nem em JS.
10. **Nenhum dado sigiloso no Git; nenhuma URL baixada automaticamente** (R11, DEC-033).

## Mapa do código

| Área | Onde | Observação |
|---|---|---|
| Entrada HTTP | `app.py` (`create_app`) | ~20 KB; rotas ainda concentradas aqui |
| Coleta TCE | `src/coleta/tce_client.py` | `TCEClient`, postback ASP.NET, CSV oficial, **sequencial** |
| Extração financeira | `src/extracao/relatorios.py` | por rótulo |
| Cálculos financeiros | `src/calculos/indicadores.py` | percentual, classificação, variações |
| Orquestração financeira | `src/services/analise_service.py`, `automacao_financeira.py` | histórico, falha parcial |
| Salarial | `src/salarial/` | `documento_service` (parser), `analise_service` (cálculo, `Decimal`), `revisao_service`, `aquisicao_service` (dossiê), `automacao_service` |
| Modelos | `src/modelos/analise.py` | dataclasses imutáveis |
| Persistência | `src/persistencia/` | arquivos/JSON; sem banco (decisão vigente) |
| Saídas | `src/exportacao/` | Excel (openpyxl) e PDF (reportlab, fontes DejaVu em `assets/fonts/`) |
| Front | `static/js/`, `static/css/`, `templates/` | duas interfaces: `inicio.html` (simples) e `index.html` (`/avancado`) |
| Testes | `tests/` (`unittest`), `scripts/testar_interface.cjs` (jsdom) | `python -m unittest discover -s tests -v` |
| Execução | `Iniciar.bat`, `iniciar.py` | porta livre em 127.0.0.1 |

## Fluxo para qualquer mudança

1. Localize a decisão (DEC-xxx) que governa o comportamento; para mudar uma decisão, proponha PR documentado.
2. Leia a(s) referência(s) do roteador acima.
3. Escreva **primeiro** um teste que reproduza o caso (valor conferido no bruto ou documento real), incluindo o caminho de falha.
4. Altere o mínimo, na camada certa (rota fina -> serviço -> cálculo).
5. Rode a suíte inteira; os testes Python **não acessam a internet** (use dublê do `TCEClient`).
6. Se a mudança afeta um número exibido, registre evidência em `docs/evidencias/`.
7. Atualize docs, dicionário de dados e `CHANGELOG.md` no mesmo PR.
8. Em saídas Excel/PDF, confirme que parâmetros e avisos continuam visíveis e recalcule o Excel no LibreOffice.
9. Diga explicitamente o que **não** foi verificado (ex.: Windows real, navegador real).

## Armadilhas conhecidas (já causaram bugs)

- Percentual em nota de rodapé — por exemplo "(reajuste anual de 5,00%)" — **não é dinheiro nem classe salarial**.
- Duas regras verticais ou duas progressões gerais conflitantes para o mesmo nível: **interromper**, não escolher a "vigente".
- Regras duplicadas/conflitantes: o parser interrompe com `ValueError` (verificado). **Revogações em texto legal NÃO são detectadas** (verificado: "Fica revogado o art. 5º…" passa sem aviso); a vigência é sempre conferência humana. O patch v0.8.1 (`_avisos_vigencia` em `documento_service.py`) adiciona o aviso; se o repositório já o tem, a lacuna está resolvida.
- Paralelizar requisições ao portal SIM-AM causa erro 500 (DEC-010).
- Rótulo do FUNDEB mudou de posição (2019–2020 vs 2021–2025); procurar `RECEITAS RECEBIDAS DO FUNDEB` normalizado.
- `tzdata` é dependência obrigatória por causa do Windows (DEC-035).
- PSPN de 2026 não pode ser estendido a outros anos nem a outras profissões.
- PDF sem texto exige OCR (hoje só diagnosticado; OCR só se amostras reais justificarem).
- Fallback silencioso para Curitiba quando o catálogo falha foi um bug real (DEC-028): falha de catálogo bloqueia a consulta.
- Handler genérico de exceção que convertia 404/405 em 500 foi um bug real: `HTTPException` preserva status.
- Excel salvo com `data_only=True` perde as fórmulas; openpyxl não grava valores calculados (recalcular no LibreOffice).
- Favicon ausente causava 500 no carregamento da página.

- **Documentos municipais reais** (`referencias/fontes_salariais_2026_09_07/`: Curitiba/Londrina PDF, Cafezal/Maringá/Ponta Grossa HTML) **não geram tabela automática** na v0.8.0 (0 candidatos); a tela orienta usar Excel/CSV ou a revisão detalhada. Não prometa extração automática desses formatos.
- Excel feito com openpyxl sem valores em cache aparece em branco em pré-visualizações; o salarial já injeta cache e o financeiro passou a injetar na v0.8.1 (`src/exportacao/cache_xlsx.py`).
- Gráficos openpyxl vêm suavizados por padrão e inventam picos: use `serie.smooth = False`.
- Ano inválido preenchido deve falhar (400); ano ausente ainda é tolerado.

## O que NÃO propor sem evidência nova

Banco de dados, machine learning, React, FastAPI e autenticação não são obrigações do MVP (DEC-030); só entram se o uso exigir. Antes de sugerir qualquer um, cite o sintoma concreto que justifica. Evolução razoável já mapeada: pytest, blueprints, CI, `Decimal` no financeiro, unificação das duas interfaces.

## Combinação com outras skills

Esta skill dá o **o quê e o porquê do projeto**; skills genéricas dão o **como**: `frontend-design` (aparência), `xlsx` e `pdf` (arquivos), revisão de código/segurança, testes. Em conflito, as regras e decisões do projeto prevalecem.
