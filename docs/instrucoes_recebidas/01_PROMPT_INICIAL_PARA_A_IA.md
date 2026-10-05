# Prompt inicial — copiar e colar (anexar os arquivos listados no fim)

Você vai **evoluir** o sistema "Análise Municipal / Jornada Magistério" (MVP v0.8.1) para uma versão melhor. Não recrie do zero: o núcleo já é validado e os números batem com o relatório-modelo do professor. O ganho está em fidelidade do Excel, leitura de documentos reais, rastreabilidade e robustez.

## 1. Arquivos que você recebeu e ordem de leitura
1. `Documento_Unico_Recriacao_Projeto_Jornada.docx` — contrato, regras, verificação e plano. Leia inteiro, principalmente as Partes 0, II e III.
2. `Projeto_Jornada_Magisterio_MVP_v0_8_1.zip` — código, 108 testes, `docs/`, e os materiais do professor em `referencias/materiais_professor/` (`Exemplo_Painel.xlsx`, `Jornada_Relatorio_Referencia.pdf`, `Anexo_A_LC_064_2026_Magisterio.doc`).
3. `analise-municipal-magisterio.skill` — regras do projeto. Se seu ambiente aceita skills, instale; se não, leia o `SKILL.md` e as referências e aplique como regras.
4. `REQUISITOS_DO_VIDEO.md` — o que o professor mostrou e disse no vídeo (relato de segunda mão; ver regra 6).

## 2. Hierarquia de fontes (quando houver conflito)
Arquivos e respostas do professor > requisitos do vídeo confirmados > documento único > código e testes > hipóteses. Se o documento e o código divergirem, **vale o código**; reporte a divergência.

## 3. Regras inegociáveis
- Não invente fórmula, regra ou dado. Premissa não confirmada vira **parâmetro configurável com aviso visível**, nunca constante escondida.
- Falhe com clareza; nunca devolva sucesso parcial silencioso nem zero no lugar de dado ausente.
- Extração por rótulo, nunca por posição de linha. Cada número com origem rastreável.
- O front não calcula. Cálculo salarial em `Decimal`, com arredondamento por etapa.
- Preserve as 28 rotas e o contrato de erros JSON. Renomeações precisam de compatibilidade com perfis antigos.
- Nenhuma conclusão jurídica; nenhum dado sigiloso no Git; nenhuma URL baixada automaticamente.
- Cafezal do Sul e Curitiba são amostras, nunca esquema universal. PSPN vale só para o magistério.
- Classifique cada proposta como: **implementado**, **a reimplementar**, **evolução solicitada** ou **decisão pendente**. Não anuncie como existente o que é plano.

## 4. Antes de programar (faça nesta ordem)
1. Rode `python -m unittest discover -s tests -v` e informe o resultado (esperado: 108 aprovados). Se não puder executar código, diga isso e não afirme que testou.
2. Gere os Excel de exemplo pelas rotas reais e guarde como **linha de base**.
3. Entregue um plano de no máximo uma página e **uma única lista de perguntas agrupadas** (não pergunte uma por vez).
4. Prossiga com os itens 1 a 3 abaixo usando parâmetros configuráveis, sem esperar as respostas. **Pare e pergunte** antes de qualquer mudança que altere contrato de rota ou formato de dados persistido.

## 5. Trabalho, em ordem de prioridade (com critério de aceite medido)

**P1. Excel financeiro fiel a `Exemplo_Painel.xlsx`.** Hoje o Painel difere do modelo. Reproduza: título "PAINEL ORÇAMENTÁRIO/FISCAL" e "Município: … - PR"; cabeçalho com os anos; por indicador, as linhas de valor, evolução acumulada contra o ano-base (`=(C6/$B$6)-1`) e evolução anual (`=(C6/B6)-1`); rótulos do modelo; percentual de despesa com formatação condicional pelos limites **lidos do relatório**; as três barras de limite (máximo, prudencial, alerta); linha de MDE com a nota do limite de 25%; rodapé "Fonte: SIM-AM, TCE-PR" com a data da coleta; gráfico de barras. Itens ambíguos (média anual dividida por 7 ou 6, rótulo RREO ou RGF para a RCL ajustada, comparativo do primeiro semestre, regra de 25% do MDE) entram como **parâmetros com padrão provisório e aviso**, listados nas perguntas.
*Aceite:* teste de fidelidade estrutural contra o modelo (rótulos, padrões de fórmula, preenchimentos, formatos numéricos); renderização lado a lado salva como evidência; recálculo no LibreOffice com zero erros; valores armazenados idênticos ao recálculo; valores conferidos contra os dados de Curitiba 2019–2025.

