# Plano de qualidade e testes

## Objetivo

Garantir que o sistema reproduza os dados e regras confirmadas, preserve a origem dos valores e apresente qualquer falha sem gerar uma conclusão enganosa.

## Estado automático

- 58 testes unitários e de integração local aprovados.
- Cobertura de API, cálculos, extração, serviço anual/histórico, módulo salarial, Excel e PDF.
- Compilação Python e validação sintática do JavaScript fazem parte do fechamento da versão.

## Matriz mínima

| Área | Cenários essenciais |
|---|---|
| Coleta | opções do portal, relatório correto, retry, indisponibilidade e bruto preservado |
| Extração | moeda brasileira, rótulo ausente, RCL/Pessoal e FUNDEB nos layouts antigo e novo |
| Cálculo | comprometimento, limites, variação anual, acumulada e pontos percentuais |
| Histórico | intervalo inválido, máximo de 10 anos, falha parcial e nenhum ano válido |
| API | campos obrigatórios, anos, amostra, uploads, 16 MB e erros 400/413/502 |
| Excel | arquivo abre, valores, fórmulas, fontes, resumo, histórico e gráfico |
| Salários | PSPN proporcional, centavos, progressões uniformes/variáveis, regra fixa/percentual, diferenças e defasagem |
| Documentos | PDF/DOCX/DOC, níveis alfabéticos/romanos/numéricos, interstício e falha sem descarte silencioso |
| PDF | arquivo reabre, quatro páginas, texto, tabelas, avisos e fonte incorporada |
| Interface | anual/histórico, carregamento, avisos, download, responsividade e teclado |

## Validações manuais prioritárias

| ID | Cenário | Resultado esperado |
|---|---|---|
| CT01 | Curitiba/2019 anual com FUNDEB | Valores iguais à evidência registrada |
| CT02 | Curitiba/2019–2025 histórico | 7 anos, 0 falhas e 21 relatórios |
| CT03 | RCL dos relatórios 10 e 20 | Diferença de R$ 0,00 nos sete anos da amostra |
| CT04 | Exportar histórico | Excel abre com abas, números e gráfico |
| CT05 | Fonte indisponível em um ano | Ano falha; outros anos permanecem |
| CT06 | PDF com texto | Diagnóstico indica texto extraível |
| CT07 | PDF digitalizado | Diagnóstico sugere OCR, sem inventar tabela |
| CT08 | Planilha `.xlsx` | Abas, dimensões e fórmulas são listadas |
| CT09 | Dois municípios adicionais | Extrações conferem manualmente por amostragem |
| CT10 | Cafezal do Sul/2026 com truncamento | 36 de 36 células iguais à referência e 0 divergências estruturais |
| CT11 | Cafezal do Sul/2026 com arredondamento | Referência inicial de R$ 2.565,32 e diferença de centavos visível |
| CT12 | Importar o `.doc` recebido | 3 níveis, 12 classes, 2%, 12% e 27% reconhecidos |
| CT13 | Exportar Excel salarial | 6 abas, 87 fórmulas e nenhum erro de referência |
| CT14 | Exportar PDF salarial | 4 páginas sem corte, sobreposição ou fonte ausente |
| CT15 | Exportar painel financeiro | fórmulas locais, 2 gráficos e nenhum link externo |
| CT16 | Níveis I/II/III | Todos os níveis e valores são preservados |
| CT17 | Níveis 01/02 e valor `2400,00` | Códigos e milhar sem ponto são interpretados corretamente |
| CT18 | Interstício de 5% | Regra horizontal reconhecida sem exigir frase literal |
| CT19 | Progressões 5%, 5%, 10%, 10% | 0 falso positivo quando a lista corresponde à tabela |
| CT20 | Nível A + R$ 300,00 | 0 falso positivo e regra fixa visível na tela, Excel e PDF |

## Evidência obrigatória

Registrar município, entidade, exercício e período, relatório, horário, valor manual, valor automático, diferença, responsável e referência da fonte. Use `docs/templates/relatorio_teste.md`.

## Critério para resultados financeiros

Uma execução automática não substitui a conferência manual inicial de uma nova estrutura de relatório ou município. Se houver divergência, bloquear a interpretação do campo afetado, preservar o bruto e abrir uma tarefa de investigação.
