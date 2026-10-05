# Execução local e empacotamento (Windows)

O usuário final é um analista num computador **Windows**, sem ambiente de desenvolvimento. O desenvolvimento e o QA automatizado rodam em Linux.

## Conteúdo
- Como o app inicia
- Requisitos
- Armadilhas do Windows
- Opções de empacotamento
- O que não foi verificado

## Como o app inicia

`Iniciar.bat` -> localiza Python 3.11+ (`py -3` ou `python`), cria `.venv`, instala `requirements.txt` (reinstala se o arquivo mudou, comparando com `.venv\requisitos_instalados.txt`) e executa `iniciar.py`. Este usa `make_server("127.0.0.1", 0, create_app(), threaded=True)` — **porta livre escolhida pelo sistema**, para nunca confundir com outra versão ligada na 5000 — e abre o navegador após 0,7 s. Fechar a janela encerra o servidor. `python app.py` continua disponível na porta 5000, sem abrir o navegador. Ambos sem debug e sem reloader.

## Requisitos

Python 3.11+; internet na primeira abertura (instalar dependências) e nas consultas ao TCE-PR. Dependências: Flask, openpyxl, requests, tzdata, pypdf, python-docx, reportlab. LibreOffice é **opcional** (só para `.doc` legado).

## Armadilhas do Windows

- `tzdata` é obrigatório: o Windows não traz a base IANA que `ZoneInfo("America/Sao_Paulo")` usa (DEC-035).
- Arquivo `.bat` precisa de finais de linha CRLF.
- Caminhos: use `pathlib`, nunca concatenar com `/` ou `\`; dados do usuário em `%LOCALAPPDATA%`.
- Codificação: abrir/gravar CSV e JSON com `encoding="utf-8"` explícito; o console do Windows pode não ser UTF-8 (cuidado com `print` de acentos).
- Antivírus/SmartScreen podem bloquear `.bat` baixado; documente o passo de desbloqueio.
- Permissão de escrita: não gravar dentro de `Program Files`.
- Downloads automáticos podem ser bloqueados pelo navegador; o botão "Baixar Excel novamente" deve continuar visível.

## Opções de empacotamento (se a equipe quiser evoluir)

| Opção | Prós | Contras |
|---|---|---|
| Manter ZIP + `Iniciar.bat` (atual) | simples, transparente | exige Python instalado |
| PyInstaller (`--onedir`) | sem Python no PC do analista | antivírus podem acusar falso positivo; incluir `templates/`, `static/`, `assets/` e `data/processed/` como dados |
| Instalador (Inno Setup/MSIX) sobre o PyInstaller | experiência de instalação | mais manutenção |

Ao empacotar: resolver caminhos relativos ao executável congelado, manter dados do usuário em `%LOCALAPPDATA%`, testar em Windows limpo.

## O que não foi verificado

O `.bat` e a aparência em Windows real não foram executados no ambiente de validação (Linux). Qualquer mudança nesta área precisa de teste manual em Windows e registro em `docs/evidencias/`.
