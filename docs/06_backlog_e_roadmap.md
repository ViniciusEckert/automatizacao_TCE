# Backlog e roadmap

## Concluído até a v0.6.1

- coleta real dos relatórios 10, 20 e 15;
- preservação dos CSVs brutos;
- extração de RCL, pessoal, limites e FUNDEB;
- análise anual e histórica 2019–2025;
- evoluções, resumo, falha parcial, gráfico e Excel;
- interface funcional com consulta ao vivo separada da demonstração offline;
- painel financeiro alinhado à estrutura do Excel recebido;
- importação salarial em PDF, DOCX e DOC legado;
- tabela real de Cafezal do Sul/2026;
- referência PSPN parametrizada, diferenças, defasagem e validação estrutural;
- Excel salarial auditável e PDF técnico;
- níveis romanos e numéricos, interstício, progressão horizontal variável e acréscimo vertical fixo;
- proteção contra descarte silencioso de linhas salariais;
- scripts do TCE parametrizados por município, entidade e ano;
- carregamento anual offline de Curitiba/2019–2025, sem ficar preso em 2019;
- catálogo real confirmado com 399 municípios e cache em memória durante a execução;
- catálogo inicial de seis páginas municipais oficiais e opção para qualquer outro município;
- aquisição separada da comparação, com tabela vigente, plano de carreira e ato de reajuste;
- preservação dos originais salariais, URL, competência, SHA-256, manifesto e diagnóstico de OCR/conversão;
- 58 testes automatizados e documentação de escopo/aquisição atualizada.

## P0 - Agora: reunir amostras reais e apropriação da equipe

- colocar a v0.6.1 no repositório compartilhado;
- cada integrante executar a aplicação e os testes;
- dividir a reescrita conforme `05_equipe_e_responsabilidades.md`;
- Vinícius repetir manualmente Curitiba/2019 e mais dois anos;
- repetir periodicamente a amostragem de Cafezal do Sul e Londrina já registrada;
- ensaiar a apresentação com a amostra offline como contingência;
- confirmar o nome do novo integrante do front-end.
- montar dossiês completos de pelo menos cinco municípios a partir do catálogo oficial;
- para cada dossiê, confirmar vigência, jornada, cargo do magistério e páginas/abas relevantes;

## P1 - Validação com o professor/consultoria

- confirmar se o anexo de Cafezal do Sul realmente representa jornada de 20 horas;
- confirmar truncamento ou regra oficial de arredondamento dos centavos;
- confirmar a fórmula de defasagem e o sentido da diferença monetária;
- esclarecer a linha nomeada MDE no PDF de referência, pois os valores coincidem com DTP/RCL;
- esclarecer o denominador usado no valor monetário abaixo do limite de alerta;
- validar os arquivos de evidência e a matriz de escopo/aquisição da v0.6.1.

## P2 - Generalização salarial

- triar os dossiês de 5 a 6 municípios com estruturas diferentes;
- definir um esquema tratado que aceite matriz, lista de referências e tabela HTML;
- criar uma prévia editável antes de qualquer cálculo;
- só depois adaptar o Excel ao esquema dinâmico usando Cafezal como layout de seções;
- mapear tabelas salariais que quebram linhas ou ocupam várias páginas;
- adicionar OCR somente se houver amostras digitalizadas prioritárias;
- permitir edição manual da tabela importada antes do cálculo;
- confirmar correspondência quando os níveis municipais não partem do primeiro nível.

## P3 — Integração e qualidade

- testar múltiplos municípios e tipos de PDF;
- criar logs e medição de tempo;
- avaliar cache persistente se o cache em memória não for suficiente;
- revisar acessibilidade, mensagens e compatibilidade de navegador;
- integrar os dois módulos em um relatório único após validação do significado de MDE e da margem fiscal.

## Roadmap de seis meses

1. Requisitos e prova de conceito — concluído.
2. Coleta e tratamento financeiro — base funcional.
3. Histórico, Excel, gráficos e validação — base funcional; ampliar amostragem.
4. Aquisição salarial auditável - concluída na v0.6.1; triagem e esquema dinâmico são o próximo ciclo.
5. Integração, testes e correções - em andamento, dependente das confirmações acima.
6. Resultados, artigo e apresentação final.

## Definição de pronto

Uma tarefa termina quando o comportamento foi executado, os testes relevantes passam, a fonte do dado está registrada, nenhuma regra foi inventada e outra pessoa da equipe consegue explicar a alteração.
