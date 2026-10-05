# Requisitos

## Requisitos funcionais

| ID | Requisito | Situação na v0.6.1 |
|---|---|---|
| RF01 | Informar município, entidade e exercício ou intervalo | Implementado para um ano ou intervalo de até 10 anos |
| RF02 | Consultar automaticamente a fonte financeira | Implementado para o TCE-PR/SIM-AM |
| RF03 | Obter RCL e RCL ajustada | Implementado; validado em Curitiba/2019–2025, Cafezal e Londrina/2024 |
| RF04 | Obter Despesa Total com Pessoal | Implementado; validado em Curitiba/2019–2025, Cafezal e Londrina/2024 |
| RF05 | Obter receitas recebidas do FUNDEB | Implementado no relatório 15, 6º bimestre (ID 32) |
| RF06 | Calcular comprometimento com pessoal | Implementado: `DTP ÷ RCL ajustada × 100` |
| RF07 | Calcular evolução anual | Implementado: `(valor atual ÷ valor anterior − 1) × 100` |
| RF08 | Calcular evolução acumulada | Implementado: `(último valor ÷ primeiro valor − 1) × 100` |
| RF09 | Classificar a situação financeira | Implementado com limites publicados no relatório 20 |
| RF10 | Gerar gráfico histórico comparativo | Implementado na interface, no Excel e no novo painel financeiro |
| RF11 | Exportar resultados para Excel | Implementado para análise anual, histórica e salarial |
| RF12 | Preservar fonte, relatório, coleta, bruto e tratado | Implementado; CSVs brutos ficam em `data/raw/tce/` |
| RF13 | Receber documento salarial municipal | Implementado para PDF/DOCX com texto e DOC legado com LibreOffice |
| RF14 | Extrair carreira e vencimentos | Implementado para códigos alfabéticos, romanos e numéricos, com falha segura |
| RF15 | Comparar tabela municipal e referência | Implementado com PSPN, jornada e modo de centavos parametrizados |
| RF16 | Calcular diferença e defasagem salarial | Implementado: `atual - referência` e `referência / atual - 1` |
| RF17 | Destacar posições abaixo da referência | Implementado na interface, no Excel e no PDF |
| RF18 | Receber e inspecionar a planilha original | Implementado; painel-modelo analisado e reproduzido sem link externo |
| RF19 | Exportar relatório salarial | Implementado em Excel auditável e PDF técnico de quatro páginas |
| RF20 | Expor premissas não declaradas | Implementado com avisos para jornada, centavos e validação jurídica |
| RF21 | Separar consulta ao vivo e demonstração preservada | Implementado; Curitiba não substitui silenciosamente uma falha do TCE |
| RF22 | Orientar a obtenção de documentos salariais oficiais | Implementado com catálogo inicial de seis municípios e opção livre |
| RF23 | Registrar um dossiê salarial sem interpretar seus valores | Implementado com tabela obrigatória, plano/ato recomendados e manifesto |
| RF24 | Preservar integridade e origem dos documentos salariais | Implementado com URL, competência, categoria, horário e SHA-256 |
| RF25 | Detectar entrada que exigirá OCR ou conversão | Implementado na aquisição para PDF sem texto e formatos legados |

## Requisitos não funcionais

| ID | Requisito | Situação |
|---|---|---|
| RNF01 | Separar coleta, extração, cálculo, persistência e exportação | Implementado em módulos |
| RNF02 | Rastrear resultados até a fonte | Implementado nos dados e nas evidências |
| RNF03 | Sinalizar falhas e campos ausentes | Implementado com erros claros e avisos por ano |
| RNF04 | Não modificar dados públicos silenciosamente | Implementado; bruto preservado e tratado separado |
| RNF05 | Permitir comparação automática e manual | Planilha de evidências pronta; validação humana continua obrigatória |
| RNF06 | Incluir novos exercícios e municípios | Suportado pela consulta dinâmica; validado também em Cafezal do Sul e Londrina/2024 |
| RNF07 | Manter documentação coerente | Atualizada para a v0.6.1 e auditada contra os materiais da Jornada |
| RNF08 | Possuir testes de regras e tratamento | 58 testes automatizados aprovados |
| RNF09 | Limitar uploads para evitar abuso acidental | 15 MB por documento do dossiê, 48 MB por requisição e validação de formato |
| RNF10 | Manter cálculos auditáveis | Parâmetros em JSON, fórmulas visíveis no Excel e fontes no relatório |

## Regras de negócio

| ID | Regra | Situação |
|---|---|---|
| RN01 | Os dois módulos pertencem à mesma análise | Confirmado |
| RN02 | Usar o fechamento anual disponível | RCL/Pessoal no resumo anual; MDE no 6º bimestre |
| RN03 | O histórico operacional começa em 2019 | Implementado para 2019 em diante na interface |
| RN04 | Fórmulas originais devem ser preservadas | Fórmulas do painel mapeadas; link externo foi removido de propósito |
| RN05 | Faixas só entram após confirmação | Limites de pessoal vêm do TCE; MDE usa 25% com campo opcional da fonte |
| RN06 | Classe, nível, titulação e vencimento permanecem relacionados | Implementado no esquema salarial e nas exportações |
| RN07 | A aplicação apoia a decisão; a conclusão é humana | Confirmado |
| RN08 | Falha em um ano não elimina os anos válidos | Implementado na análise histórica |
| RN09 | Ausência do FUNDEB gera aviso, não resultado financeiro falso | Implementado |
| RN10 | Jornada não encontrada não pode parecer confirmada | Implementado com aviso obrigatório |
| RN11 | Tratamento dos centavos deve ser reproduzível | Implementado com `truncar` ou `arredondar` em cada etapa |
| RN12 | O primeiro nível é a base da carreira | Implementado; demais níveis usam regra percentual ou fixa e referência explícita |
| RN13 | Progressões horizontais podem variar | Implementado com um percentual por transição de classe |
| RN14 | Linha salarial duvidosa não pode ser descartada | Implementado: importação falha e informa a linha |
| RN15 | Cafezal define o layout do resultado, não a estrutura de todos os municípios | Implementado na interface e na documentação |
| RN16 | Registro do documento não prova vigência | Dossiê parcial/completo continua exigindo triagem humana |
| RN17 | A aquisição deve terminar antes da filtragem e do cálculo | Implementado em rota e serviço independentes |

## Casos de uso

- **UC01 — Análise anual:** município, entidade, exercício e opção FUNDEB → dados, validação, classificação e Excel.
- **UC02 — Análise histórica:** município e intervalo → anos válidos, falhas parciais, evoluções, gráfico, resumo e Excel.
- **UC03 — Analisar tabela salarial:** amostra ou documento → extração, referência, diferenças, avisos e resumo.
- **UC04 — Inspecionar planilha original:** `.xlsx` → abas, dimensões e quantidade de fórmulas.
- **UC05 — Exportar análise salarial:** resultado → Excel recalculável e PDF técnico.
- **UC06 — Importar DOC legado:** `.doc` → conversão local com LibreOffice → tabela estruturada.
- **UC07 — Demonstração offline:** Curitiba/2019–2025 ou Cafezal/2026 → resultado reproduzível sem confundir a amostra com a consulta real.
- **UC08 — Montar dossiê salarial:** página oficial + competência + documentos → inspeção, hashes, manifesto e pendências, sem comparação automática.
