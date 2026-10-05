# Evidência de validação — Curitiba/2019

- Data da validação: 15/08/2026.
- Município: Curitiba.
- ID do município no portal: 1490.
- Entidade: Município de Curitiba.
- ID da entidade: 12268.
- Exercício: 2019.

## Relatórios utilizados

1. RREO — Demonstrativo da Receita Corrente Líquida, identificador 10.
2. RGF — Demonstrativo da Despesa com Pessoal, identificador 20.

## Resultado da execução real

| Campo | Valor extraído |
|---|---:|
| Receita Corrente Líquida | R$ 7.361.430.652,73 |
| Receita Corrente Líquida Ajustada | R$ 7.359.872.310,73 |
| Despesa Total com Pessoal | R$ 2.786.074.714,14 |
| Percentual oficial do relatório | 37,85% |
| Percentual recalculado pelo protótipo | 37,8549% |
| Limite de alerta | 48,6% |
| Limite prudencial | 51,3% |
| Limite máximo | 54% |
| Diferença de RCL entre RREO e RGF | R$ 0,00 |

## Erro encontrado durante o teste

O CSV do RGF repete o rótulo “Despesa Total com Pessoal” em uma tabela mensal e no resumo anual. A primeira implementação selecionou a ocorrência mensal.

A extração foi corrigida para aceitar como resumo somente a linha cujo rótulo começa na primeira coluna. Um teste automatizado foi adicionado para impedir regressão.

## Resultado

- Coleta: aprovada no cenário testado.
- Extração: aprovada após correção.
- Validação da RCL: aprovada, diferença zero.
- Cálculo de conferência: compatível com o percentual oficial após arredondamento.
- Exportação Excel: aprovada por teste automatizado de abertura do arquivo.

