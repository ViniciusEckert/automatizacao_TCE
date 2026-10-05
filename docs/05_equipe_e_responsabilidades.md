# Equipe e responsabilidades

## Composição atual

| Integrante | Frente | Responsabilidade principal | Revisão cruzada |
|---|---|---|---|
| Heryck | Back-end | Coleta TCE e integração geral | Cliente TCE e documentação técnica |
| Luiz | Back-end | Extração, tratamento e cálculos | Dados históricos e regras |
| Larissa | Back-end | Excel, modelos e integração | API e cálculos |
| Kauan | Front-end | Formulários, filtros e usabilidade | HTML e estados de entrada |
| Cesar | Front-end | Resultados, tabelas e gráficos | Integração com API |
| Integrante 7 — nome pendente | Front-end | Uploads, downloads e responsividade | CSS e documentação do front |
| Vinícius | QA e revisão | Casos de teste, evidências e regressão | Apoio em Python e SQL |

## Como usar o código-base

A equipe não precisa compreender tudo de uma vez. Cada responsável executa a versão 0.3, estuda seu componente, reescreve uma parte pequena em uma branch e prova que manteve o comportamento pelos testes.

## Entregas sugeridas desta versão

| Pacote | Responsável | Revisor | Evidência mínima |
|---|---|---|---|
| Coleta dos relatórios 10, 20 e 15 | Heryck | Luiz | Execução real de um ano |
| Extrações por rótulo e conversão | Luiz | Heryck | Testes de 2019 e layout 2021+ |
| Modelos e Excel histórico | Larissa | Luiz | Arquivo abre e fórmulas conferem |
| Fluxo anual/histórico | Kauan | Integrante 7 | Validação responsiva |
| Gráfico, tabela e avisos | Cesar | Kauan | Cenários completo e falha parcial |
| Uploads e estados de arquivo | Integrante 7 | Cesar | PDF, XLSX e erro de formato |
| Regressão e conferência manual | Vinícius | Responsável do pacote | Relatório de teste preenchido |

## Rotina de QA

Vinícius não possui computador disponível nos fins de semana. Pull Requests que precisem da revisão dele devem chegar com instruções, resultado esperado e evidências até o início de um dia útil. Todos continuam responsáveis por testar o próprio trabalho.

## Regras contra silos

- toda função crítica deve ser explicável por pelo menos duas pessoas;
- cada PR tem um responsável, um revisor e um critério de aceitação;
- front-end integra rotas pequenas durante a sprint, não apenas no final;
- mudanças de regra atualizam testes e documentação no mesmo PR;
- o nome do sétimo integrante deve substituir o marcador assim que for confirmado.
