# Registro de riscos

| ID | Risco | Prob. | Impacto | Resposta atual |
|---|---|---:|---:|---|
| R01 | TCE-PR alterar página, campos ou exportação | Média | Alto | Cliente isolado, erros claros e scripts de mapeamento |
| R02 | Layout dos relatórios mudar por ano | Média | Alto | Extração por rótulo; mudança 2020/2021 do FUNDEB já coberta |
| R03 | Fórmulas originais terem interpretação ambígua | Média | Alto | Implementar como parâmetro, registrar fonte e bloquear narrativa não confirmada |
| R04 | PDFs salariais variarem ou serem digitalizados | Alta | Alto | Diagnosticar amostras antes de escolher extração/OCR |
| R05 | Front e back trabalharem isolados | Média | Alto | Contratos pequenos, PRs integrados e revisão cruzada |
| R06 | QA receber tudo no fim | Alta | Alto | Entregas em dias úteis com evidência e resultado esperado |
| R07 | Equipe depender de uma pessoa | Média | Alto | Guia de estudo, divisão de reescrita e dois conhecedores por função |
| R08 | Escopo crescer antes da validação | Alta | Alto | Manter a v0.6 focada nas regras comprovadas pelo QA e ampliar amostras gradualmente |
| R09 | Resultado automático divergir do manual | Média | Alto | Preservar bruto, impedir conclusão do campo e investigar |
| R10 | Documentação ficar desatualizada | Média | Médio | Atualizar docs, testes e código no mesmo PR |
| R11 | Dados sensíveis serem versionados | Baixa | Alto | Apenas dados públicos e amostras autorizadas; raw fora do pacote |
| R12 | Histórico demorar ou sofrer instabilidade | Alta | Médio | Coleta sequencial, retry, progresso visual e falha parcial por ano |
| R13 | Amostra de Curitiba não representar todos os municípios | Média | Alto | Validar pelo menos dois municípios adicionais antes de generalizar |
| R14 | Planilha recebida conter macros ou links externos | Média | Alto | Inspecionar `.xlsx` sem executar macros e trabalhar em cópia |
| R15 | Jornada ou centavos serem assumidos como regra jurídica | Alta | Alto | Premissas aparecem como parâmetros e avisos em todas as saídas |
| R16 | Importação DOC depender do ambiente | Média | Médio | LibreOffice opcional, mensagem clara e alternativa DOCX/PDF |
| R17 | Rótulo MDE do modelo induzir conclusão errada | Alta | Alto | Não automatizar a narrativa até confirmar indicador e denominador |

## Mudança de risco até a v0.6

R02 foi reduzido pela extração por rótulo e pela validação real em Curitiba, Cafezal do Sul e Londrina; ainda exige regressão periódica quando o portal mudar. A v0.5 reduziu o risco de perda silenciosa no módulo salarial e passou a modelar progressão variável e acréscimo fixo. A v0.6 reduziu o risco de escopo aparente: a interface não trata mais Curitiba como fallback silencioso da consulta real.

## Escalonamento

Um risco de impacto alto vira tarefa do backlog quando houver sinal concreto. Divergência financeira, arquivo suspeito ou perda de rastreabilidade bloqueiam a entrega afetada.
