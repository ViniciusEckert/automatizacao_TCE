# Índice da documentação

| Arquivo | Finalidade | Quando atualizar |
|---|---|---|
| `01_visao_geral.md` | Problema, objetivos, stakeholders e escopo | Quando o escopo mudar |
| `02_requisitos.md` | Requisitos, regras e situação de implementação | Após novos materiais ou validações |
| `03_processos_as_is_to_be.md` | Processo manual e fluxo automatizado atual | Quando o fluxo real mudar |
| `04_arquitetura.md` | Componentes, tecnologias e estrutura | Quando houver decisão técnica |
| `05_equipe_e_responsabilidades.md` | Papéis dos 7 integrantes | Quando a divisão mudar |
| `06_backlog_e_roadmap.md` | Concluído, prioridades e próximos ciclos | Toda semana |
| `07_plano_qa.md` | Estratégia, testes e validação manual | Antes e depois de cada entrega |
| `08_riscos.md` | Riscos, impactos e respostas | Quando surgir ou mudar um risco |
| `09_decisoes.md` | Histórico de decisões | Sempre que houver decisão relevante |
| `10_estado_atual.md` | Fotografia objetiva da versão 0.6.1 | Ao final de cada semana |
| `11_dicionario_de_dados.md` | Campos financeiros e salariais | Quando uma fonte for analisada |
| `12_apresentacao_21_08.md` | Roteiro e contingência da apresentação | Até 21/08/2026 |
| `13_guia_codigo_base.md` | Ordem de estudo e reescrita do código | Sempre que o código mudar |
| `14_mapeamento_tce_fundeb.md` | Relatórios, períodos e mudanças de layout | Quando o portal mudar |
| `15_materiais_necessarios.md` | Arquivos e respostas que ainda faltam | Quando um item chegar |
| `16_regras_salariais_v0.5.md` | Fórmulas, regras variáveis e limites do módulo salarial | Ao validar nova lei/tabela |
| `17_escopo_confirmado_v0.6.md` | Separa requisitos, exemplos, validações e itens fora do MVP | Quando uma fonte oficial mudar o escopo |
| `18_aquisicao_dados_salariais_v0.6.1.md` | Fontes oficiais, dossiê bruto e limite entre aquisição e comparação | Ao incluir município, formato ou regra de coleta |
| `evidencias/validacao_curitiba_2019_2025.md` | Evidência da coleta histórica real | Após nova execução validada |
| `evidencias/Analise_Salarial_Cafezal_do_Sul_2026.xlsx` | Modelo salarial recalculável | Após alterar regras salariais |
| `evidencias/Relatorio_Salarial_Cafezal_do_Sul_2026.pdf` | Relatório visual da amostra real | Após alterar o PDF |
| `evidencias/Painel_Financeiro_Curitiba_2019_2025.xlsx` | Painel financeiro inspirado no modelo recebido | Após alterar o Excel histórico |
| `evidencias/correcao_qa_v0.5.md` | Confirmação e regressão dos bugs apontados no QA | Após nova rodada de QA |
| `evidencias/correcao_qa_v0.5.1.md` | Correção da contaminação por notas e de regras conflitantes | Após a varredura final do QA |
| `evidencias/validacao_cafezal_londrina_2024.md` | Validação real do TCE em dois municípios adicionais | Após nova coleta oficial |
| `evidencias/validacao_escopo_interface_v0.6.md` | Diagnóstico do fallback Curitiba e validação da correção | Após alterar catálogo, amostras ou downloads |
| `evidencias/validacao_aquisicao_salarial_v0.6.1.md` | Testes da nova etapa, tzdata e separação entre aquisição/comparação | Após alterar fontes, formatos ou manifesto |

## Status usados

- **Implementado:** existe no código e possui teste automático ou execução validada.
- **Validado em Curitiba:** conferido na amostra indicada; ainda requer amostragem em outros municípios.
- **Implementado com premissa:** funciona, mas uma informação não declarada na fonte continua visível e exige confirmação.
- **Pendente de material:** depende de arquivo ou decisão externa; não deve ser inventado.
- **Fora do MVP:** não faz parte da primeira prova de conceito.

## Modelos

- `templates/ata_reuniao.md`
- `templates/registro_decisao.md`
- `templates/relatorio_teste.md`
- `templates/relatorio_semanal.md`
