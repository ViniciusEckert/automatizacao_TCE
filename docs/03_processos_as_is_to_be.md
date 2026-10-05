# Processos AS-IS e TO-BE

## Módulo 1 — Processo manual atual

```text
Identificar município e anos
→ abrir o portal do TCE-PR
→ escolher três relatórios e seus períodos
→ localizar RCL, pessoal e FUNDEB
→ copiar para Excel
→ repetir para cada ano
→ calcular, colorir, criar gráfico
→ conferir e interpretar
```

## Módulo 1 - Processo automatizado na v0.6

```text
Informar município, entidade e período
→ sistema consulta os relatórios 10, 20 e 15
→ salva os CSVs públicos brutos
→ extrai campos por rótulo e valida RCL
→ calcula comprometimento e evoluções
→ mantém anos válidos mesmo se outro falhar
→ exibe gráfico e permite baixar Excel com painel
→ analista confere e interpreta
```

O fluxo está implementado. A etapa humana continua obrigatória para interpretar viabilidade e conferir municípios ainda não amostrados.

## Módulo 2 — Processo manual atual

```text
Receber PDF municipal
→ localizar tabela salarial
→ transcrever carreira e vencimentos
→ obter tabela de referência
→ corresponder posições
→ calcular diferença e defasagem
→ formatar e interpretar
```

## Módulo 2 — Aquisição implementada na v0.6.1

```text
Escolher uma fonte oficial ou informar outro município
→ baixar tabela vigente, plano de carreira e ato de reajuste
→ registrar URL, competência e observações
→ sistema valida formatos, calcula SHA-256 e detecta OCR/conversão
→ preserva originais e manifesto sem interpretar salários
→ analista confirma vigência e escolhe o trecho do magistério
```

## Módulo 2 — Comparação preservada como protótipo

```text
Carregar amostra ou fornecer PDF/DOCX/DOC com texto
→ sistema extrai níveis, classes, percentuais e vencimentos
→ analista informa PSPN, jornada e modo de centavos
→ sistema calcula a referência e valida progressões
→ calcula diferença e defasagem por célula
→ exibe avisos e três tabelas comparativas
→ analista revisa e exporta Excel/PDF
```

O fluxo preserva a amostra de Cafezal e também suporta níveis romanos/numéricos, progressões não uniformes e acréscimo vertical fixo. Essas variações possuem testes sintéticos; ainda precisam ser validadas com documentos municipais reais. PDF apenas imagem continua exigindo OCR externo.

A aquisição e a comparação não são mais o mesmo botão. Registrar o dossiê não executa o parser nem gera uma conclusão. A triagem editável será implementada na próxima fase, antes da nova planilha dinâmica.

## Ganhos já demonstrados

- consulta repetível de 21 relatórios na amostra histórica;
- eliminação da transcrição manual dos campos financeiros mapeados;
- rastreabilidade do valor tratado até o CSV oficial;
- padronização de cálculo, aviso e exportação;
- redução do impacto de uma falha isolada do portal.
- eliminação da transcrição manual do `.doc` recebido;
- reprodução exata das 36 células salariais com premissas visíveis;
- geração repetível do Excel salarial e do relatório PDF.
