# Parser de documentos salariais (PDF, DOCX, DOC, HTML, planilhas)

Complementa `salarial-regras.md` (o que as regras significam). Aqui: **como extrair e onde estão os riscos**. É a parte mais delicada do sistema: cada prefeitura publica a carreira de um jeito.

## Conteúdo
- Ferramentas atuais
- Pipeline recomendado
- Padrões do `documento_service`
- Detecção de problemas
- Quando considerar pdfplumber/camelot/OCR
- Contratos de erro
- Fixtures

## Ferramentas atuais

| Formato | Como lê hoje | Observação |
|---|---|---|
| PDF com texto | `pypdf` (`_texto_pdf`, `inspecionar_pdf`) | limite 15 MB; prévia de 4000 caracteres |
| PDF sem texto | só diagnóstico (`requer_ocr`) | OCR externo, decisão pendente |
| DOCX | `python-docx` (parágrafos e tabelas) | |
| DOC legado | LibreOffice ou `antiword` (opcional) | `_texto_doc_legado`; `requer_conversao` se ausente |
| HTML | `HTMLParser` (`TabelasHTML`, `_ExtratorHTML`) | tabelas viram matrizes |
| CSV/TSV/XLSX | `extrair_para_revisao`, `inspecionar_planilha` | XLSX inspecionado **sem executar macros** |

## Pipeline recomendado (manter a separação)

```text
arquivo original (hash, preservado)
  -> extrair TEXTO/TABELAS candidatas
  -> ESTRUTURA intermediária (níveis, classes, vencimentos, regras declaradas)
  -> VALIDAÇÃO determinística (progressões coerentes, tolerância R$ 0,01)
  -> REVISÃO HUMANA (grade editável) quando houver dúvida
  -> CÁLCULO e comparação
```

Cada etapa devolve dados **e** avisos. Quem decide vigência/regra aplicável é o analista.

## Padrões do `documento_service`

- `PADRAO_MOEDA`, `PADRAO_NIVEL`, `PADRAO_PERCENTUAL`, `PADRAO_GATILHO_PROGRESSAO` são regex compiladas no topo. Ao ampliar, **adicione o caso de teste antes** e verifique que não quebra os existentes (Cafezal, Curitiba, `test_outros_municipios.py`).
- `CODIGO_NIVEL = r"[A-Z]+|\d+"`; romanos entram como letras maiúsculas.
- `_percentuais_progressao` interpreta frases como `Percentual entre classes = 2%`, `Interstício de 5% entre classes` e listas por transição.
- `_regras_verticais` interpreta `Nível B = Nível A acrescido de 12%` ou `de R$ 300,00`.
- `_inferir_progressoes` deduz da primeira linha e **sempre** adiciona aviso.

## Detecção de problemas (falhar alto)

Verificado na v0.8.0 contra o código: nota com percentual é ignorada; regras verticais conflitantes e progressões gerais conflitantes levantam `ValueError`; linha de nível com valor ilegível falha (por quantidade de classes diferente); **texto de revogação não gera aviso** na v0.8.0 (corrigido no patch v0.8.1 com `_avisos_vigencia`). Com os 5 documentos reais do projeto, a preparação automática devolve 0 candidatos.


- Linha com `Nível` + >= 2 valores não interpretável -> `ValueError` citando a linha.
- Percentual dentro de nota (`(reajuste anual de 5,00%)`) -> ignorar como valor, nunca como classe.
- Regras verticais ou progressões gerais conflitantes -> interromper.
- Quantidade de classes diferente entre níveis -> erro de estrutura.
- Tabela dividida em páginas/blocos -> exigir confirmação do recorte (`recorte_confirmado`).
- PDF multicoluna ou com tabela rotacionada: o texto extraído pode embaralhar a ordem; valide a soma de colunas e a progressão, não confie na ordem.

## Quando considerar pdfplumber / camelot / OCR

Só com amostras reais que o `pypdf` não resolva e depois de registrar a decisão (`docs/09_decisoes.md`):

- **pdfplumber**: boa para tabelas com linhas/colunas e para obter coordenadas; permite recortar região e fixar colunas.
- **camelot** (modos `lattice` para bordas, `stream` para alinhamento por espaços): devolve DataFrames e `accuracy`; exige Ghostscript — avalie o custo de instalação no Windows do analista.
- **OCR (Tesseract)**: último recurso; valores lidos por OCR sempre vão para revisão humana com aviso de baixa confiança.

Se adicionar uma biblioteca: fixe versão no `requirements.txt`, mantenha o fallback atual e cubra com teste usando PDF sintético pequeno (gerado com `reportlab`/`pypdf` nos testes, como em `tests/test_app.py`).

## Contratos de erro

- Falha de leitura/estrutura -> `ValueError` com mensagem acionável (qual linha, qual regra).
- Formato fora do escopo -> 400 com orientação (converter para DOCX/PDF, usar revisão detalhada).
- Nunca devolver carreira "completa" a partir de tabela parcialmente reconhecida.

## Fixtures

Use textos curtos que reproduzem o padrão (como `TEXTO_ANEXO` em `tests/test_salarios.py`) e, para casos reais, a pasta `referencias/fontes_salariais_2026_09_07/` (Cafezal HTML, Curitiba PDF, Londrina PDF, Maringá HTML, Ponta Grossa HTML) — são públicas e já usadas no projeto. Não versionar documentos sigilosos.
