# Validação da comparação por profissão — MVP 0.7.0

Data: 07/09/2026.

## Resultado

- 68 testes automatizados aprovados, incluindo os 58 casos anteriores e 10 casos novos da comparação por profissão.
- Sintaxe dos dois arquivos JavaScript aprovada.
- Base `America/Sao_Paulo` carregada via `tzdata` com `PYTHONTZPATH` vazio, simulando ausência da base IANA no sistema.
- Comparação de todos os caches numéricos dos Excel entregues com o cálculo Decimal do servidor: 180 fórmulas em Cafezal e 922 em Curitiba, total de 1.102. Nenhuma divergência ou célula com erro Excel encontrada.
- Quatro abas em cada arquivo, na ordem prevista: Comparação salarial, Parâmetros, Dados originais, Fontes e premissas.

## Casos exercitados

- Cafezal/2026: 36 vencimentos municipais, três níveis e 12 classes, truncamento e jornada de 20 h declarada como premissa.
- Curitiba/2026: 184 vencimentos oficiais do Auxiliar Administrativo Operacional, quatro níveis e 46 classes. Verificados os extremos de R$ 2.180,44 e R$ 11.490,21 e a preservação de todas as classes no CSV e na exportação.
- Separação de cargos e jornadas no mesmo arquivo; rejeição de duplicatas e de matrizes incompletas.
- Extração de matriz HTML sem inventar ano, município ou jornada.
- Impedimento de aplicação automática do PSPN a outras profissões.
- Jornada de 44 h, proporcionalidade expressa e rejeição de ano incompatível e valores não finitos.
- Recalculo no servidor antes da exportação, mesmo se resultados anteriores enviados pelo navegador forem alterados.
- Fluxo HTTP de amostra, extração para revisão, análise e exportação Excel. O PDF legado rejeita comparações genéricas que não são de magistério/PSPN.

## Conferência visual e referência

As planilhas foram renderizadas e inspecionadas durante a criação: quatro abas, blocos iniciais e finais, rótulos, cores, alinhamento e alertas. A formatação condicional marca o vencimento inferior à base inicial de referência; a contagem abaixo da carreira correspondente aparece separadamente.

A referência visual é o relatório `Jornada (2).pdf`, páginas impressas 9–11. `Exemplo.xlsx` é somente o modelo fiscal. Mantiveram-se a sequência e as tabelas do relatório salarial, com adaptação da quantidade de classes. Não foi possível rever o vídeo original; o arquivo salarial original em XLSX não foi fornecido. Veja `docs/19_comparacao_profissoes_v0.7.md` para a correspondência detalhada e as decisões da equipe.

## Fontes e limites

A amostra de Curitiba usa o PDF oficial de 2026 preservado em `referencias/fontes_salariais_2026_09_07/curitiba.pdf`. Seu parâmetro de comparação é um cenário didático de +5% na base inicial, expressamente identificado; não é um piso ou reajuste aprovado.

A tabela histórica de Londrina encontrada é de 2025. Ponta Grossa requer mapeamento entre códigos, cargos e jornadas. Maringá retornou a estrutura da página dinâmica, sem o anexo necessário. O download do diário de Siqueira Campos retornou HTTP 403. Esses municípios não são apresentados como comparações completas validadas.

O navegador remoto bloqueou o servidor local com `ERR_BLOCKED_BY_CLIENT`. Por isso não foi possível validar visualmente os cliques na aplicação nesta sessão; os testes cobrem as rotas e a sintaxe dos scripts. A equipe deve executar o roteiro do README no seu navegador.

A revisão humana da fonte e dos parâmetros continua necessária. A planilha fica pronta para a conferência acadêmica; as regras escolhidas não são atribuídas ao professor.
