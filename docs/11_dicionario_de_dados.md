# Dicionário de dados

## Identificação e rastreabilidade

| Campo | Descrição | Origem ou situação |
|---|---|---|
| `municipio_id`, `municipio` | Identificador e nome do município | Opções do TCE-PR |
| `entidade_id`, `entidade` | Identificador e nome da entidade | Opções do TCE-PR |
| `ano` | Exercício analisado | Entrada validada |
| `periodo` | Fechamento do relatório | Anual para RCL/Pessoal; 6º bimestre para MDE |
| `relatorio_id` | 10, 20 ou 15 | Portal TCE-PR |
| `coletado_em` | Data e hora da consulta | Gerado pelo sistema |
| `valor_bruto` | Texto exatamente recebido | CSV preservado em `data/raw/tce/` |
| `valor_tratado` | Número após conversão | Extração testada |

## Módulo financeiro

| Campo | Descrição | Implementação |
|---|---|---|
| `receita_corrente_liquida` | RCL publicada | Relatórios 10 e 20 |
| `receita_corrente_liquida_ajustada` | Denominador do compromisso | Relatório 20 |
| `despesa_total_pessoal` | Despesa total com pessoal | Resumo do relatório 20 |
| `percentual_oficial` | Percentual publicado | Relatório 20 |
| `percentual_calculado` | `DTP ÷ RCL ajustada × 100` | Função testada |
| `diferenca_validacao_rcl` | RCL do relatório 20 menos RCL do 10 | Controle de qualidade |
| `limites.alerta` | 90% do máximo | 48,6% na amostra |
| `limites.prudencial` | 95% do máximo | 51,3% na amostra |
| `limites.maximo` | Limite máximo publicado | 54,0% na amostra |
| `fundeb.receitas_recebidas` | Receitas recebidas do FUNDEB | Relatório 15, 6º bimestre |
| `fundeb.resultado_liquido_transferencias` | Resultado líquido das transferências | Relatório 15 |
| `fundeb.percentual_aplicacao_mde` | Aplicação constitucional em MDE | Relatório 15; opcional quando o rótulo não existe |
| `evolucao.*_percentual` | Variação contra o ano anterior | `(atual ÷ anterior − 1) × 100` |
| `comprometimento_pontos_percentuais` | Mudança do percentual calculado | percentual atual menos anterior |
| `resumo.evolucao_acumulada_*` | Primeiro para o último ano válido | `(último ÷ primeiro − 1) × 100` |
| `erros[]` | Ano e mensagem de falha | Histórico parcial |
| `avisos[]` | Problema não fatal | Ex.: FUNDEB indisponível |

## Classificação de pessoal

| Condição | Resultado |
|---|---|
| percentual abaixo de alerta | `normal` |
| percentual entre alerta e prudencial | `alerta` |
| percentual entre prudencial e máximo | `prudencial` |
| percentual igual ou acima do máximo | `limite_excedido` |

## Módulo salarial

### Dossiê bruto

| Campo | Descrição | Implementação |
|---|---|---|
| `dossie_id` | Identificador único do registro | horário em Brasília + assinatura curta do conjunto |
| `municipio`, `uf`, `ano_referencia` | Identificação e competência declarada | entrada obrigatória |
| `fonte_url`, `tipo_fonte` | Onde o analista encontrou a publicação | metadado; a URL não é baixada pelo servidor |
| `registrado_em` | Horário da aquisição | ISO 8601 em `America/Sao_Paulo` |
| `status` | `parcial_para_triagem` ou `completo_para_triagem` | depende de tabela, plano e ato de reajuste |
| `arquivos[].categoria` | tabela vigente, plano ou ato | classificação informada no upload |
| `arquivos[].sha256` | Integridade do original | hash dos bytes recebidos |
| `arquivos[].requer_ocr` | PDF sem texto extraível | diagnóstico, não execução de OCR |
| `arquivos[].requer_conversao` | DOC/XLS legado | original preservado para tratamento posterior |
| `itens_recomendados_ausentes[]` | Partes que faltam ao dossiê | plano e/ou ato de reajuste |

### Dados estruturados e comparação

| Campo | Descrição | Implementação |
|---|---|---|
| `classes[]` | Identificadores das classes | Extraído ou informado; mesma quantidade em todos os níveis |
| `tabela_atual[].codigo` | Código do nível | Letras, romanos ou números: A, II, 01 |
| `tabela_atual[].descricao` | Titulação/descrição | Ex.: Licenciatura Plena |
| `tabela_atual[].regra_vertical.tipo` | Regra entre níveis | `base`, `percentual` ou `valor_fixo` |
| `tabela_atual[].regra_vertical.valor` | Percentual ou valor em reais | Unidade depende do tipo |
| `tabela_atual[].regra_vertical.nivel_referencia` | Nível usado no cálculo vertical | Ex.: A ou nível anterior |
| `tabela_atual[].acrescimo_percentual` | Compatibilidade com regras percentuais | `null` quando a regra é fixa em reais |
| `tabela_atual[].acrescimo_valor_fixo` | Acréscimo monetário | `null` quando a regra é percentual |
| `tabela_atual[].valores[]` | Vencimentos municipais | Transcritos do documento |
| `parametros.piso_nacional_40h` | PSPN nacional informado | Entrada auditável |
| `parametros.jornada_semanal` | Carga horária usada | Entrada; gera aviso se não confirmada na fonte |
| `parametros.modo_arredondamento` | `truncar` ou `arredondar` | Aplicado em cada etapa |
| `parametros.progressao_classes_percentual` | Evolução horizontal uniforme | `null` quando varia por transição |
| `parametros.progressoes_classes_percentuais[]` | Percentual de cada transição | Uma posição entre cada par de classes |
| `parametros.progressao_classes_origem` | Origem da regra horizontal | `declarada`, `informada` ou `inferida` |
| `tabela_referencia` | Valores recalculados | PSPN proporcional + progressões |
| `diferencas` | Atual menos referência | Valor monetário por célula |
| `defasagens_percentuais` | Referência/atual menos 1 | Percentual por célula |
| `inconsistencias_estrutura` | Divergência de progressão | Tolerância de R$ 0,01 |
| `resumo.situacao` | `compativel` ou `abaixo_referencia` | Depende das células comparadas |
| `avisos[]` | Premissas e limites | Repetidos na interface, Excel e PDF |
