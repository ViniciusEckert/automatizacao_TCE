# Sistema de Automação da Análise Financeira e Salarial Municipal

Projeto acadêmico da disciplina **Jornada de Aprendizagem - Engenharia de Requisitos e Gestão de Projetos**, do 2º semestre de Engenharia de Software.

## Objetivo

Reduzir o trabalho manual de uma consultoria que analisa, para prefeituras do Paraná, a capacidade financeira para reajustes e a situação das tabelas salariais por profissão ou cargo. O sistema organiza evidências e cálculos; não produz parecer jurídico nem decide automaticamente sobre reajustes.

## Estado em 07/09/2026

- Código: **MVP 0.7.2**.
- Módulo financeiro: consulta anual e histórica ao TCE-PR, sem mudança das regras nesta versão.
- Módulo salarial: aquisição, extração para revisão, grade editável por profissão, referência configurável, comparação e Excel com a organização do relatório do professor.
- Exemplos completos: Cafezal do Sul/2026, magistério (36 vencimentos), e Curitiba/2026, Auxiliar Administrativo Operacional (184 vencimentos oficiais, cenário didático de referência).
- Seis pontos oficiais de pesquisa continuam disponíveis. Isso não significa que seis dossiês completos e vigentes já estejam validados.
- Consulte `docs/19_comparacao_profissoes_v0.7.md` para as decisões adotadas e `docs/evidencias/validacao_profissoes_v0.7.0.md` para as verificações e limitações.

## Correção 0.7.2 — seleção da entidade e estabilidade local

- A entidade Município/Prefeitura aparece primeiro no catálogo, quando disponível. Isso evita que a escolha inicial caia em uma autarquia ou Câmara apenas pela ordem da lista. As demais entidades continuam selecionáveis.
- O coletor confere se a entidade oferece o relatório antes de solicitá-lo. Ausência de relatório retorna 422 com uma explicação, sem provocar a requisição que fazia o portal responder 500.
- O histórico interrompe imediatamente a consulta quando falta um relatório obrigatório no catálogo da entidade. Falhas de outros tipos preservam os motivos por ano.
- Erros de consulta/coleta passam a registrar método, caminho e mensagem no terminal. A mensagem também aparece na resposta da API.
- Incluído o ícone da aba; `/favicon.ico` passa a responder 200.
- `python app.py` inicia sem debug e sem recarregamento automático. Reinicie manualmente depois de editar o código. Para desenvolvimento com recarga deliberada, use `python -m flask --app app run --debug`.

**Para a análise financeira consolidada**, selecione a entidade `MUNICÍPIO DE ...`/`PREFEITURA ...`. Outras entidades só podem ser analisadas quando oferecem todos os relatórios exigidos. Na coleta observada, a Câmara de Cruzeiro do Sul oferece pessoal, mas não RCL; a Autarquia dos Serviços Funerários de Apucarana não oferece relatórios no seletor consultado.

Detalhes e limites: `docs/evidencias/validacao_entidades_v0.7.2.md`.

## Correção 0.7.1 — URLs e erros HTTP

Corrigido o tratamento genérico que convertia erros HTTP 404/405 em erro interno 500. Uma URL ausente agora mantém o status 404 e informa o caminho solicitado; métodos incorretos mantêm o 405 e seu cabeçalho Allow. Falhas internas continuam registradas, com método e caminho no log. O erro específico de upload acima de 48 MB permanece 413.

Essa correção não cria uma rota inexistente. Se um botão continuar apontando para um endereço ausente, copie a linha do terminal com GET/POST e o caminho para identificar a origem. Abra o sistema em `http://127.0.0.1:5000/` e recarregue com Ctrl+F5 depois de atualizar a versão.

## O que funciona

