# Comparação salarial por profissão — v0.7.0

## Decisão autorizada pela equipe

Em 07/09/2026, Heryck autorizou avançar sem esperar a resposta do professor e escolher as regras em aberto, mantendo a organização do Excel conforme o material fornecido. As escolhas abaixo são decisões de implementação, não aprovações atribuídas ao professor.

## Organização do Excel

A referência salarial disponível é o relatório `Jornada (2).pdf`, páginas impressas 9–11. O arquivo `Exemplo.xlsx` contém exclusivamente o painel orçamentário/fiscal; não contém uma aba salarial. O vídeo original não foi recuperado nesta revisão, portanto a fidelidade foi conferida contra o relatório e o anexo recebidos.

A primeira aba, `Comparação salarial`, mantém a sequência:

1. estrutura de promoção/progressão;
2. tabela de vencimentos atual, em verde;
3. tabela de referência, em roxo;
4. interpretação das divergências e reprodução da tabela atual com alertas;
5. defasagem mensal, em vermelho;
6. destaque da defasagem percentual inicial.

Mantém classes/referências nas colunas, níveis nas linhas e a indicação de jornada. Carreiras com mais de 15 classes repetem o conjunto em blocos de até 15, preservando todas as classes. As outras abas são `Parâmetros`, `Dados originais` e `Fontes e premissas`. Não há macros.

As setas ornamentais e a diagramação do texto corrido do PDF foram traduzidas para células; não se trata de uma cópia binária de uma planilha salarial original, pois esse arquivo não foi fornecido.

## Regras adotadas

| Questão | Decisão |
|---|---|
| Profissões aceitas | Qualquer cargo informado com tabela estruturada, uma profissão/jornada/ano por análise |
| Obtenção | Upload, transcrição na grade ou exemplos documentados; o catálogo direciona para a fonte oficial |
| Referência | PSPN para magistério; piso profissional informado, referência de consultoria ou cenário para outros cargos |
| Cargo sem referência definida | O usuário precisa informar uma referência; não se presume PSPN ou salário mínimo |
| Ano | Referência e análise precisam ter o mesmo ano |
| Jornada | Até 60 h no modelo genérico; proporcionalidade exige seleção expressa, senão as jornadas devem coincidir |
| Centavos | Arredondamento comercial em cada etapa como padrão; Cafezal usa truncamento em cada etapa para reproduzir o anexo |
| Diferença mensal | Vencimento atual − referência da mesma classe/nível |
| Defasagem (%) | (Referência ÷ atual − 1) × 100 |
| Vermelho na tabela atual | Vencimento abaixo da base inicial de referência |
| Comparação da carreira | Cada célula comparada à referência correspondente; contagem distinta da comparação com a base |
| Conclusão | Comparação numérica; cenários e referências de consultoria não significam violação de piso legal |

Os valores municipais originais são entradas. As referências, diferenças, interpretações resumidas e a defasagem são fórmulas editáveis no Excel. O servidor recalcula a partir das entradas antes de exportar para não aceitar resultados adulterados no navegador.

## Fluxo de uso

1. Registre os documentos no dossiê, preservando fonte e competência.
2. Escolha a amostra de Cafezal, a de Curitiba/Administrativo, uma nova tabela ou envie um arquivo.
3. Se o arquivo reunir tabelas diferentes, selecione a candidata correta.
4. Revise os nomes das classes, códigos, descrições, valores e progressões na grade.
5. Informe cargo, município, lei, ano, jornada, referência e sua origem.
6. Marque a revisão e clique em `Recalcular referência`.
7. Baixe o Excel. Mudanças na entrada invalidam o resultado anterior.

### Importação

- CSV/TSV/XLSX/HTML em formato longo: `municipio;profissao;ano;jornada;nivel;descricao;classe;vencimento;lei;fonte_url`.
- Matriz explícita CSV/XLSX/HTML: `Nível | Descrição (opcional) | classes...`. Metadados ausentes devem ser informados na revisão.
- JSON: entrada estruturada com `niveis` ou lista de registros longos.
- PDF: extração textual por página e candidatos de tabelas reconhecíveis. Texto completo disponível para revisão. PDFs imagem precisam de OCR externo.
- DOCX/DOC: importador textual existente; DOC legado exige LibreOffice/antiword ou conversão para DOCX/PDF.
- XLS legado deve ser convertido para XLSX. Arquivos com títulos complexos, células fundidas, tabelas partidas ou formatos não reconhecidos podem exigir recorte/transcrição. Não há promessa de interpretação automática universal.

Formato longo não mistura municípios, cargos, anos ou jornadas. Duplicatas, salários não positivos, valores não finitos e classes incompletas causam erro, sem descarte silencioso. Os percentuais inferidos ficam identificados; a grade permite substituí-los pelas regras documentadas.

## Fontes e exemplos

| Município | Evidência preservada em 07/09/2026 | Situação da comparação |
|---|---|---|
| Cafezal do Sul | Anexo A da LC 064/2026 enviado pelo professor e página de legislação | Exemplo do magistério: 3 níveis × 12 classes; 36 valores reproduzidos. Jornada de 20 h é hipótese registrada, pois o anexo não a declara |
| Curitiba | Portaria SMGP nº 4/2026, PDF de janeiro de 2026 | Recorte completo da parte permanente do Anexo B1: Auxiliar Administrativo Operacional, 40 h, 4 níveis × 46 referências; 184 salários reais |
| Londrina | Anexo III da Lei 11.531/2012, atualizado até Lei 13.927/2025 | Documento histórico preservado; ainda exige recorte da carreira e confirmação de reajustes posteriores |
| Ponta Grossa | Página HTML da estrutura de salários | Página contém tabelas de classes/níveis/valores; enquadramento por cargo, jornada e vigência ainda precisam ser relacionados |
| Maringá | Página do catálogo de publicações | Página dinâmica obtida; o arquivo salarial não foi baixado nesta execução |
| Siqueira Campos | Link oficial identificado | Download do diário de 26/01/2026 retornou HTTP 403; não há novo documento local dessa fonte |

O exemplo de Curitiba usa **cenário didático de +5% na base**, de R$ 2.180,44 para R$ 2.289,46. Essa referência não é um piso da profissão nem uma proposta aprovada. As progressões de 2,8% na horizontal e 15% entre níveis são inferências matemáticas explicitadas para testar o fluxo. A parte especial do Anexo B1 fica excluída expressamente porque tem enquadramento distinto.

Links e hashes estão em `referencias/fontes_salariais_2026_09_07/fontes.json`. Os dois exemplos não significam validação completa de seis municípios. Essa amostragem documental continua pendente; o programa já aceita novas tabelas via revisão.

## Compatibilidade e limites

- Backend permanece Python/Flask. A exportação continua executável no computador da equipe com `requirements.txt`; não depende do ambiente do ChatGPT.
- `tzdata>=2024.1` permanece no requirements para Windows.
- O módulo financeiro não teve suas regras alteradas.
- O PDF legado continua específico do magistério; para as demais profissões, a entrega é o Excel.
- A validação visual foi feita nas planilhas. O navegador remoto bloqueou `localhost` com `ERR_BLOCKED_BY_CLIENT`; o fluxo foi validado pelas rotas, testes Python e sintaxe JavaScript, sem alegar teste visual completo da aplicação.
