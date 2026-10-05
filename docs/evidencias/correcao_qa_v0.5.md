# Evidência de correção do QA — MVP 0.5

- Data: 25/08/2026
- Entrada: `referencias/qa/QA_Relatorio_Claude_v0.4.md`
- Resultado automático: 43 testes aprovados

## Classificação dos achados

| Achado | Confirmação | Correção na v0.5 |
|---|---|---|
| Níveis I/II/III eram perdidos | Confirmado | O importador aceita códigos romanos completos e testa os três níveis |
| Níveis 01/02 falhavam | Confirmado | Códigos numéricos são reconhecidos e preservam zero à esquerda |
| Apenas a frase literal de progressão funcionava | Confirmado | `interstício`, progressão e lista por transição são aceitos; ausência pode ser inferida com aviso |
| Progressão não uniforme gerava falso erro | Confirmado como limitação do modelo | Novo campo lista um percentual para cada transição e valida cada par separadamente |
| Acréscimo vertical fixo não era representável | Confirmado como limitação do modelo | Regra vertical agora possui tipo, valor e nível de referência |
| Linha salarial desconhecida podia desaparecer | Confirmado | Uma linha com `Nível` e valores que não seja interpretada interrompe a importação com erro claro |

Durante a correção também foi encontrado um defeito não destacado no relatório: valores sem ponto de milhar, como `2400,00`, podiam ser capturados parcialmente como `400,00`. O padrão monetário foi corrigido e ganhou teste de regressão.

## Cobertura adicionada

- importação de `I`, `II` e `III`;
- importação de `01` e `02`;
- valor `2400,00` sem separador de milhar;
- redação `Interstício de 5% entre classes`;
- progressões `5%, 5%, 10%, 10%` sem divergências falsas;
- regra `Nível B = Nível A + R$ 300,00`;
- fórmulas do Excel usando cada transição e o valor fixo;
- PDF exibindo a regra fixa;
- API de upload com algarismos romanos e rejeição de linha ambígua;
- resolução parametrizada de município e entidade nos scripts do TCE.

## Situação do TCE

O código financeiro não apresentou um bug reproduzível no relatório; o bloqueio era de rede do ambiente do QA. Após parametrizar os scripts, foram executadas coletas reais de Cafezal do Sul/2024 e Londrina/2024 em 25/08/2026. As seis consultas de relatório terminaram sem falha.

```powershell
python -m scripts.testar_tce --municipio "Cafezal do Sul" --ano 2024 --json cafezal-2024.json
python -m scripts.testar_tce --municipio "Londrina" --ano 2024 --json londrina-2024.json
```

RCL ajustada, despesa total com pessoal, percentual oficial e FUNDEB conferiram com os CSVs brutos. A RCL do RREO também coincidiu com a do RGF nos dois municípios. A evidência detalhada está em `docs/evidencias/validacao_cafezal_londrina_2024.md`.

## Resultado

Os bugs salariais do relatório foram corrigidos e possuem regressão automática. A validação externa do TCE em dois municípios adicionais foi concluída. Continua pendente validar as regras salariais generalizadas com 3 a 5 documentos municipais reais de estruturas diferentes.
