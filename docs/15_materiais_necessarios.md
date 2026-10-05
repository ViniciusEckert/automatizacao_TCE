# Materiais recebidos e pendências

## Recebidos em 24/08/2026

| Material | O que confirmou | Como entrou na v0.4 |
|---|---|---|
| `Exemplo.xlsx` | painel anual, evoluções, DTP/RCL, FUNDEB, MDE, limites, cores e gráfico | nova aba `Painel financeiro`, com fórmulas locais e sem o link externo quebrado |
| `ANEXO A - LC 064.2026 MAGIST.doc` | Cafezal do Sul, 3 níveis, 12 classes, progressão de 2%, acréscimos de 12% e 27% | amostra JSON, importador DOC e 36 valores de regressão |
| `Jornada (2).pdf` | estrutura visual do relatório, tabela atual/referência, diferenças e defasagem | relatório PDF e layout das tabelas salariais |

Os originais foram preservados em `referencias/materiais_professor/`.

## O que os materiais não respondem

### 1. Jornada do Anexo A

O anexo não declara se os vencimentos correspondem a 20, 30 ou 40 horas. A coincidência com metade do PSPN de 2026 sugere 20 horas, mas isso é uma inferência. É necessário enviar a lei completa ou confirmar a jornada por escrito.

### 2. Tratamento dos centavos

O valor federal informado de R$ 5.130,63 produz R$ 2.565,315 para 20 horas. O anexo mostra R$ 2.565,31 e sua sequência é reproduzida quando cada etapa é truncada. É necessário confirmar se o truncamento é regra jurídica/contábil ou apenas efeito da planilha usada para criar o anexo.

### 3. Fórmula de defasagem

O PDF de referência é compatível com `referência / valor atual - 1`. A v0.4 usa essa expressão, mas a consultoria deve confirmar o denominador.

### 4. Rótulo MDE no PDF-modelo

A seção intitulada MDE/25% contém percentuais iguais a DTP/RCL e depois os interpreta contra o limite de alerta de pessoal de 48,6%. Isso precisa ser esclarecido antes de gerar texto conclusivo automático.

### 5. Margem monetária abaixo do alerta

O valor monetário mostrado no PDF-modelo não coincide com a aplicação simples da diferença percentual sobre a RCL ajustada. O sistema não automatiza essa frase até o responsável confirmar a fórmula e o denominador.

## Materiais ainda necessários

1. Lei completa de Cafezal do Sul associada ao Anexo A.
2. Confirmação escrita da jornada e da regra de centavos.
3. Confirmação da fórmula de defasagem e da margem fiscal monetária.
4. Dossiês reais de cinco a seis municípios: tabela vigente, plano de carreira e ato de reajuste quando separado.
5. Ao menos um PDF digitalizado se OCR for realmente necessário.
6. Valores manuais de dois municípios além de Curitiba para validar a coleta financeira.
7. Nome do novo integrante do front-end e formato final da apresentação.

## Fluxo para cada novo material

Localizar fonte oficial → registrar o dossiê bruto → confirmar vigência → selecionar o magistério → transcrever gabarito → implementar em tarefa isolada → testar → revisar com o responsável.

As páginas oficiais iniciais de Cafezal do Sul, Curitiba, Londrina, Maringá, Ponta Grossa e Siqueira Campos já foram localizadas. Isso resolve **onde começar a busca**, mas os respectivos arquivos vigentes ainda precisam ser baixados e conferidos. Veja `18_aquisicao_dados_salariais_v0.6.1.md`.
