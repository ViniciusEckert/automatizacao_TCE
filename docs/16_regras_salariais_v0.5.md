# Regras salariais da v0.5

## Entrada estruturada

Cada análise possui município, ano, lei, arquivo-fonte, jornada semanal, PSPN de 40 horas, regras entre classes, modo de centavos e uma lista de níveis. Cada nível mantém código, descrição, regra vertical e vencimentos por classe.

Os códigos podem ser alfabéticos (`A`, `B`), romanos (`I`, `II`, `III`) ou numéricos (`01`, `02`). A regra vertical possui `tipo`, `valor` e `nivel_referencia`; o tipo pode ser percentual ou valor fixo em reais.

O primeiro nível é a base da carreira. Todos os níveis precisam possuir a mesma quantidade de classes e vencimentos maiores que zero.

## Piso proporcional

```text
piso proporcional exato = PSPN de 40h × jornada semanal / 40
```

Para a amostra de 2026:

```text
R$ 5.130,63 × 20 / 40 = R$ 2.565,315
```

## Modos de centavos

### `truncar`

Descarta valores além de dois centavos em cada etapa. Reproduz os 36 valores do anexo de Cafezal do Sul.

```text
classe 1 do nível A = truncar(2.565,315) = 2.565,31
classe 2 do nível A = truncar(2.565,31 × 1,02) = 2.616,61
nível B, classe 1 = truncar(2.565,31 × 1,12) = 2.873,14
```

### `arredondar`

Usa arredondamento comercial (`half up`) em cada etapa.

```text
classe 1 do nível A = arredondar(2.565,315) = 2.565,32
```

O modo sempre aparece no resultado, no Excel e no PDF.

## Progressão horizontal uniforme ou variável

Cada nível progride sequencialmente a partir do valor exibido na classe anterior:

```text
próxima classe = centavos(classe anterior × (1 + progressão da transição / 100))
```

Na amostra de Cafezal, todas as transições usam 2%. Outras carreiras podem informar uma lista, como `5%, 5%, 10%, 10%`. Nesse caso, cada posição é aplicada somente ao par de classes correspondente.

Se o documento não declarar a regra, o importador pode inferir os percentuais a partir da primeira linha da tabela, mas adiciona um aviso obrigatório de confirmação.

## Progressão vertical percentual ou fixa

A primeira classe de cada nível adicional parte da primeira classe do nível base:

```text
nível B, classe 1 = centavos(nível A, classe 1 × 1,12)
nível C, classe 1 = centavos(nível A, classe 1 × 1,27)
```

Uma lei também pode definir valor fixo:

```text
nível B, classe 1 = centavos(nível A, classe 1 + R$ 300,00)
```

O nível de referência é explícito e pode ser o nível base ou um nível anterior. As demais classes seguem a lista horizontal da carreira.

## Comparação

Para cada célula:

```text
diferença monetária = valor atual - valor de referência
defasagem percentual = (valor de referência / valor atual - 1) × 100
```

- diferença negativa: valor municipal abaixo da referência;
- defasagem positiva: referência superior ao valor municipal;
- zero: equivalência nos centavos exibidos.

## Validação da estrutura

O sistema verifica:

- a regra específica de cada transição horizontal;
- a regra percentual ou fixa da classe inicial de cada nível;
- quantidade idêntica de classes;
- códigos de nível únicos;
- vencimentos positivos.

A tolerância estrutural é de um centavo. Diferenças maiores viram itens de `inconsistencias_estrutura`.

## Importação de documentos

- PDF: usa texto extraível; documento somente imagem exige OCR externo.
- DOCX: lê parágrafos e tabelas.
- DOC: converte para texto com LibreOffice ou `antiword`, quando instalado.

O importador reconhece:

- níveis com letras, romanos ou números;
- valores brasileiros com ou sem separador de milhar;
- frases como `Percentual entre classes = 2%` e `Interstício de 5% entre classes`;
- listas com um percentual por transição;
- regras como `Nível B = Nível A acrescido de 12%`;
- regras como `Nível B = Nível A acrescido de R$ 300,00`.

Se uma linha contiver `Nível` e pelo menos dois valores, mas não puder ser interpretada, a importação falha com a linha problemática. A família v0.5 não entrega sucesso com níveis descartados.

Na correção v0.5.1, valores percentuais em notas, como `(reajuste anual de 5,00%)`, deixam de ser tratados como dinheiro. Se o documento declarar duas regras verticais diferentes para o mesmo nível ou duas progressões gerais incompatíveis, a importação é interrompida. O sistema não escolhe automaticamente qual redação legal está vigente.

## Fonte federal informada na amostra

Lei Federal nº 15.437/2026: `https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15437.htm`.

## Limites da conclusão

O sistema compara números conforme os parâmetros. Ele não conclui sozinho que uma lei é válida, que há direito a reajuste ou que o município possui disponibilidade financeira. Jornada, vigência, enquadramento e interpretação jurídica permanecem sob revisão humana.