**P2. Excel salarial e PDF.** Compare as páginas 8 a 11 do `Jornada_Relatorio_Referencia.pdf` com o Excel gerado (percentuais ao lado de "Classes", posição do destaque vermelho, cores). Adicione orientação e ajuste de impressão nas abas Parâmetros, Dados originais e Fontes e premissas. Permita relatório PDF para referências que não sejam PSPN.
*Aceite:* reproduz referência 2.433,89, diferença −314,57 e defasagem 14,84% (já há teste); lista de diferenças visuais fechada ou justificada; Cafezal com 36 valores e Curitiba com 184 preservados.

**P3. Leitura de documentos reais.** Os 5 arquivos de `referencias/fontes_salariais_2026_09_07/` (Curitiba e Londrina em PDF; Cafezal, Maringá e Ponta Grossa em HTML) hoje geram **zero candidatos**. Teste `pdfplumber`/`camelot` e extração de tabelas HTML, sempre com revisão humana quando houver dúvida.
*Aceite:* ao menos 3 dos 5 geram tabela **conferida à mão** contra o documento; os demais falham com mensagem clara; nenhum sucesso parcial silencioso; testes com PDF e HTML sintéticos pequenos; versões das bibliotecas fixadas.

**P4. Rastreabilidade.** Versione cada coleta bruta por data e hash (hoje a mesma seleção sobrescreve o CSV); vincule a exportação financeira a uma análise registrada.
*Aceite:* duas coletas da mesma seleção coexistem; a exportação aponta a coleta de origem.

**P5. Robustez da fonte TCE.** Isole o adaptador WebForms atrás de uma interface, com testes de contrato sobre HTML/CSV salvos, cache com validade, e andamento visível na tela. Sem internet, **não afirme** que testou a consulta real; registre como não verificado.

**P6. Dívida técnica (só depois de P1 a P4).** `pytest` mantendo os testes atuais, blueprints sem mudar URLs, `Decimal` nos valores monetários financeiros, CI em Ubuntu e Windows, unificação das duas interfaces.

**P7. Banco relacional, API estruturada, coleta em lote, Next.js.** Dependem do escopo do artigo: **apresente apenas um desenho e aguarde decisão**; não implemente.

## 6. Sobre o vídeo
`REQUISITOS_DO_VIDEO.md` foi produzido por outra IA que assistiu ao vídeo. Trate cada item como **provisório**. Use-o para entender o fluxo e o resultado esperado; não atribua ao professor detalhe visual que só esteja ali. Se um requisito do vídeo contradisser o `Exemplo_Painel.xlsx` ou o PDF-modelo, **o arquivo do professor vale** e a divergência vai para a lista de perguntas.

## 7. Definição de pronto (para cada entrega)
Suíte completa aprovada; teste novo para cada mudança; Excel recalculado no LibreOffice sem erros; cache igual ao recálculo; renderização conferida; `CHANGELOG.md`, dicionário de dados e documentação atualizados; seção **"Não verificado"** (consulta real ao TCE-PR, Windows real, navegador real, Microsoft Excel, celular).

## 8. Formato das respostas
Português do Brasil, direto. A cada entrega: o que mudou, evidência, o que **não** foi verificado e as decisões pendentes. Entregue o projeto em ZIP versionado (v0.8.2, v0.8.3…) e o diff em relação à versão anterior.

## 9. Se você não executa código
Diga isso logo. Nesse caso, produza apenas: plano, lista de perguntas, especificação de testes e os trechos de código revisáveis, marcando tudo como **não executado**.
