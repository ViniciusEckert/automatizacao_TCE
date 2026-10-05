# Escopo confirmado — MVP 0.6.0

## Resposta objetiva sobre Curitiba

**Curitiba não é o único município do sistema.** Curitiba/2019 foi a primeira prova de conceito e Curitiba/2019–2025 é a demonstração financeira preservada para funcionar sem internet. Na utilização real, o analista deve selecionar o município, a entidade e o período oferecidos pelo TCE-PR.

A distinção correta é:

| Item | Município usado | Significado |
|---|---|---|
| Demonstração financeira offline | Curitiba, 2019–2025 | Evidência principal reproduzível sem depender do portal |
| Consulta financeira real | Município escolhido no TCE-PR | Escopo funcional do sistema |
| Validação financeira adicional | Cafezal do Sul e Londrina, 2024 | Casos de QA que comprovam que o coletor não está preso a Curitiba |
| Demonstração salarial offline | Cafezal do Sul, 2026 | Tabela real recebida do professor |
| Análise salarial real | Município informado e seu documento | Escopo funcional do sistema |

Não é necessário manter uma cópia offline de todos os municípios. Isso duplicaria a fonte pública e criaria dados desatualizados. A demonstração offline existe como contingência acadêmica; os demais casos são consultados ao vivo.

## Hierarquia das fontes consultadas

Quando os materiais divergiram, foi adotada a seguinte prioridade:

1. APS atualizada e arquivos fornecidos pelo professor/consultoria;
2. descrição detalhada do processo e do vídeo preservada em `referencias/Contexto_Mestre_Original.md`;
3. conversa do grupo, usada como registro de hipóteses e planejamento;
4. decisões técnicas e QA produzidos durante o desenvolvimento.

### Evidências determinantes

- A APS atualizada declara seleção de município, entidade, exercício e período, repetição para diferentes anos e reaproveitamento para diferentes períodos e municípios.
- `Jornada_Relatorio_Referencia.pdf` usa o município genérico `XYZ - PR` e apresenta uma série de seis anos, não um caso exclusivo de Curitiba.
- `Exemplo_Painel.xlsx` usa `XYX - PR`, anos de 2019 a 2025, evoluções, limites, FUNDEB e gráfico.
- `Link.docx` aponta para o portal de Relatórios de LRF do TCE-PR.
- O Anexo A da LC 064/2026 é uma tabela específica de Cafezal do Sul e serve como entrada real do módulo salarial, não como estrutura universal.
- A conversa do grupo de 08/08/2026 já previa seleção de município e período, mas misturava a origem dos dados salariais com o TCE. Os materiais oficiais posteriores corrigem essa interpretação.

Dois arquivos MP4 encontrados junto aos materiais foram inspecionados e excluídos da definição de escopo: um mostra buscas de vestuário no Pinterest e o outro uma atividade de estatística. Eles não documentam a Jornada. O fluxo relevante descrito a partir da demonstração está preservado no Contexto Mestre e determina “selecionar o município desejado”; Curitiba aparece somente como primeiro cenário de referência.

## Escopo funcional do MVP

### Módulo 1 — análise financeira

- selecionar município, entidade, um exercício ou intervalo;
- consultar relatórios públicos de LRF do TCE-PR/SIM-AM;
- obter RCL, RCL ajustada, Despesa Total com Pessoal e transferências do FUNDEB;
- calcular comprometimento, evolução anual e evolução acumulada;
- mostrar limites, classificação, fontes, avisos, tabela e gráfico;
- tolerar falha isolada de um exercício sem apagar os demais;
- gerar Excel anual ou histórico auditável;
- manter Curitiba/2019–2025 como demonstração offline.

### Módulo 2 — análise salarial

- receber tabela municipal em PDF ou DOCX com texto; aceitar DOC legado quando o LibreOffice estiver instalado;
- extrair níveis, classes, titulações, vencimentos e regras identificáveis;
- parametrizar PSPN, jornada e tratamento dos centavos;
- montar tabela de referência e calcular diferenças e defasagem;
- sinalizar valores abaixo da referência e conflitos de estrutura;
- gerar Excel auditável e relatório PDF;
- manter Cafezal do Sul/2026 como demonstração offline;
- exigir revisão humana das premissas e da interpretação jurídica.

## O que não pertence ao MVP confirmado

- pesquisar folha individual, cargos como médico/engenheiro ou remuneração de servidores no TCE;
- produzir parecer jurídico ou decidir automaticamente se o reajuste deve ser aprovado;
- automatizar todos os relatórios existentes no TCE-PR;
- manter todos os municípios em uma base offline;
- OCR genérico para PDF escaneado sem antes receber amostras prioritárias;
- aplicativo móvel, SaaS, autenticação complexa, chatbot, previsão ou BI completo;
- banco de dados ou machine learning sem uma necessidade validada;
- React, FastAPI ou outra tecnologia apenas porque apareceu no brainstorming inicial.

O banco de dados e o uso de machine learning aparecem numa versão anterior da APS. A APS atualizada detalha extração, estruturação e comparação, mas não os mantém como obrigação. A arquitetura Flask/JavaScript atual satisfaz o fluxo e pode ser substituída pela equipe depois sem alterar os requisitos.

## O que ainda precisa de validação externa

- confirmar, na lei completa, a jornada da tabela de Cafezal do Sul;
- confirmar a regra oficial de centavos e a fórmula de defasagem usada pela consultoria;
- esclarecer o rótulo MDE e o denominador da margem monetária no relatório-modelo;
- testar três a cinco tabelas salariais reais com estruturas diferentes;
- decidir sobre OCR somente após receber PDFs escaneados representativos;
- obter aceite do professor/consultoria sobre os arquivos gerados.

## Situação de conclusão

A v0.6.0 é um **MVP acadêmico completo e demonstrável** dos dois módulos. Ela ainda não deve ser chamada de produto operacional final da consultoria enquanto as validações externas acima estiverem abertas. Novas tecnologias não são necessárias para concluir a demonstração; o próximo avanço legítimo é validar regras e documentos reais.
