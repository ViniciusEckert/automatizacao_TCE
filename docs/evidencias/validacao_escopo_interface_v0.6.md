# Validação de escopo e interface — MVP 0.6.0

- Data: 26/08/2026
- Motivo: a interface aparentava permitir somente Curitiba/2019 e o botão de demonstração sempre carregava esse exercício.
- Resultado automático: 50 testes aprovados.
- Sintaxe: módulos Python compilados e `static/js/app.js` validado.

## Diagnóstico confirmado

O HTML inicial continha Curitiba/2019 enquanto o JavaScript executava três consultas sequenciais para obter municípios, entidades e exercícios. Se o TCE demorasse ou alguma etapa falhasse, Curitiba permanecia visível como “opção de segurança”. Isso misturava dois conceitos:

- consulta real, que depende do catálogo do TCE;
- demonstração offline, cuja evidência preservada é Curitiba.

O coletor já era parametrizado. A falha estava na apresentação e no fallback da interface.

## Correções

| Antes | Depois |
|---|---|
| Curitiba aparecia antes de o catálogo responder | A tela informa que está conectando ao TCE e mantém a consulta desabilitada |
| Falha da fonte mantinha Curitiba e anos genéricos | A fonte é marcada como indisponível, nenhuma consulta é simulada e existe botão de nova tentativa |
| Demonstração anual fixa em Curitiba/2019 | A rota aceita Curitiba/2019 a Curitiba/2025 |
| Modo inicial anual | Modo inicial histórico, alinhado ao relatório e à planilha de referência |
| Consulta e amostra pareciam a mesma coisa | A interface explica “Consulta real” e “Demo offline” separadamente |
| URL de download era revogada imediatamente | O link é anexado, acionado, removido e a URL é liberada após pequeno intervalo |

## Integração real executada

| Verificação | Resultado |
|---|---|
| Municípios retornados pelo TCE-PR | 399 |
| Curitiba | ID 1490 |
| Cafezal do Sul | ID 868 |
| Londrina | ID 2761 |
| Entidades de Cafezal do Sul | 3 |
| Município de Cafezal do Sul | Entidade ID 12223 |
| Exercícios fechados dessa entidade | 2019–2025, 7 opções |
| Demonstração anual adicional | Curitiba/2025, 38,64% oficial |
| Exportação correspondente | HTTP 200, `analise-curitiba-2025.xlsx` |

## Limitação do ambiente de QA

O navegador remoto usado na validação não permite abrir `localhost`. Por isso a verificação foi concluída com a aplicação Flask e seu cliente de integração no mesmo processo, além dos testes de HTML/JavaScript. No computador do usuário, a página é aberta normalmente em `http://127.0.0.1:5000`.

## Conclusão

Curitiba permanece como demonstração reproduzível, mas não é mais apresentada como o único município. A consulta real foi confirmada com o catálogo completo e com outro município. O comportamento solicitado está coberto por regressão automática.
