# Visão geral

## Identificação

- Disciplina: Jornada de Aprendizagem — Engenharia de Requisitos e Gestão de Projetos.
- Curso: Engenharia de Software — 2º semestre.
- Duração prevista: aproximadamente 6 meses.
- Equipe: 7 integrantes.
- Nome provisório: Sistema de Automação da Análise Financeira e Salarial do Magistério Municipal.

## Problema

Uma consultoria analisa dados financeiros e tabelas salariais de prefeituras. O processo atual envolve consultas manuais ao TCE-PR/SIM-AM, leitura de PDFs, transcrição para Excel, cálculos, formatação e comparação. Isso consome tempo e aumenta o risco de erro e de perda da origem dos valores.

## Objetivo

Automatizar a coleta, a estruturação, os cálculos confirmados, a comparação e a exportação necessárias para apoiar a análise financeira e salarial do magistério municipal.

## Stakeholders

| Stakeholder | Interesse ou responsabilidade |
|---|---|
| Analista da consultoria | Confere, interpreta e decide como usar o resultado |
| Prefeitura municipal | Fornece documentos e recebe a análise |
| Professores municipais | Grupo impactado pelas decisões apoiadas pela análise |
| TCE-PR/SIM-AM | Fonte pública dos dados financeiros |
| Governo Federal/MEC | Fonte possível da referência do piso |
| Professor da disciplina | Orienta e avalia o projeto acadêmico |
| Equipe de desenvolvimento | Levanta requisitos, desenvolve, testa e documenta |

## Escopo implementado do Módulo 1

- consulta ao vivo destinada aos municípios e entidades publicados pelo TCE-PR;
- seleção de município, entidade e um exercício ou intervalo;
- coleta de RCL, RCL ajustada, Despesa Total com Pessoal e FUNDEB;
- preservação dos CSVs públicos;
- comprometimento, evolução anual, acumulado e classificação;
- falha parcial por exercício;
- resultado anual e histórico em tela, gráfico e Excel;
- painel financeiro com fórmulas locais e limites;
- amostra real de Curitiba/2019–2025 para demonstração offline, sem limitar a consulta real.

## Escopo implementado do Módulo 2

- importação de PDF/DOCX com texto e DOC legado;
- estrutura de nível, titulação, classe e vencimento;
- amostra real de Cafezal do Sul/2026;
- referência proporcional ao PSPN e à jornada informada;
- tratamento configurável dos centavos;
- diferença, defasagem e verificação das progressões;
- interface, Excel auditável e PDF técnico.

Cafezal do Sul é o exemplo recebido, não um modelo universal. O fluxo aceita o documento de outro município, mas novas estruturas salariais ainda exigem amostragem e testes.

## Fora do MVP atual

- aplicativo mobile, autenticação complexa e SaaS;
- chatbot, previsão financeira e BI completo;
- parecer jurídico automático;
- automação de todos os relatórios do TCE-PR;
- OCR genérico antes de comprovar prioridade com PDFs digitalizados reais;
- banco de dados antes de existir necessidade de histórico multiusuário.

Veja `17_escopo_confirmado_v0.6.md` para a matriz completa das fontes e a distinção entre demonstração, validação e requisito.

## Critério de sucesso

O projeto é bem-sucedido quando a equipe consegue explicar e reproduzir o fluxo, os valores conferem com a fonte, as falhas são visíveis e os arquivos originais podem ser incorporados sem reescrever toda a arquitetura.
