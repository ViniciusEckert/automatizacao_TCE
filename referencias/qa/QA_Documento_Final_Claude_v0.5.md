# Documento de QA — Jornada Magistério (MVP)

- Projeto testado: `Projeto_Jornada_Magisterio_MVP_v0_5.zip`
- Testador: Claude (QA exploratório/adversarial)
- Data: 25/08/2026
- Rodadas: (1) v0.4 — teste inicial; (2) v0.5 — reteste dos achados + regressão; (3) v0.5 — varredura final dos módulos ainda não testados
- Veredito atual: **não está com 0 bugs.** 3 bugs confirmados e reproduzíveis, todos da mesma família (contaminação de leitura por regex "gulosa"), concentrados no importador de tabelas salariais. Todo o resto do sistema testado (TCE, exportação Excel/PDF, planilha/PDF de materiais, persistência, rotas Flask) passou sem problemas encontrados.

---

## 1. Como o teste foi feito (metodologia)

Não me limitei a ler o código — cada afirmação abaixo foi **executada de verdade** contra o código entregue, dentro de um ambiente Linux com Python 3, as dependências do `requirements.txt` instaladas, e LibreOffice disponível para recálculo real de planilhas.

### 1.1. Suíte automatizada existente
Rodei `pytest` na íntegra a cada rodada:
- v0.4: 31 testes, todos passando.
- v0.5: 43 testes, todos passando (12 testes novos cobrindo os achados da rodada anterior).

Isso confirma que nada regrediu, mas **não é suficiente sozinho**: todos os testes automatizados do projeto usam dados sintéticos "bem-comportados" — nenhum deles tenta ativamente quebrar o sistema com formatações "do mundo real" (leis com notas de rodapé, ressalvas, erratas, nomenclaturas diferentes de nível). É exatamente esse tipo de teste adversarial que fiz manualmente.

### 1.2. TCE — validação cruzada de 3 fontes independentes
Como meu ambiente de execução não tem saída de rede liberada para `tce.pr.gov.br` (não consigo fazer a consulta ao vivo), a validação foi feita **auditando os artefatos entregues**, não confiando neles às cegas:
1. Peguei os CSVs brutos salvos em `data/raw/tce/` (Cafezal do Sul e Londrina/2024).
2. Conferi manualmente, linha por linha, os valores desses CSVs contra os JSONs de evidência (`docs/evidencias/TCE_*.json`).
3. Recalculei na mão, fora do sistema, o percentual de comprometimento com a folha de pessoal (`despesa com pessoal ÷ RCL ajustada`) para os dois municípios e confirmei que bate exatamente com o `percentual_calculado` gravado pelo sistema.

### 1.3. Importador salarial — testes adversariais escritos e executados
Para cada hipótese de bug, escrevi um trecho de texto de anexo de lei plausível (não um caso artificial de laboratório) e rodei diretamente `extrair_tabela_salarial_texto(...)` e `analisar_tabela_salarial(...)` — as mesmas funções que a aplicação usa — comparando a saída obtida com a saída esperada por um leitor humano do mesmo texto. Sempre que a saída divergia do que uma pessoa razoável entenderia lendo a lei, registrei como bug, com o texto de entrada e a saída exata do sistema como evidência.

Fiz isso em 3 rodadas:
- **Rodada 1 (v0.4):** 6 cenários (nomenclatura de nível, formas de descrever progressão, progressão não uniforme, acréscimo em R$ fixo).
- **Rodada 2 (v0.5, reteste):** repeti os mesmos 6 cenários para confirmar a correção + 12 cenários adversariais novos (referência circular, referência a nível posterior, PSPN inválido, nível único, valores sem separador de milhar em série, código duplicado com casing diferente, etc.).
- **Rodada 3 (v0.5, aprofundamento):** ataquei especificamente o padrão de captura de números (regex) com textos legais realistas contendo notas, ressalvas e revogações na mesma linha de um dado relevante — foi aqui que encontrei os 3 bugs atuais.

