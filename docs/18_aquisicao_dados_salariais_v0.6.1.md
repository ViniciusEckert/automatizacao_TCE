# Aquisição dos dados salariais — MVP 0.6.1

## Decisão principal

Cafezal do Sul é a referência de **como apresentar o resultado**. Ele não é a fonte padrão nem uma estrutura que possa ser aplicada a todas as prefeituras.

O TCE-PR fornece os indicadores fiscais do módulo financeiro, mas não oferece uma API única com as tabelas de carreira do magistério de todos os municípios. Cada prefeitura publica seus documentos em um local e formato diferente. Por isso, o módulo salarial começa por um **dossiê municipal auditável**.

## Evidências usadas

1. A orientação do professor de 24/08/2026 recomendou procurar de cinco a seis municípios nas páginas municipais de plano de cargos e salários.
2. O registro do fluxo demonstrado para professores descreve: obter a tabela municipal, identificar a carreira, montar a tabela atual, gerar a referência, comparar e calcular a defasagem.
3. O PDF `Jornada_Relatorio_Referencia.pdf` mostra o resultado esperado: base legal, estrutura da carreira, tabela atual, tabela de referência, não conformidades, diferenças monetárias e defasagem.
4. O Anexo A de Cafezal do Sul fornece uma amostra real para esse layout.

O arquivo de vídeo salarial original não está dentro do pacote atual. Os dois MP4 localizados na auditoria anterior eram de outros trabalhos e foram corretamente descartados como evidência. O fluxo acima foi confirmado pelos registros da conversa, pelo Contexto Mestre e pelo relatório do professor.

## O que deve ser obtido por município

### Item obrigatório

- **Tabela salarial vigente:** matriz, lista ou anexo com os vencimentos do magistério e sua competência.

### Itens recomendados

- **Plano de carreira ou estatuto do magistério:** explica classes, níveis, titulações, progressões e jornada.
- **Ato do reajuste vigente:** lei, decreto ou portaria que confirma percentual, data de vigência e eventual substituição de anexos.

Somente uma tabela solta pode ser registrada, mas o dossiê fica marcado como parcial. Ela não deve ser tratada como vigente sem conferir os atos associados.

## Ordem de confiança das fontes

1. anexo vigente publicado no portal oficial da prefeitura;
2. página oficial de Recursos Humanos ou Transparência;
3. diário oficial e legislação municipal;
4. documento fornecido diretamente pela prefeitura, preservando remetente e data;
5. sindicato ou notícia apenas para localizar/validar a publicação — nunca como única fonte do cálculo.

Nesta versão, a URL é registrada como evidência, mas a aplicação **não baixa automaticamente URLs informadas pelo usuário**. Isso evita buscar conteúdo arbitrário e evita escolher silenciosamente um arquivo desatualizado em portais com JavaScript, CAPTCHA ou várias vigências.

## Municípios-piloto e diferenças encontradas

| Município | Ponto oficial | Forma observada | Consequência para a próxima fase |
|---|---|---|---|
| Cafezal do Sul | [Legislação municipal](https://www.cafezaldosul.pr.gov.br/index.php?novo_cliente=12145&pagina=20&sessao=b054603368xsb0) | leis e anexos; exemplo recebido em DOC | referência visual de níveis x classes, não esquema universal |
| Curitiba | [Gestão de Pessoal/Transparência](https://www.transparencia.curitiba.pr.gov.br/conteudo/gestaodepessoal.aspx) | PDF anual compilando muitas carreiras | localizar e recortar somente Profissional do Magistério/Professor |
| Londrina | [PCCS do Magistério](https://portal.londrina.pr.gov.br/menu-oculto-recursos-humanos/legislacao-rh-portal-servidor/plano-de-cargos-carreiras-e-salarios-do-magisterio-publico-municipal-do-poder-executivo-do-municipio-de-londrina) | anexos separados e muitas referências | modelar referência/interstício sem forçar uma matriz 3 x 12 |
| Maringá | [Tabela Salarial](https://transparencia.maringa.pr.gov.br/portaltransparencia/1/publicacoes/4383) | PDF/DOCX em portal que usa JavaScript | aquisição manual assistida e registro da URL do arquivo |
| Ponta Grossa | [Estrutura Salarial](https://rh.pontagrossa.pr.gov.br/estatisticas/salarios) | tabela HTML por classe, nível e valor | aceitar página HTML salva e normalizar linhas depois |
| Siqueira Campos | [Estatuto do Magistério](https://siqueiracampos.pr.gov.br/pagina/37/educacao/sub-pagina/48/) | tabela e estatuto anexados à página | conferir se existe documento posterior antes de comparar |

O catálogo é uma amostragem inicial, não uma lista fechada. A interface possui a opção **Outro município**.

## Fluxo implementado na v0.6.1

```text
Escolher município ou informar outro
→ abrir a página oficial indicada
→ baixar tabela, plano e ato de reajuste
→ informar município, competência, URL e tipo de fonte
→ registrar os arquivos originais
→ validar formato e integridade
→ calcular SHA-256 de cada arquivo
→ detectar PDF provavelmente escaneado ou formato que exige conversão
→ salvar originais e manifesto em data/raw/salarios/
→ parar antes da interpretação salarial
```

Formatos aceitos para aquisição: PDF, DOCX, DOC, XLSX, XLS, CSV e HTML. A aceitação no dossiê não significa que o extrator da etapa seguinte já compreenda todos eles.

## Manifesto comum

Cada dossiê recebe um `manifesto.json` com:

- identificador único;
- município, UF e ano/competência;
- URL e tipo de fonte;
- data e horário do registro em Brasília;
- observações da coleta;
- categoria, nome original, extensão, tamanho e SHA-256 de cada arquivo;
- diagnóstico de texto, OCR ou conversão;
- itens recomendados ausentes;
- próxima etapa humana obrigatória.

Os arquivos brutos não são alterados nem distribuídos no ZIP. Eles ficam somente na instalação em que foram enviados.

## Próxima fase: triagem e estruturação

Antes de gerar uma planilha, o próximo desenvolvimento deve transformar cada dossiê em um conjunto revisável:

1. confirmar qual ato está vigente na competência;
2. localizar as páginas/abas exclusivas do magistério;
3. identificar cargo, jornada e base legal;
4. separar classe horizontal, nível/titulação vertical e referência;
5. capturar os vencimentos sem perder cabeçalhos ou partes especiais/permanentes;
6. mostrar uma prévia editável para validação humana;
7. somente depois comparar com o PSPN e gerar a planilha no layout do relatório.

## Estrutura-alvo para a futura planilha

O layout de Cafezal e do relatório será reutilizado nas seções, não nas dimensões:

- identificação, competência, jornada e fontes;
- legislação e regras da carreira;
- tabela municipal atual em estrutura dinâmica;
- tabela de referência baseada no PSPN e nas regras confirmadas;
- não conformidades e premissas;
- diferença monetária por posição;
- defasagem e resumo técnico.

Não entram ainda: crawler universal, OCR automático, escolha automática de vigência, equivalência jurídica entre carreiras ou geração de conclusão sem revisão humana.
