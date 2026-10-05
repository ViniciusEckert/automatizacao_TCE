# Regras salariais da v0.4

## Entrada estruturada

Cada análise possui município, ano, lei, arquivo-fonte, jornada semanal, PSPN de 40 horas, progressão entre classes, modo de centavos e uma lista de níveis. Cada nível mantém código, descrição, acréscimo percentual e os vencimentos por classe.

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

## Progressão horizontal

Cada nível progride sequencialmente a partir do valor exibido na classe anterior:

```text
próxima classe = centavos(classe anterior × (1 + progressão / 100))
```

Na amostra, a progressão é 2%.

## Progressão vertical

A primeira classe de cada nível adicional parte da primeira classe do nível base:

```text
nível B, classe 1 = centavos(nível A, classe 1 × 1,12)
nível C, classe 1 = centavos(nível A, classe 1 × 1,27)
```

As demais classes do nível seguem sua própria progressão horizontal. Esse detalhe é necessário para reproduzir a linha C do anexo.

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

- progressão horizontal de todas as classes;
- acréscimo da classe inicial de cada nível;
- quantidade idêntica de classes;
- códigos de nível únicos;
- vencimentos positivos.

A tolerância estrutural é de um centavo. Diferenças maiores viram itens de `inconsistencias_estrutura`.

## Importação de documentos

- PDF: usa texto extraível; documento somente imagem exige OCR externo.
- DOCX: lê parágrafos e tabelas.
- DOC: converte para texto com LibreOffice ou `antiword`, quando instalado.

O importador reconhece linhas iniciadas por `Nível`, valores brasileiros, percentual entre classes e frases do tipo `Nível B = Nível A acrescido de 12,00%`.

## Fonte federal informada na amostra

Lei Federal nº 15.437/2026: `https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/l15437.htm`.

## Limites da conclusão

O sistema compara números conforme os parâmetros. Ele não conclui sozinho que uma lei é válida, que há direito a reajuste ou que o município possui disponibilidade financeira. Jornada, vigência, enquadramento e interpretação jurídica permanecem sob revisão humana.