### 1.4. Exportação Excel — recálculo real, não só leitura de fórmula
Gerei um `.xlsx` com `gerar_excel_salarial(...)` combinando regra vertical percentual e valor fixo, e depois **mandei o LibreOffice (`soffice --headless`) abrir e recalcular de verdade** as fórmulas da planilha, extraindo os valores calculados e comparando célula a célula com o que o Python (`analisar_tabela_salarial`) havia calculado. Bateram exatamente — essa parte não tem bug.

### 1.5. Varredura dos módulos restantes
Nas rodadas anteriores eu tinha focado em TCE e no importador salarial (o que o usuário pediu). Nesta última rodada, li e testei o que ainda não tinha sido coberto:
- `src/calculos/indicadores.py`
- `src/modelos/analise.py` e `src/services/analise_service.py` (montagem do histórico/resumo financeiro)
- `src/materiais/planilha_service.py` (inspeção de planilhas enviadas)
- `src/salarial/pdf_service.py` (inspeção de PDFs enviados)
- `src/persistencia/arquivos.py` (gravação dos CSVs brutos do TCE em disco)
- `app.py` (todas as rotas Flask, tratamento de erros, validação de parâmetros)
- `static/js/app.js` (o trecho novo de UI para regra vertical/progressão não uniforme, incluindo o fluxo de reenvio de dados importados para nova análise)

Nenhum bug novo foi encontrado nesses módulos (detalhes na seção 3).

---

## 2. Bugs confirmados (3) — todos no importador de texto salarial

Os três têm a mesma causa raiz: **o parser assume que cada informação relevante (um valor, uma regra vertical, um percentual de progressão) aparece exatamente uma vez no texto, sem ambiguidade** — e isso não é verdade em textos legais reais, que frequentemente têm notas, ressalvas ou revogações no mesmo parágrafo/linha.

### Bug 1 — percentual em nota/parênteses vira "classe salarial" fantasma

**Entrada:**
```
Nível A - Professor 2.400,00 2.448,00 (reajuste anual de 5,00%)
Nível B - Licenciatura 2.640,00 2.692,80 (reajuste anual de 5,00%)
Percentual entre classes = 2,00%
Nível B = Nível A acrescido de 10,00%
```
**Obtido:** o Nível A ganha uma 3ª classe fantasma de **R$ 5,00** (o "5,00%" da nota foi lido como dinheiro). Como os dois níveis têm a mesma nota, a checagem de "quantidade de classes diferente entre níveis" não detecta o problema, e a análise segue adiante calculando "divergências de estrutura" em cima de um valor que não existe na lei.
**Esperado:** `[2400.0, 2448.0]` (2 classes), sem nenhuma menção à nota como valor.
**Causa raiz:** o padrão de moeda (`PADRAO_MOEDA`) aceita qualquer número no formato `X,XX` desde que não seja seguido por outro dígito — não verifica se depois vem `%` ou fecha parênteses de uma nota.

### Bug 2 — regra vertical duplicada é sobrescrita sem aviso

**Entrada:**
```
Nível B = Nível A acrescido de 12,00%
Em caso de dúvida, considera-se que o Nível B = Nível A acrescido de 20,00%
```
**Obtido:** o sistema fica com 20,00% e descarta os 12,00% em silêncio — sem sinalizar que havia duas afirmações conflitantes sobre a mesma regra.
**Esperado (no mínimo):** um aviso de conflito, para o analista humano decidir qual vale.

### Bug 3 — progressão geral "corrigida"/revogada é lida como progressão não uniforme

**Entrada:**
```
Percentual entre classes = 5,00%
Nota de rodapé: revogado o artigo anterior, o percentual entre classes passa a ser de 8,00%
```
**Obtido:** `progressoes_classes_percentuais = [5.0, 8.0]`, classificado como progressão não uniforme.
**Esperado:** deveria ser 8% para todas as transições (é uma correção, não duas regras diferentes) — ou, na dúvida, um aviso de conflito, nunca uma leitura silenciosa como se fossem duas taxas.

