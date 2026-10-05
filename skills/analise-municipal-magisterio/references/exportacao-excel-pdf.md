# Exportação — Excel e PDF

## Conteúdo
- Princípios
- Excel financeiro
- Excel salarial (modelo do professor)
- Verificação
- PDF salarial
- Checklist

## Princípios

1. **Excel é a saída operacional principal; PDF é complementar; CSV é evidência.**
2. **Fórmulas vivas**, não resultados colados: o analista precisa poder alterar parâmetros (jornada, PSPN, modo de centavos) e ver recalcular. Mantenha também valores em cache para quem abre sem recalcular.
3. **Premissas e avisos em todas as saídas** (aba/bloco de parâmetros e avisos): jornada, modo de centavos, PSPN usado, origem da progressão, anos sem dados, falhas parciais.
4. **Nenhum link externo** na planilha (DEC-021): o arquivo-modelo do professor referenciava uma pasta que não foi enviada; links quebrados foram removidos.
5. O servidor **recalcula a entrada** na exportação salarial; não confia em números vindos do navegador.

## Excel financeiro (`src/exportacao/excel.py`)

- `gerar_excel(dados)` despacha para `gerar_excel_anual` ou `gerar_excel_historico` conforme o dado.
- Aba **Painel financeiro** com fórmulas locais, limites, cores por status (`CORES_STATUS`) e dois gráficos (`_criar_painel_financeiro`).
- Formatos: `MOEDA = 'R$ #,##0.00'`, `PERCENTUAL = '0.00%'` (lembre: percentual no Excel é fração; se o dado for `37.85`, divida por 100 ou use formato literal).
- Paleta: `VERDE_ESCURO 124B3A`, `VERDE 1E6B53`, `VERDE_CLARO EAF4EC`, `CINZA DCD8CC`. Configuração de impressão (`_configurar_impressao`, paisagem, ajuste à largura).
- Anos com erro aparecem como avisos; **não** preencher célula com valor presumido.

## Excel salarial (`modelo_salarial.py` + `excel_modelo_salarial.py` + `excel_salarial.py`)

Reconstrói o modelo das páginas 9–11 do material do professor:
- tabela **atual em verde**, tabela de **referência em roxo**, **não conformidades** em vermelho/rosa, **diferenças monetárias** e **defasagem**;
- células de entrada em azul (`#0000FF`) sobre fundo amarelo claro (`#FFF2CC`) na aba de parâmetros; dados originais em azul;
- formatação condicional marca valor atual < referência;
- todas as classes preservadas, inclusive carreiras longas em **blocos de continuação** (Curitiba tem 184 vencimentos);
- abas auxiliares: parâmetros, dados originais, fontes.
- `normalizar_analise(dados)` padroniza a entrada antes de gerar.

Convenções do projeto para modelos financeiros/tabelas: entradas e premissas em células próprias e referenciadas (`=B5*(1+$B$6)`, nunca `=B5*1.05`); fórmulas consistentes ao longo das classes.

## Verificação (obrigatória ao mexer em exportação)

1. Gere o arquivo pelos testes (`tests/test_excel.py`, `tests/test_salarios.py` abrem o XLSX com `openpyxl`).
2. **Recalcule com LibreOffice** e compare com o valor do Python; o QA v0.5 fez isso e os valores bateram. Em ambiente com a skill `xlsx`, use `scripts/recalc.py` e exija zero erros de fórmula.
3. Evite funções que o LibreOffice não calcula (`XLOOKUP`, `XMATCH`, `SORT`, `FILTER`, `UNIQUE`, `SEQUENCE`); use `INDEX/MATCH`. Funções pós-2007 como `TEXTJOIN`, `IFS`, `MAXIFS` exigem prefixo `_xlfn.` ao escrever com openpyxl.
4. openpyxl **não grava valores calculados**; sem recalcular, leitores que usam `data_only=True` veem `None`. Nunca salve um workbook aberto com `data_only=True` por cima do original (perde as fórmulas).
5. Valide visualmente a ordem, as cores e a impressão num programa de planilhas.

## PDF salarial (`relatorio_pdf.py`, reportlab)

- Fontes **DejaVu Sans** embarcadas em `assets/fonts/` (licença em `DEJAVU_LICENSE.txt`) para acentos e símbolos; `_registrar_fontes()` registra normal e negrito. Não troque por fonte padrão do PDF (perde acentuação).
- Cores: `AZUL #10102E`, `VERDE #4A6123`/`VERDE_CLARO #DCE9BD` (atual), `ROXO #403250`/`ROXO_CLARO #D8CBE5` (referência), `VERMELHO_CLARO #F4CCCC` (não conformidade), `VERDE_OK #D9EAD3`.
- Helpers: `_moeda`, `_percentual`, `_rotulo_regra`, `_rotulo_progressoes`, `_tabela_salarios(...)`; rodapé por `_rodape` com paginação.
- O PDF repete as premissas e avisos do Excel; testes leem o PDF com `pypdf` e checam texto.

## Checklist

- [ ] Fórmulas vivas + cache; nenhum valor colado
- [ ] Parâmetros, avisos e fontes visíveis
- [ ] Sem links externos nem macros
- [ ] Recalculado no LibreOffice, zero erros, valores iguais ao Python
- [ ] Todas as classes presentes (carreiras longas)
- [ ] Nome do arquivo sanitizado (`secure_filename`) e com município/ano/profissão
- [ ] Teste automatizado abre o arquivo gerado e confere células-chave
