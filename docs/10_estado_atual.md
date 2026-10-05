# Estado atual - MVP 0.6.1 - 31/08/2026

## Resumo executivo

Os dois módulos possuem um fluxo demonstrável. O financeiro mantém a coleta real do TCE-PR e o painel histórico inspirado no Excel recebido. No salarial, a v0.6.1 separa a obtenção das fontes da comparação: primeiro registra um dossiê oficial e auditável; o importador, os cálculos e as exportações anteriores continuam preservados como protótipo da fase seguinte.

A v0.6.1 é suficiente para demonstrar coleta financeira e aquisição salarial com rastreabilidade. A generalização da comparação ainda depende de montar e triar dossiês reais, confirmar jornada, centavos e fórmula de defasagem e então adaptar o esquema tratado.

## Escopo auditado

- Curitiba/2019 foi a primeira prova de conceito.
- Curitiba/2019–2025 é a demonstração financeira preservada e funciona offline.
- A consulta financeira real aceita os municípios, entidades e exercícios publicados pelo TCE-PR.
- Cafezal do Sul/2026 é a demonstração salarial recebida, não uma estrutura universal.
- Cafezal do Sul e Londrina/2024 permanecem como validações financeiras adicionais.
- O TCE fornece indicadores fiscais; a tabela salarial é recebida em documento municipal separado.
- Banco de dados, machine learning, React e FastAPI não são obrigações do MVP atualizado.

Veja `17_escopo_confirmado_v0.6.md` para a justificativa por fonte.

## Módulo financeiro

- consulta anual e histórica de até 10 exercícios;
- relatórios 10, 20 e 15 do TCE-PR;
- RCL, RCL ajustada, DTP, limites, FUNDEB e aplicação MDE quando publicada;
- falha parcial por ano e preservação dos CSVs brutos;
- interface, gráfico e Excel;
- nova aba `Painel financeiro` com fórmulas locais, limites, cores e dois gráficos;
- nenhum link para a pasta externa ausente da planilha-modelo.
- validação adicional concluída em Cafezal do Sul/2024 e Londrina/2024, com RCL, DTP, percentual e FUNDEB conferidos no bruto.
- interface separa consulta real e demonstração offline, mostra o estado do TCE e permite reconexão;
- modo anual carrega qualquer ano preservado de Curitiba entre 2019 e 2025;
- catálogo real da v0.6 confirmado com 399 municípios, 3 entidades de Cafezal e 7 exercícios fechados.

### Evidência Curitiba/2019-2025

| Ano | RCL ajustada | Despesa pessoal | Receitas FUNDEB | Comprometimento |
|---:|---:|---:|---:|---:|
| 2019 | R$ 7.359.872.310,73 | R$ 2.786.074.714,14 | R$ 600.162.934,45 | 37,85% |
| 2020 | R$ 7.835.897.240,90 | R$ 2.884.571.613,07 | R$ 572.011.470,93 | 36,81% |
| 2021 | R$ 8.282.730.694,45 | R$ 3.186.380.692,32 | R$ 713.790.814,68 | 38,47% |
| 2022 | R$ 9.314.379.936,42 | R$ 3.334.993.704,03 | R$ 860.918.344,60 | 35,80% |
| 2023 | R$ 9.935.910.243,97 | R$ 4.250.070.902,71 | R$ 863.804.576,18 | 42,77% |
| 2024 | R$ 11.309.265.897,14 | R$ 4.685.119.821,38 | R$ 1.006.315.150,20 | 41,43% |
| 2025 | R$ 12.336.669.938,27 | R$ 4.766.555.515,29 | R$ 1.043.518.164,66 | 38,64% |

## Módulo salarial

- Cafezal do Sul tratado como referência de layout e amostra, não como município único;
- seis páginas oficiais iniciais e opção para informar qualquer outro município;
- dossiê com tabela vigente obrigatória, plano de carreira e ato de reajuste recomendados;
- URL, competência, observações, horário, originais, SHA-256 e manifesto preservados;
- diagnóstico de PDF sem texto e formatos que exigem conversão;
- aquisição termina antes de filtrar, estruturar ou calcular;
- amostra real de Cafezal do Sul/2026: 3 níveis x 12 classes;
- importação de PDF/DOCX com texto e DOC legado via LibreOffice;
- progressão horizontal de 2%;
- níveis B e C com acréscimos de 12% e 27%;
- códigos de nível alfabéticos, romanos e numéricos;
- progressão uniforme ou diferente por transição de classe;
- regra vertical percentual ou com valor fixo em reais;
- falha segura quando uma linha salarial não pode ser interpretada;
- percentuais em notas não viram classes salariais;
- regras verticais ou progressões gerais conflitantes interrompem a importação com erro claro;
- PSPN de 40 horas e jornada como parâmetros;
- referência calculada com truncamento ou arredondamento comercial;
- diferença `atual - referência`;
- defasagem `referência / atual - 1`;
- verificação das progressões da carreira;
- interface com três tabelas e avisos;
- Excel com 6 abas e 87 fórmulas auditáveis;
- PDF técnico com 4 páginas.

### Resultado da amostra com modo `truncar`

| Indicador | Resultado |
|---|---:|
| PSPN 40h informado | R$ 5.130,63 |
| Proporção matemática para 20h | R$ 2.565,315 |
| Referência exibida após truncamento | R$ 2.565,31 |
| Vencimento inicial do anexo | R$ 2.565,31 |
| Células abaixo da referência | 0 de 36 |
| Divergências estruturais | 0 |

O resultado mostra compatibilidade com a referência **sob essas premissas**. A carga horária de 20h não aparece no anexo e deve ser confirmada na lei completa.

## Qualidade técnica

- 58 testes automatizados aprovados no ambiente de validação;
- módulos Python compilados e JavaScript validado sintaticamente;
- teste de integração real confirmou catálogo, entidades, exercícios, amostra Curitiba/2025 e geração do Excel correspondente;
- dois arquivos Excel abertos e recalculados pelo LibreOffice;
- varredura de 168 fórmulas nas duas evidências sem `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` ou `#N/A`;
- todas as 4 páginas do PDF salarial renderizadas e inspecionadas;
- importação real do `.doc` recebido confirmada: 3 níveis e 12 classes.

## Pendências que impedem uso genérico

- confirmar que o anexo municipal corresponde a 20 horas;
- confirmar truncamento em cada etapa ou a regra oficial de centavos;
- obter a lei municipal completa e não apenas o Anexo A;
- confirmar com a consultoria a fórmula de defasagem;
- esclarecer as inconsistências de rótulo/denominador no PDF-modelo;
- montar e triar dossiês de cinco a seis municípios com documentos vigentes;
- criar um esquema tratado e uma prévia editável para estruturas municipais diferentes;
- testar PDFs digitalizados e decidir se OCR entra no escopo;
- confirmar o nome do novo integrante do front-end.

## Evidências

- `docs/evidencias/Painel_Financeiro_Curitiba_2019_2025.xlsx`
- `docs/evidencias/Analise_Salarial_Cafezal_do_Sul_2026.xlsx`
- `docs/evidencias/Relatorio_Salarial_Cafezal_do_Sul_2026.pdf`
- `docs/evidencias/validacao_cafezal_londrina_2024.md`
- `docs/evidencias/correcao_qa_v0.5.1.md`
- `docs/17_escopo_confirmado_v0.6.md`
- `referencias/materiais_professor/`
