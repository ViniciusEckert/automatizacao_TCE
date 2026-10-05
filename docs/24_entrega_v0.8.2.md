# Entrega 0.8.2 — evolução do projeto existente

## Base e critérios

Base: ZIP 0.8.1 fornecido pelo usuário, com 108 testes aprovados antes das alterações. Os prompts 01–03 e a skill recebida orientaram esta evolução. Mantidas 28 rotas explícitas (29 incluindo a rota automática de arquivos estáticos), payloads e perfis anteriores. Não foi realizada recriação do zero.

## Implementado

- Painel financeiro com título cinza, cabeçalhos pretos por exercício, valores, evolução acumulada e anual, classificação de pessoal, três barras de limites, fontes e gráfico de barras com três séries. Limites por exercício usam os valores da análise/Histórico. A média anual é selecionável em Parâmetros do painel: exercícios (padrão compatível com o modelo), intervalos ou geométrica. Valores ausentes permanecem vazios.
- Impressão das abas auxiliares salariais configurada; preservadas as seções e cores da comparação existente e o destaque vermelho de vencimentos abaixo da base. Matrizes extensas conservam todas as classes em blocos. A coluna explícita de regra vertical foi preservada para carreiras genéricas; não se afirma identidade visual pixel a pixel.
- PDF salarial aceita referências de outras profissões, apresenta a referência informada e divide carreiras extensas em blocos de até 12 classes. Nenhum piso é inventado para uma profissão.
- Extração por coordenadas com pdfplumber 0.11.7 para os formatos reconhecidos de Curitiba e Londrina; extração HTML contextual para Ponta Grossa. Cabeçalhos e eixos explícitos, ordem numérica das referências, rejeição de matrizes incompletas e avisos de inferência. A revisão do recorte permanece obrigatória.
- CSVs brutos preservados em versões com data UTC, hash e identificador, mantendo o caminho legado para compatibilidade. O hash corresponde ao texto UTF-8 recebido pelo gravador, não necessariamente aos bytes HTTP originais.
- Cache do catálogo TCE limitado e com expiração de 24 horas; erros não são armazenados. Mantidos cookies, postbacks e coleta sequencial do cliente existente.

## Fontes reais e professor

Preservados em referencias/materiais_professor: Exemplo_Painel.xlsx, Jornada_Relatorio_Referencia.pdf e Anexo_A_LC_064_2026_Magisterio.doc. O PDF físico possui cinco páginas; as páginas impressas 9–11 fundamentam as seções salariais. Cafezal é referência de organização, não o único município ou profissão. Sua regra do nível C é 27%, conforme os arquivos e código recebidos. O modelo financeiro rotula RCL como RREO; o valor utilizado pelo coletor vem do RGF, relatório 20. Essa diferença está visível no painel e nas premissas.

Não foi recebido nesta rodada o vídeo original nem REQUISITOS_DO_VIDEO.md com transcrição e tempos. O prompt 02 foi preservado, mas não pode substituir a evidência audiovisual ausente. Nenhum trecho do vídeo foi atribuído como observado nesta rodada.

Os cinco documentos municipais preservados em referencias/fontes_salariais_2026_09_07 produziram: Curitiba 67 candidatos; Londrina 5; Ponta Grossa 59; Cafezal e Maringá zero. Os dois últimos arquivos são catálogos, não tabelas salariais completas. Isso não representa 131 carreiras juridicamente validadas nem dossiês vigentes completos. Resultados brutos da preparação em docs/evidencias/v0.8.2. Conferidos o início de Curitiba (2.180,44), NH inicial de Londrina (2.150,79) e ordenação integral de 1 a 128; os demais valores exigem revisão documental.

## Validação

118 testes passaram após as alterações, contra 108 na base. Exemplos financeiros, Cafezal e Curitiba gerados pelas rotas reais do Flask. Recalculados no LibreOffice: 105, 192 e 987 fórmulas respectivamente; nenhuma divergência de cache e nenhum erro de fórmula, dentro da tolerância numérica do verificador. Validação não equivale à aprovação do professor.

Impressão inspecionada: painel financeiro em uma página A3, sem divisão do gráfico; primeira página salarial de Cafezal e resumo PDF de Curitiba. Não foram inspecionadas visualmente todas as páginas de todas as saídas.

## Limitações e trabalho pendente

- P1: primeiro semestre não coletado; MDE não classificado automaticamente. Média e centavos são premissas provisórias editáveis. O painel explicita essas escolhas.
- P2: conferência no Microsoft Excel e reprodução visual integral do modelo do professor ainda pendentes.
- P3: extração limitada aos layouts reconhecidos; PDF imagem exige OCR externo; portais de catálogo exigem obter o documento real. Não há coleta salarial universal com um clique. Vigência, jornada, cargo e progressões devem ser confirmados; inferência matemática não substitui a lei.
- P4: versões brutas implementadas. Vínculo obrigatório de toda exportação financeira a um registro autenticado/persistido de análise não implementado: o contrato atual continua aceitando dados enviados. Exige decidir o contrato antes de quebrar compatibilidade.
- P5: cache TTL implementado; cliente WebForms existente preservado. Nova interface de fonte, serviço de tarefas e progresso por etapa não implementados.
- P6/P7: migração para pytest/blueprints, CI, banco de dados, processamento em lote e Next.js permanecem propostas, sem implementação nem promessa de funcionamento.

Não verificado: TCE ao vivo nesta rodada, Windows/Python 3.14, navegador e dispositivos móveis, Microsoft Excel e atualidade jurídica dos pisos. O erro histórico de favicon não é a causa dos 502; falhas de fonte externa devem permanecer distintas. tzdata já presente na base foi preservado. Não é possível garantir eliminação de indisponibilidade do TCE.

As mudanças não enviam e-mails, não buscam URLs arbitrárias e não inventam valores para preencher dados faltantes. Não houve alteração na fórmula de defasagem nem migração de perfis salariais existentes.