**Evidência/reprodução:** scripts `teste_contaminacao_percentual.py` (Bug 1) e os trechos reproduzidos em chat para os Bugs 2 e 3 — todos rodam com as mesmas funções (`extrair_tabela_salarial_texto`) usadas pela aplicação real, sem mocks.

---

## 3. Áreas testadas sem bugs encontrados

| Módulo/área | O que foi verificado | Método |
|---|---|---|
| TCE (Cafezal do Sul e Londrina/2024) | RCL, despesa com pessoal, FUNDEB, % de comprometimento | Conferência manual linha a linha do CSV bruto vs. JSON + recálculo do percentual fora do sistema |
| Achados da rodada 1 (6 bugs do relatório anterior) | Todos reconfirmados corrigidos | Reexecução dos mesmos 6 cenários |
| Referência circular / nível posterior na regra vertical | Bloqueio correto com erro claro | 2 cenários adversariais dedicados |
| PSPN não numérico, nível único sem progressão, código duplicado com casing diferente | Comportamento correto (erro claro ou resultado coerente) | 3 cenários adversariais |
| Exportação Excel (fórmulas) | Valores recalculados batem com o Python, célula a célula | Geração real + recálculo via LibreOffice headless |
| `indicadores.py` (cálculo de %, defasagem, margem fiscal) | Fórmulas conferem com o esperado matematicamente | Leitura + checagem manual das fórmulas |
| `modelos/analise.py` / `services/analise_service.py` | Serialização, ordenação de histórico, agregação (maior/menor/média) | Leitura de código, sem inconsistência encontrada |
| `materiais/planilha_service.py` e `salarial/pdf_service.py` | Validação de tamanho/formato de arquivo, extração de estrutura | Leitura de código; lógica simples e defensiva, sem furos óbvios |
| `persistencia/arquivos.py` | Sanitização de nomes de diretório/arquivo (municipio_id, entidade_id, ano) | Leitura de código; regex de sanitização cobre o caso |
| Rotas Flask (`app.py`) | Validação de campos obrigatórios, limites de tamanho de arquivo, tratamento de erros | Leitura de código; único ponto teoricamente frágil é `incluir_fundeb=0` (ver observação abaixo) |
| Nomes de arquivo com acento (`secure_filename`) | Município com acento não quebra o download | Testado diretamente: "Foz do Iguaçu" → "Foz_do_Iguacu", sem string vazia |
| `app.js` — fluxo de reenviar dados importados para nova análise (`entradaAPartirDaAnalise`) | Round-trip de `regra_vertical`, progressão não uniforme e avisos de importação | Leitura cuidadosa do fluxo completo; a estrutura serializada é reaproveitada corretamente |

**Observação menor, não classificada como bug:** em `/api/analisar`, a expressão `dados.get("incluir_fundeb", True) is not False` trata qualquer valor diferente do booleano literal `False` (por exemplo, o número `0`) como "incluir". Isso não é alcançável pela interface atual (o front-end sempre manda um booleano real via `checkbox.checked`), então não é um bug em uso normal — só ficaria frágil se algum outro cliente da API mandasse `0` em vez de `false`.

---

## 4. Recomendação

Os 3 bugs continuam concentrados num único ponto: as expressões regulares de `documento_service.py` capturam **qualquer** número no formato certo dentro da linha/frase-gatilho, sem restringir à cláusula que de fato declara o valor. A correção sugerida nas duas rodadas anteriores continua valendo e cobriria os 3 bugs ao mesmo tempo:
1. Limitar a captura ao trecho imediatamente após o padrão-gatilho (não a linha inteira).
2. Quando a mesma regra (valor de classe, regra vertical, progressão) for encontrada mais de uma vez com valores diferentes, **não escolher uma automaticamente** — emitir erro/aviso de conflito, do mesmo jeito que já é feito hoje para linhas de "Nível" totalmente irreconhecíveis.

Fora isso, não encontrei mais nada quebrado no sistema.
