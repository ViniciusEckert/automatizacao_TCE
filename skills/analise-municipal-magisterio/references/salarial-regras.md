# Módulo salarial — PSPN, carreira e parser

## Conteúdo
- Princípio do módulo
- Dossiê municipal (aquisição)
- Modelo de entrada estruturada
- Piso proporcional e centavos
- Progressão horizontal e vertical
- Comparação e defasagem
- Validação estrutural
- Parser de documentos
- Limites e premissas

## Princípio do módulo

A tabela salarial **não vem do TCE**: vem de documento municipal (lei, anexo, HTML, PDF, DOC). Cada prefeitura publica de um jeito (matriz, lista, anexo, HTML). Por isso a aquisição é separada da comparação: primeiro registra-se um dossiê auditável; só depois estrutura-se e calcula-se.

## Dossiê municipal (DEC-032 a 034)

- Reúne **tabela vigente** (obrigatória), **plano de carreira** e **ato de reajuste** (recomendados), porque vigência e regras dependem dos três.
- Guarda URL, competência, horário (`America/Sao_Paulo`), originais, **SHA-256** e `manifesto.json` em `data/raw/salarios/<municipio-uf>/<ano>/<dossie>/`.
- **Não baixa URL informada automaticamente** (evita conteúdo arbitrário e documento desatualizado).
- Status: `parcial_para_triagem` ou `completo_para_triagem`.
- Diagnostica `requer_ocr` (PDF sem texto) e `requer_conversao` (DOC/XLS legado); não executa OCR.

## Entrada estruturada

Cada análise: município, ano, lei, arquivo-fonte, jornada semanal, PSPN 40h, regras entre classes, modo de centavos, lista de níveis. Cada nível: `codigo`, `descricao`, `regra_vertical{tipo,valor,nivel_referencia}`, `valores[]`.

- Códigos de nível: alfabéticos (`A`), romanos (`II`) ou numéricos (`01`).
- `regra_vertical.tipo`: `base`, `percentual` ou `valor_fixo` (reais).
- O **primeiro nível é a base** (DEC-019). Todos os níveis têm a mesma quantidade de classes e vencimentos > 0.
- Carreira que não parte do primeiro nível: **regra pendente** (não assumir equivalência).

## Piso proporcional e centavos

```text
piso proporcional exato = PSPN 40h x jornada semanal / 40
Ex. 2026: R$ 5.130,63 x 20 / 40 = R$ 2.565,315
```

PSPN 2026 vem da Lei Federal 15.437/2026 conforme os docs do projeto; **não estender a outros anos nem a outras profissões**. Jornada, PSPN e centavos são **parâmetros** (DEC-017), sempre com aviso quando não confirmados na fonte.

| Modo | Implementação | Uso |
|---|---|---|
| `truncar` | `ROUND_DOWN` a cada etapa | reproduz os 36 valores do anexo de Cafezal |
| `arredondar` | `ROUND_HALF_UP` a cada etapa | padrão das novas análises |

Aplicar o modo **a cada etapa**, sobre o valor exibido na etapa anterior; usar `Decimal`, nunca `float` no cálculo. Exemplo (truncar): classe 1 nível A = 2.565,31; classe 2 = trunc(2.565,31 x 1,02) = 2.616,61; nível B classe 1 = trunc(2.565,31 x 1,12) = 2.873,14. O modo aparece em resultado, Excel e PDF.

## Progressão horizontal (entre classes)

```text
próxima classe = centavos(classe anterior x (1 + percentual da transição / 100))
```

- Uniforme (Cafezal: 2%) **ou** lista por transição (ex. `5%, 5%, 10%, 10%`), cada posição só no seu par de classes (DEC-024).
- `progressao_classes_origem`: `declarada` (no documento), `informada` (pelo usuário) ou `inferida` (da 1ª linha). **Inferida exige aviso obrigatório de confirmação.**

## Progressão vertical (entre níveis)

A 1ª classe de cada nível adicional parte do nível de referência (explícito):

```text
percentual:  B1 = centavos(A1 x 1,12)      C1 = centavos(A1 x 1,27)
valor fixo:  B1 = centavos(A1 + R$ 300,00)
```

As demais classes seguem a lista horizontal. Modelar por tipo, valor e nível de referência (DEC-025).

## Comparação

```text
diferença monetária  = atual - referência
defasagem percentual = (referência / atual - 1) x 100
```

Negativo/positivo respectivamente = município abaixo da referência; zero = equivalente nos centavos exibidos. `resumo.situacao`: `compativel` ou `abaixo_referencia`. **A fórmula de defasagem ainda aguarda confirmação do professor** — manter como parâmetro documentado.

## Validação estrutural

Tolerância de **R$ 0,01** entre o valor lido e o recalculado pela regra. Divergências maiores vão para `inconsistencias_estrutura`. Verificar: cada transição horizontal, a classe inicial de cada nível, mesma quantidade de classes, códigos únicos, vencimentos positivos.

## Parser de documentos

- PDF: texto extraível (OCR externo se for imagem). DOCX: parágrafos e tabelas. DOC: LibreOffice ou `antiword`, opcional (DEC-020). Também CSV/TSV/XLSX/HTML via revisão.
- Reconhece valores brasileiros com/sem milhar; frases como `Percentual entre classes = 2%`, `Interstício de 5% entre classes`; listas por transição; `Nível B = Nível A acrescido de 12%` ou `de R$ 300,00`.
- **Linha com "Nível" e >= 2 valores que não pôde ser interpretada → a importação falha citando a linha** (DEC-023).
- Percentuais em notas não viram classes; regras verticais/progressões conflitantes **interrompem** com erro claro; o sistema nunca escolhe a redação legal vigente.
- PDFs multipágina/continuação: exigir conferência do recorte; não converter tabela parcial em carreira completa presumida.

### Casos adversariais para testar (os 3 bugs do QA v0.5 vieram daqui)

1. Nota com percentual no rodapé próximo a uma tabela.
2. Mesma regra vertical declarada duas vezes com valores diferentes.
3. Texto com revogação ("fica revogado…") junto da tabela — hoje passa **sem aviso** (lacuna conhecida).
4. Código de nível romano, número com zero à esquerda, valores sem milhar.
5. Tabela dividida em blocos de continuação (carreiras longas, ex. Curitiba: 184 vencimentos).

## Limites e premissas

O sistema compara números conforme os parâmetros. Não conclui validade da lei, direito a reajuste nem disponibilidade financeira. Cenário percentual aplicado à base inicial **não representa ato de reajuste aprovado**. Curitiba Administrativo +5% é cenário didático.