- carrega municípios, entidades e exercícios oferecidos pelo TCE-PR;
- deixa explícito quando a fonte está carregando, pronta ou indisponível, sem substituir silenciosamente a seleção por Curitiba;
- permite reconectar ao TCE e mantém a consulta bloqueada se entidade/anos não forem confirmados;
- coleta sequencialmente os relatórios 10 (RCL), 20 (Pessoal) e 15 (MDE/FUNDEB);
- preserva os CSVs públicos brutos em `data/raw/tce/`;
- extrai RCL, RCL ajustada, Despesa Total com Pessoal, limites, FUNDEB e, quando publicado, aplicação em MDE;
- calcula comprometimento, evolução anual, evolução acumulada e variação em pontos percentuais;
- mantém os anos válidos quando um exercício do histórico falha;
- exporta o histórico para Excel com a nova aba `Painel financeiro`, fórmulas locais, limites, cores e gráficos;
- extrai candidatos de PDF/DOCX/DOC, CSV/TSV/XLSX/HTML e JSON para revisão; documentos complexos podem exigir transcrição ou conversão;
- separa grupos de município, cargo, ano e jornada em dados estruturados;
- oferece uma grade para editar níveis, classes, vencimentos e regras antes de comparar;
- preserva níveis alfabéticos, romanos ou numéricos sem descartar linhas silenciosamente;
- reconhece `percentual entre classes`, `interstício` e listas de percentuais por transição;
- ignora percentuais de notas como valores salariais e bloqueia regras legais conflitantes;
- aceita progressão horizontal uniforme ou variável e regra vertical percentual ou fixa em reais;
- aceita PSPN para magistério, piso profissional informado, referência da consultoria ou cenário;
- exige anos coerentes e proporcionalidade de jornada explicitamente selecionada;
- permite escolher entre truncamento e arredondamento comercial em cada etapa;
- calcula diferença monetária, defasagem e divergências na progressão da carreira;
- exporta a comparação por profissão para Excel com fórmulas; o PDF legado continua disponível somente para magistério/PSPN;
- disponibiliza a tabela real de Cafezal do Sul/2026 como amostra offline.
- permite abrir, no modo anual, qualquer exercício preservado de Curitiba entre 2019 e 2025.
- oferece seis pontos de partida oficiais para obter tabelas salariais e aceita qualquer outro município informado pelo usuário;
- registra tabela vigente, plano de carreira e ato de reajuste em um dossiê separado da análise;
- preserva URL, competência, originais, SHA-256 e manifesto, sinalizando OCR ou conversão necessários.

## Tecnologias

- **Python e Flask:** regras, coleta, serviços e API.
- **Requests:** sessão com o portal ASP.NET do TCE-PR.
- **HTML, CSS e JavaScript puro:** interface acessível para uma equipe iniciante.
- **OpenPyXL:** Excel gerado pela aplicação.
- **pypdf e python-docx:** leitura de PDF/DOCX com texto.
- **ReportLab:** relatório PDF.
- **tzdata:** base de fusos utilizada no Windows para registrar o horário de Brasília.
- **LibreOffice opcional:** conversão de arquivos `.doc` legados. DOCX e PDF não dependem dele.

## Executar no Windows

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Abra `http://127.0.0.1:5000`.

Na primeira abertura, aguarde o aviso verde de que município, entidade e exercícios estão prontos. A consulta ao TCE depende de internet e pode demorar; o botão de demonstração funciona offline.

## Conferir a correção de Curitiba

1. Deixe `Histórico` selecionado e clique em `Abrir demo Curitiba 2019–2025`.
2. Baixe o Excel do histórico.
3. Selecione `Um exercício`, escolha 2025 e clique em `Abrir demo Curitiba/2025`.
4. Baixe `analise-curitiba-2025.xlsx`.
5. Para provar a generalização, aguarde o catálogo do TCE, selecione `CAFEZAL DO SUL`, a entidade `MUNICÍPIO DE CAFEZAL DO SUL` e um exercício fechado.

A demonstração continua em Curitiba porque é a evidência preservada. A seleção ao vivo não está limitada a ela. O detalhamento das fontes está em `docs/17_escopo_confirmado_v0.6.md`.

Para importar `.doc` legado, instale o LibreOffice ou converta o documento para DOCX/PDF. A amostra de Cafezal do Sul já vem transcrita e funciona sem essa instalação.

## Obter os dados salariais

1. Abra **Módulo salarial → Pontos de partida oficiais**.
2. Escolha um dos seis municípios-piloto ou `Outro município`.
3. Abra a página oficial e baixe a tabela vigente; sempre que possível, baixe também o plano de carreira e o ato de reajuste.
4. Informe competência e URL e clique em `Registrar documentos brutos`.
5. Confira hashes, itens ausentes e alertas de OCR/conversão.

O registro preserva o documento; a revisão e a comparação são as etapas seguintes. Veja `docs/18_aquisicao_dados_salariais_v0.6.1.md` para o dossiê.

## Comparar uma profissão e gerar o Excel

