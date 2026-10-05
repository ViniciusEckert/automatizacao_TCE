# Módulo financeiro — TCE-PR, LRF e FUNDEB

## Conteúdo
- Fonte e coleta
- Relatórios adotados
- Indicadores e fórmulas
- Limites e classificação
- FUNDEB / MDE
- Histórico e falhas parciais
- Campos de saída

## Fonte e coleta

Portal SIM-AM/TCE-PR (`Rel_LRF.aspx?relTipo=1`), ASP.NET Web Forms. O `TCEClient` reproduz postbacks, mantém cookies e baixa o **CSV oficial** (DEC-009: preferir CSV à automação de cliques). Campos do formulário: `ddlMunicipio`, `ddlEntidade`, `ddlRelatorio`, `ddlAno`, `ddlPeriodo` (prefixo `ctl00$ContentPlaceHolder1$`).

Regras de coleta:
- **Sequencial** (DEC-010). Paralelismo derruba o portal com erro 500.
- Verificar o catálogo antes de solicitar relatório (entidade pode não oferecer o relatório). Ausência confirmada → HTTP 422 com orientação; falha de conexão é um erro distinto.
- Entidade: priorizar Município/Prefeitura que ofereça RCL e Pessoal.
- Preservar os CSVs em `data/raw/tce/<municipio>/<entidade>/<ano>/`. Nunca editar.
- Se um rótulo sumir: preserve o bruto, compare a estrutura, adicione a variação explícita ao extrator **e crie o teste antes** de alterar a regra. Use `python -m scripts.mapear_tce`.

## Relatórios adotados

| ID | Relatório | Período | Campos |
|---:|---|---|---|
| 10 | RREO — Receita Corrente Líquida | anual | RCL e controle |
| 20 | RGF — Despesa com Pessoal | anual | RCL ajustada, DTP, percentual, limites |
| 15 | RREO — MDE | 6º bimestre (ID 32) | receitas do FUNDEB, resultado líquido |

## Indicadores e fórmulas

```text
comprometimento (%) = Despesa Total com Pessoal / RCL Ajustada x 100
variação (%)        = (atual / anterior - 1) x 100        # None se base zero ou ausente
diferença (p.p.)    = percentual atual - percentual anterior
evolução acumulada  = (último ano válido / primeiro ano válido - 1) x 100
diferença_validacao_rcl = RCL do relatório 20 - RCL do relatório 10   # controle de qualidade
```

- Denominador é a **RCL ajustada**, não a RCL simples.
- RCL ajustada <= 0 → erro explícito (`ValueError`), nunca divisão silenciosa.
- Base zero na variação devolve `None`; não mascarar com 0 nem infinito.
- Sempre exibir `percentual_oficial` (publicado) ao lado de `percentual_calculado`; divergência é sinal para investigar o bruto, não para "corrigir".

## Limites e classificação

Os limites são **lidos do relatório**, não fixados no código. Referência LRF para o Poder Executivo municipal: máximo de 54% da RCL (conferir sempre o valor publicado). Derivados:

| Faixa | Classe |
|---|---|
| abaixo de 90% do máximo | `normal` |
| >= alerta (90%) e < prudencial (95%) | `alerta` |
| >= prudencial (95%) e < máximo | `prudencial` |
| >= máximo | `limite_excedido` |

Na amostra: alerta 48,6%, prudencial 51,3%, máximo 54,0%.

## FUNDEB / MDE

- Extrair por rótulo normalizado `RECEITAS RECEBIDAS DO FUNDEB` (era `11-` em 2019–2020 e `6 -` em 2021–2025).
- Falha do FUNDEB num ano = **aviso**; RCL e Pessoal válidos são mantidos (DEC-014).
- `fundeb.percentual_aplicacao_mde` é opcional (rótulo pode não existir).
- **Não automatizar a narrativa MDE / margem fiscal** (DEC-022, R17): rótulos e denominadores do PDF-modelo são ambíguos. Mostre os números; não conclua.

## Histórico e falhas parciais

- Máximo de 10 exercícios, a partir de 2019 (DEC-016).
- Anos fora do catálogo viram ausência de dados registrada; não consultar relatório inexistente nem preencher número.
- Cada ano falho entra em `erros[]` com o motivo; se todos falham por causas diferentes, preservar os motivos individuais.
- Catálogo indisponível **bloqueia** a consulta ao vivo (DEC-028); nunca cair em Curitiba como fallback.
- Curitiba 2019–2025 é demonstração offline identificada, não limite funcional.

## Campos de saída principais

`municipio_id/municipio`, `entidade_id/entidade`, `ano`, `periodo`, `relatorio_id`, `coletado_em`, `valor_bruto`, `valor_tratado`, `receita_corrente_liquida`, `receita_corrente_liquida_ajustada`, `despesa_total_pessoal`, `percentual_oficial`, `percentual_calculado`, `limites.{alerta,prudencial,maximo}`, `fundeb.{receitas_recebidas,resultado_liquido_transferencias,percentual_aplicacao_mde}`, `evolucao.*_percentual`, `resumo.evolucao_acumulada_*`, `erros[]`, `avisos[]`.

## Valores de referência para regressão (Curitiba, validados no bruto)

| Ano | Comprometimento |
|---:|---:|
| 2019 | 37,85% |
| 2020 | 36,81% |
| 2021 | 38,47% |
| 2022 | 35,80% |
| 2023 | 42,77% |
| 2024 | 41,43% |
| 2025 | 38,64% |

Também validados no bruto: Cafezal do Sul/2024 e Londrina/2024.

## Atenção a tipos numéricos

Na extração financeira (`tce_client`, `relatorios`) não há uso de `Decimal` no código atual; o salarial usa. Ao mexer em conversão monetária (formato brasileiro `1.234.567,89`), teste vírgula/ponto, milhar, negativos e vazio, e considere padronizar com `Decimal`.
