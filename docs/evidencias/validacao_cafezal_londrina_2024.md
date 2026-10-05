# Validação financeira — Cafezal do Sul e Londrina/2024

- Coleta: 25/08/2026
- Fonte: portal oficial TCE-PR/SIM-AM
- Relatórios: RREO/RCL (10), RGF/Pessoal (20) e RREO/MDE-FUNDEB (15)
- Período do MDE: 6º bimestre

## Resultados conferidos

| Campo | Cafezal do Sul | Londrina |
|---|---:|---:|
| ID município / entidade | 868 / 12223 | 2761 / 12367 |
| RCL no RREO | R$ 35.517.215,86 | R$ 3.058.397.847,70 |
| RCL no RGF | R$ 35.517.215,86 | R$ 3.058.397.847,70 |
| Diferença entre relatórios | R$ 0,00 | R$ 0,00 |
| RCL ajustada para pessoal | R$ 32.900.699,50 | R$ 3.012.781.541,28 |
| Despesa Total com Pessoal | R$ 14.464.640,57 | R$ 1.341.895.717,35 |
| Percentual oficial | 43,96% | 44,54% |
| Percentual recalculado | 43,9645% | 44,5401% |
| Diferença por arredondamento | 0,0045 p.p. | 0,0001 p.p. |
| Receitas recebidas do FUNDEB | R$ 3.586.720,18 | R$ 334.487.956,04 |
| Resultado líquido FUNDEB | -R$ 1.794.286,45 | R$ 200.307.310,81 |

## Conferência manual do bruto

Nos CSVs preservados em `data/raw/tce/`, as linhas de resumo do relatório 20 publicam exatamente os valores de RCL ajustada, DTP e percentual oficial exibidos acima. O relatório 10 publica a mesma RCL, produzindo diferença de R$ 0,00. O relatório 15 publica os valores de FUNDEB extraídos pelo sistema.

## Conclusão

As duas execuções terminaram sem falhas e confirmam que a extração por rótulo usada na amostra de Curitiba também funcionou em um município pequeno e em um município de grande porte. Isso amplia a evidência, mas não elimina a necessidade de amostragem periódica caso o TCE altere seus relatórios.

Arquivos tratados:

- `docs/evidencias/TCE_Cafezal_do_Sul_2024.json`
- `docs/evidencias/TCE_Londrina_2024.json`
