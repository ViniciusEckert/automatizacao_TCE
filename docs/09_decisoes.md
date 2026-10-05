# Registro de decisões

## Decisões vigentes

| ID | Decisão | Motivo |
|---|---|---|
| DEC-001 | Manter os módulos financeiro e salarial no mesmo sistema | Ambos apoiam a análise do reajuste do magistério |
| DEC-002 | Começar pelo Módulo 1 e Curitiba/2019 | Prova rapidamente acesso, extração e validação |
| DEC-003 | Usar Python no back-end | Adequado a automação, dados, Excel e PDF |
| DEC-004 | Não inventar fórmulas | Evita decisão incorreta e retrabalho |
| DEC-005 | Separar coleta, extração, cálculo, persistência e interface | Facilita teste e mudança de fonte |
| DEC-006 | Organizar 3 back, 3 front e 1 QA com revisão cruzada | Reflete a equipe sem criar silos |
| DEC-007 | QA recebe entregas pequenas em dias úteis | Vinícius não tem computador aos fins de semana |
| DEC-008 | Usar Flask e JavaScript puro no MVP | Reduz conceitos simultâneos para a equipe iniciante |
| DEC-009 | Preferir CSV oficial à automação de cliques | Estrutura mais estável e auditável |
| DEC-010 | Coletar relatórios em sequência | Paralelismo causou erro 500 no portal |
| DEC-011 | Usar relatório 15/MDE e período 32 para FUNDEB | É o fechamento do 6º bimestre disponível no portal |
| DEC-012 | Extrair indicadores por rótulo, não linha fixa | O layout do MDE mudou entre 2020 e 2021 |
| DEC-013 | Isolar falhas por exercício | Um ano indisponível não deve apagar anos válidos |
| DEC-014 | Tratar falha do FUNDEB como aviso no resultado anual | RCL/Pessoal válidos não devem ser descartados |
| DEC-015 | Criar inspetores de PDF/XLSX antes das regras salariais | Prepara a entrada sem presumir conteúdo ou fórmula |
| DEC-016 | Limitar análise histórica a 10 exercícios | Controla tempo e carga no portal externo |
| DEC-017 | Tratar jornada, PSPN e centavos como parâmetros | O anexo não declara todas as premissas necessárias |
| DEC-018 | Oferecer truncamento e arredondamento comercial | O primeiro reproduz o anexo; o segundo expõe a alternativa convencional |
| DEC-019 | Usar o primeiro nível como base da carreira | É a estrutura observada no Anexo A recebido |
| DEC-020 | Importar DOC legado com LibreOffice opcional | O formato binário não possui leitor Python confiável no escopo do MVP |
| DEC-021 | Não copiar o link externo da planilha-modelo | O arquivo referenciado não foi enviado e deixaria o Excel quebrado |
| DEC-022 | Não automatizar a narrativa MDE/margem fiscal | O PDF-modelo apresenta rótulos e denominadores ambíguos |
| DEC-023 | Nunca descartar silenciosamente uma linha salarial com valores | Uma tabela incompleta aparentando sucesso é mais perigosa que uma falha clara |
| DEC-024 | Representar cada transição horizontal separadamente | Algumas carreiras usam percentuais não uniformes |
| DEC-025 | Modelar a regra vertical por tipo, valor e nível de referência | Planos municipais podem usar percentual ou valor fixo em reais |
| DEC-026 | Parametrizar os scripts manuais do TCE | A validação precisa ser repetível fora de Curitiba |
| DEC-027 | Tratar Curitiba/2019–2025 como demonstração offline, não como limite funcional | APS, relatório e planilha usam municípios genéricos e seleção dinâmica |
| DEC-028 | Bloquear a consulta ao vivo quando o catálogo falha | Evita que o fallback de Curitiba pareça um resultado para outro município |
| DEC-029 | Carregar qualquer ano preservado de Curitiba no modo anual | A demonstração histórica possui sete exercícios e não deve ficar presa a 2019 |
| DEC-030 | Separar requisitos oficiais de ideias do brainstorming | Banco, ML e frameworks não são obrigatórios sem necessidade validada |
| DEC-031 | Tratar Cafezal como layout de saída, não esquema universal | As fontes municipais apresentam matrizes, listas, anexos e HTML diferentes |
| DEC-032 | Criar dossiê municipal antes da extração | Vigência e regras dependem de tabela, plano e ato de reajuste em conjunto |
| DEC-033 | Não baixar automaticamente uma URL informada | Evita conteúdo arbitrário e seleção silenciosa de documento desatualizado |
| DEC-034 | Preservar originais com SHA-256 e manifesto | Permite demonstrar origem e detectar alteração do documento analisado |
| DEC-035 | Incluir tzdata como dependência | O Windows não traz necessariamente a base IANA usada por `ZoneInfo` |

DEC-001 a DEC-016 foram aceitas em 15/08/2026. DEC-017 a DEC-022 documentam a incorporação dos materiais em 24/08/2026. DEC-023 a DEC-026 registram as correções do QA em 25/08/2026. DEC-027 a DEC-030 registram a auditoria de escopo e a correção da interface em 25/08/2026. DEC-031 a DEC-035 registram a revisão da aquisição salarial em 31/08/2026. Todas podem ser revistas por PR documentado.

## Decisões pendentes

- OCR para documentos sem texto, somente se amostras reais justificarem;
- confirmação da jornada de Cafezal do Sul e da regra oficial de centavos;
- confirmação da fórmula de defasagem e do denominador da margem fiscal;
- regra de equivalência para carreiras que não partem do primeiro nível;
- persistência em banco e autenticação, apenas se o uso exigir;
- nome definitivo do sistema e nome do sétimo integrante.