1. No módulo salarial, abra uma das duas amostras, escolha `Nova tabela por profissão` ou envie um arquivo em `Extrair para revisão`.
2. Se houver mais de uma tabela candidata, escolha a profissão e a jornada corretas.
3. Confira todos os vencimentos, classes e regras na grade. Para testar o formato longo, use `data/modelos/curitiba_administrativo_2026.csv`; o cabeçalho vazio está em `data/modelos/importacao_profissoes.csv`.
4. Informe município, profissão, ano, jornada e a referência salarial com sua fonte. Campos não encontrados no documento precisam ser preenchidos.
5. Marque `Revisei a tabela e os parâmetros da comparação` e clique em `Recalcular referência`.
6. Baixe o Excel. Editar a entrada invalida o resultado anterior.

A primeira aba mantém estrutura, tabela atual verde, referência roxa, interpretação e alertas, diferenças mensais e destaque da defasagem. As abas auxiliares guardam parâmetros, dados originais e fontes. Carreiras longas repetem esses mesmos blocos sem omitir classes.

**Regras escolhidas pela equipe:** arredondamento comercial como padrão; Cafezal usa truncamento para reproduzir o anexo. Ambos podem ser alterados. O PSPN não é aplicado a outras profissões. A referência de Curitiba é um **cenário didático de +5% na base inicial**, não um piso legal nem um reajuste aprovado.

## Executar os testes

```powershell
python -m unittest discover -s tests -v
```

## Testar a integração real

```powershell
python -m scripts.testar_tce
python -m scripts.testar_tce --municipio "Cafezal do Sul" --ano 2024
python -m scripts.testar_tce --municipio "Londrina" --ano 2024 --json londrina-2024.json
```

Uma análise anual consulta três relatórios e pode levar cerca de 30-60 segundos. O histórico 2019-2025 faz 21 consultas sequenciais e pode levar alguns minutos. O sistema evita paralelismo porque o portal antigo apresentou erros em gerações simultâneas.

## Evidências prontas da v0.7.0

- `docs/evidencias/v0.7/Comparacao_Cafezal_2026.xlsx`
- `docs/evidencias/v0.7/Comparacao_Curitiba_Administrativo_2026.xlsx`
- `docs/evidencias/validacao_profissoes_v0.7.0.md`
- `docs/19_comparacao_profissoes_v0.7.md`
- `referencias/fontes_salariais_2026_09_07/` — documentos públicos coletados e manifesto de origem

## Evidências históricas preservadas

- `docs/evidencias/Painel_Financeiro_Curitiba_2019_2025.xlsx`
- `docs/evidencias/Analise_Salarial_Cafezal_do_Sul_2026.xlsx`
- `docs/evidencias/Relatorio_Salarial_Cafezal_do_Sul_2026.pdf`
- `docs/evidencias/validacao_cafezal_londrina_2024.md`
- `docs/evidencias/TCE_Cafezal_do_Sul_2024.json`
- `docs/evidencias/TCE_Londrina_2024.json`
- `docs/evidencias/correcao_qa_v0.5.1.md`
- `docs/17_escopo_confirmado_v0.6.md`
- materiais originais preservados em `referencias/materiais_professor/`

## Premissas salariais que continuam explícitas

- A lei federal informada para o PSPN de 2026 fixa R$ 5.130,63 para 40 horas.
- A proporcionalidade para 20 horas resulta em R$ 2.565,315 antes do tratamento dos centavos.
- O anexo municipal não declara a jornada semanal; a amostra adota 20 horas e mostra um aviso.
- O modo `truncar` reproduz os 36 valores do anexo de Cafezal do Sul. O modo `arredondar` expõe a diferença de centavos.
- A fórmula de defasagem usada é `referência / valor atual - 1`.
- Toda conclusão jurídica ou autorização de reajuste permanece humana.

Veja `docs/16_regras_salariais_v0.5.md` para os cálculos e pendências.

## Organização

```text
assets/        Fontes incorporadas ao relatório PDF
data/          Dados públicos brutos e amostras tratadas
docs/          Documentação e evidências geradas
referencias/   Materiais originais recebidos
src/           Coleta, extração, cálculos, serviços e exportações
static/        CSS e JavaScript
templates/     HTML da interface
tests/         Testes automatizados de cálculo, importação, API e exportação
```

## Regra principal

O sistema implementa somente regras confirmadas nos materiais recebidos ou informadas como parâmetro. Qualquer premissa não declarada na fonte aparece como aviso e deve ser validada pelo responsável.
