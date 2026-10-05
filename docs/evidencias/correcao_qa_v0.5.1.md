# Evidência de correção do QA — MVP 0.5.1

- Data: 25/08/2026
- Entrada: `referencias/qa/QA_Documento_Final_Claude_v0.5.md`
- Resultado automático: 46 testes aprovados

## Confirmação dos três achados

| Achado | Resultado na v0.5 | Correção na v0.5.1 |
|---|---|---|
| Percentual em nota virava classe salarial | Confirmado: `5,00%` era importado como R$ 5,00 | O padrão monetário rejeita números seguidos de `%`; os valores também são procurados somente após o identificador do nível |
| Regra vertical duplicada era sobrescrita | Confirmado: 12% era substituído silenciosamente por 20% | Regras diferentes para o mesmo nível geram erro de conflito e exigem revisão humana |
| Progressões gerais corrigidas/revogadas viravam lista não uniforme | Confirmado: 5% e 8% viravam duas transições | Cada declaração é analisada separadamente; declarações incompatíveis geram erro de conflito |

## Comportamento seguro adotado

O importador não tenta decidir qual artigo, nota, errata ou redação possui validade jurídica. Quando encontra valores incompatíveis para a mesma regra, ele interrompe a importação e informa ao analista que a lei precisa ser revisada. Declarações repetidas e idênticas continuam aceitas.

## Regressão adicionada

Foram incluídos três testes em `tests/test_outros_municipios.py` com as entradas exatas do relatório. Eles verificam:

- duas classes reais mesmo quando a linha termina com `(reajuste anual de 5,00%)`;
- rejeição de regras verticais de 12% e 20% para o mesmo nível;
- rejeição de declarações gerais de progressão de 5% e 8%.

Os demais 43 testes da v0.5 permanecem na suíte para cobrir API, TCE, cálculos financeiros, documentos, análise salarial, Excel e PDF.
