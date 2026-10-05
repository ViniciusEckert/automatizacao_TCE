# Dados e ETL — do bruto ao resultado

## Conteúdo
- Pipeline
- Extração por rótulo
- Números brasileiros
- Modelos de dados
- float x Decimal
- Rastreabilidade
- Checklist para novo extrator

## Pipeline

```text
fonte externa -> BRUTO (imutável) -> EXTRAÇÃO -> TRATADO -> CÁLCULO -> SAÍDA (Excel/PDF/tela)
```

| Etapa | Código | Regra |
|---|---|---|
| Bruto TCE | `src/persistencia/arquivos.py` (`ArquivoBrutoStore`) | `data/raw/tce/<mun>/<ent>/<ano>/relatorio-<id>.csv`, nunca editar |
| Bruto salarial | `src/persistencia/dossie_salarial.py` | `data/raw/salarios/<mun-uf>/<ano>/<dossie>/` + `manifesto.json` + SHA-256 |
| Extração | `src/extracao/relatorios.py`, `src/salarial/documento_service.py` | determinística, por rótulo/regra, sem estado oculto |
| Tratado | `src/modelos/analise.py`, JSON em `data/processed/` | dataclasses `frozen=True` / dicionários validados |
| Cálculo | `src/calculos/indicadores.py`, `src/salarial/analise_service.py` | funções puras, testáveis sem rede |

`data/raw/*` e `data/processed/*` ficam fora do Git (exceto amostras expressamente listadas no `.gitignore`).

## Extração por rótulo

Funções como `_primeira_linha_contendo(linhas, trecho)` e `_resumo_por_inicio` procuram o texto do rótulo (normalizado) e não o índice da linha. Ao tratar um novo campo:

1. Abra o CSV bruto real e identifique o rótulo literal.
2. Normalize (maiúsculas, acentos, espaços) antes de comparar.
3. Aceite variações **explícitas** observadas (ex.: `11- RECEITAS RECEBIDAS DO FUNDEB` e `6 - RECEITAS RECEBIDAS DO FUNDEB`).
4. Se o rótulo não existe: devolva `None`/aviso, não zero.
5. Escreva o teste com um CSV sintético mínimo que reproduza cada variação.

## Números brasileiros

`numero_brasileiro(texto)` converte `1.234.567,89` -> `1234567.89`. Casos que o teste deve cobrir: milhar com ponto, decimal com vírgula, negativo (`-1.234,56` e `(1.234,56)` se existir no portal), percentual `37,85%`, `-`/vazio (ausente, não zero), espaços e `R$`. O mesmo formato vale para tabelas salariais (`documento_service._numero_brasileiro`). Não confundir percentual de nota de rodapé com valor monetário.

## Modelos de dados

`LimitesPessoal`, `DadosFundeb`, `EvolucaoFinanceira`, `AnaliseFinanceira`, `AnaliseHistorica` são dataclasses imutáveis em `src/modelos/analise.py`, com `asdict` para serializar e timestamp em `America/Sao_Paulo` (`ZoneInfo`, por isso `tzdata`). Campos opcionais usam `Optional[...] = None`. Dicionário completo em `docs/11_dicionario_de_dados.md`; ao criar campo novo, atualize o dicionário no mesmo PR.

## float x Decimal

- **Salarial**: `Decimal` com `ROUND_DOWN` (truncar) e `ROUND_HALF_UP` (arredondar) a cada etapa; `float` só na serialização final com 2 casas.
- **Financeiro**: os modelos atuais usam `float`. Aceitável para os percentuais exibidos hoje; ao somar/subtrair valores monetários em bilhões, comparar igualdade ou reproduzir centavos, **converta para `Decimal`** e documente. Nunca compare `float` por `==`; use tolerância (`abs(a-b) < 0.005`) ou `Decimal`.
- Percentual calculado vs. oficial: exiba os dois; diferença > 0,01 p.p. merece investigação no bruto.

## Rastreabilidade

Cada resultado deve permitir responder "de onde veio este número?": `relatorio_id`, `ano`, `periodo`, `coletado_em`, `valor_bruto`, caminho do CSV preservado. Resultados salariais carregam arquivo-fonte, hash, origem da progressão (`declarada|informada|inferida`) e `avisos[]`. Se um número não tem origem, não entra na saída.

## Pandas?

Hoje não é dependência. Só introduza se uma tarefa realmente ganhar (limpeza de tabelas grandes, agregações). Mantenha as funções de cálculo independentes de DataFrame para continuarem testáveis com dados mínimos. Se adicionar, fixe versão no `requirements.txt`.

## Checklist para novo extrator/indicador

- [ ] CSV/documento real preservado como fixture (ou sintético identificado)
- [ ] Rótulo localizado por texto, com variações listadas
- [ ] Ausência tratada (`None` + aviso), não zero
- [ ] Teste de valor conferido manualmente no bruto
- [ ] Campo no dicionário de dados
- [ ] Origem do valor exposta na saída
