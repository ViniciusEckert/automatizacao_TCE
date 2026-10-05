# Relatório de QA — Jornada Magistério (MVP v0.4)

- Data: 25/08/2026
- Responsável: Claude (QA exploratório, a pedido do usuário)
- Escopo pedido: (1) TCE com pelo menos 2 municípios além de Curitiba, comparando valores manualmente; (2) tabelas salariais de outros municípios, já que a estrutura de Cafezal do Sul pode não representar todas as prefeituras.
- Como foi feito: 31 testes automatizados existentes rodados (todos passam), leitura do código-fonte, e 6 testes exploratórios novos escritos e executados de fato contra `src/salarial/*` simulando estruturas de outros municípios. **A parte de TCE não pôde ser executada ao vivo** — ver bloqueio abaixo.

---

## 1. Teste do TCE com outros municípios — BLOQUEADO

**Situação: [x] Bloqueado**

Meu ambiente de execução não tem saída de rede liberada para `simam.tce.pr.gov.br` / `servicos.tce.pr.gov.br` (proxy de rede nega o domínio; e a busca web também recebe 503 do WAF do portal). Ou seja, eu não consegui, de fato, coletar dados reais de nenhum município — nem Curitiba, nem outro.

Isso já é, por si só, um achado relevante:

- **`scripts/testar_tce.py` só sabe testar Curitiba.** Os IDs `municipio_id="1490"` e `entidade_id="12268"` estão fixos no script (não há parâmetro de linha de comando). Para testar outro município hoje, alguém precisa chamar `TCEClient().listar_municipios()` manualmente, achar o ID, achar a entidade, e escrever um script à parte.
- **Toda a evidência de validação registrada no projeto é só de Curitiba.** `docs/evidencias/validacao_curitiba_2019.md` e `validacao_curitiba_2019_2025.md` — 21 relatórios, 7 anos, 0 falhas, mas **só Curitiba**. O próprio arquivo admite isso no rodapé: *"Esta validação comprova o comportamento observado para Curitiba (...). Não comprova automaticamente todos os municípios."*
- **`tests/test_extracao.py` usa apenas fixtures copiadas de relatórios de Curitiba** (os números batem exatamente com os de `validacao_curitiba_2019.md`). Não existe nenhum fixture de um município pequeno/médio.

### O que revisei no código (já que não pude rodar ao vivo)

`src/extracao/relatorios.py` é o módulo que interpreta o CSV do TCE. Ponto positivo: a extração é **por rótulo de texto** ("RECEITA CORRENTE LÍQUIDA - RCL", "DESPESA TOTAL COM PESSOAL", "RECEITAS RECEBIDAS DO FUNDEB"), não por posição de linha/coluna fixa — isso é o design certo, porque RGF/RREO são formatos padronizados pelo Tesouro Nacional (STN) e deveriam ter os mesmos rótulos em qualquer município do Paraná. Isso reduz bastante o risco de quebrar em outra prefeitura.

Ainda assim, há riscos reais que só um teste ao vivo revela:
- Municípios pequenos podem não publicar todas as linhas usadas (ex.: `LIMITE MÁXIMO`, `LIMITE PRUDENCIAL`) se algum período estiver sem dados — a função `_resumo_por_inicio` lança `TCEError` se não achar a linha, o que é o comportamento correto, mas nunca foi observado acontecendo de verdade.
- Entidades diferentes de "Prefeitura" (RPPS, consórcios, câmara) podem ter layout de RGF diferente.
- O relatório FUNDEB (`RELATORIO_MDE`) pode não existir para anos anteriores a 2019 (antes do FUNDEB substituir o FUNDEF) — o código já trata isso com try/except, mas não foi validado em município nenhum além de Curitiba.

### O que peço que você rode (com sua rede liberada)

```powershell
python -m scripts.mapear_tce --ano 2024
```
e, para dois municípios pequenos/médios do Paraná (sugestão: um bem pequeno tipo Cafezal do Sul, já que vocês têm dados salariais de lá, e um médio tipo Foz do Iguaçu ou Londrina):

```python
from src.coleta.tce_client import TCEClient
c = TCEClient()
municipios = c.listar_municipios()
# procure o município na lista, pegue o id, depois:
entidades = c.listar_entidades(municipio_id="<ID_ENCONTRADO>")
```

Depois rode `AnaliseService().analisar(...)` com esses IDs (como em `scripts/testar_tce.py`) e compare manualmente 2–3 valores (RCL, despesa com pessoal, % oficial) com o RGF publicado no site do próprio município ou no portal público do TCE, para confirmar que bate.

**Recomendação de bug/melhoria:** transformar `scripts/testar_tce.py` em um script parametrizável (`--municipio`, `--entidade`, `--ano`) para que esse teste possa ser repetido facilmente para qualquer prefeitura, não só Curitiba.

---

## 2. Tabelas salariais de outros municípios — REPROVADO (bugs confirmados)

**Situação: [ ] Aprovado / [x] Reprovado**

Esta parte eu consegui testar de verdade, rodando `src/salarial/documento_service.py` e `src/salarial/analise_service.py` com estruturas de tabela plausíveis de *outras* prefeituras. Confirmo a suspeita do usuário: **o sistema está fortemente amarrado ao formato específico do anexo de Cafezal do Sul**, tanto no importador de documentos quanto no comparador.

### Bug 1 (crítico, silencioso) — níveis em algarismo romano perdem dados sem aviso

Entrada (comum no PR: "Nível I", "Nível II", "Nível III"):
```
Nível I - Ensino Médio Magistério   2.400,00 2.448,00 2.496,96
Nível II - Licenciatura Curta       2.640,00 2.692,80 2.746,66
Nível III - Licenciatura Plena      3.000,00 3.060,00 3.121,20
```
Resultado obtido: o importador retornou **sucesso**, mas só reconheceu o **Nível I**. Níveis II e III desapareceram silenciosamente, sem nenhum erro ou aviso — em vez de um erro, o sistema entrega uma tabela incompleta como se fosse a tabela completa.

Causa: o regex `PADRAO_NIVEL = r"N[ií]vel\s+([A-Z])\s*-\s*"` só captura **uma letra** depois de "Nível". "I" (isolado) passa despercebido como válido; "II" e "III" não batem com o padrão e a linha inteira é ignorada.

Isso é o bug mais grave que encontrei: numeração romana com mais de um algarismo é extremamente comum em planos de carreira do magistério no Paraná, e o usuário não teria como perceber que perdeu níveis, porque a ferramenta não avisa nada.

### Bug 2 — códigos numéricos de nível ("Nível 01", "Nível 02") quebram totalmente

```
Nível 01 - Professor        2400,00 2448,00
Nível 02 - Professor Pleno  2600,00 2652,00
```
Resultado obtido: `ValueError: Nenhuma linha salarial com níveis e valores foi reconhecida.` — falha completa, mesmo o texto sendo perfeitamente estruturado.

### Bug 3 — a frase de progressão precisa ser exatamente "Percentual entre classes = X%"

Testei com uma redação equivalente, só que com outra palavra ("interstício"):
```
Interstício de 5% entre classes.
Nível B corresponde ao Nível A acrescido de 10%.
```
Resultado: `ValueError: O percentual de progressão entre classes não foi reconhecido.` — falha total, mesmo a lei sendo perfeitamente compreensível para um humano. Note a inconsistência: para o acréscimo *vertical* entre níveis, o código já tem um plano B (infere matematicamente e avisa o usuário); para a progressão *horizontal* entre classes, não existe plano B — é tudo ou nada.

### Bug 4 — falso positivo de "inconsistência" quando a progressão real não é uniforme

Muitas leis municipais usam interstícios diferentes por faixa (ex.: 5% nas primeiras classes, 10% nas últimas) — isso é legal e comum, não é erro. Testei uma tabela assim, mecanicamente correta:

- Progressão real declarada na lei: 5%, 5%, 10%, 10%
- O sistema assume **um único percentual** para a tabela inteira (`progressao_classes_percentual`) e comparou cada classe com esse valor único.
- Resultado: **2 "divergências de estrutura" reportadas**, sugerindo erro na tabela municipal — quando na verdade o erro é do modelo do comparador, que não suporta progressão não uniforme.

Isso é sério porque o relatório final ("avisos") e o Excel/PDF gerados apresentariam essas "divergências de estrutura" como se fossem um problema real na lei do município, quando é só uma limitação do comparador.

### Bug 5 — acréscimo vertical fixo em R$ (não percentual) não tem como ser representado

Alguns planos antigos definem o próximo nível como "nível anterior + R$ 300,00 fixos", não como percentual. Como o campo `acrescimo_percentual` só aceita percentual, não há como o analista representar corretamente essa regra — ao forçar `acrescimo_percentual: 0`, o sistema aponta uma "divergência de estrutura" de R$ 300,00 em toda a coluna, mascarando o fato de que a estrutura é só diferente do modelo assumido, não errada.

### Evidência / como reproduzir

Rodei estes 6 cenários com um script Python chamando diretamente `extrair_tabela_salarial_texto` e `analisar_tabela_salarial` (as mesmas funções usadas pela aplicação). Posso reenviar o script (`teste_outros_municipios.py`) se quiser rodar de novo ou adicionar ao `tests/`.

| Cenário | Resultado |
|---|---|
| Nível I/II/III (romano) | ⚠️ "sucesso" mas perde 2 de 3 níveis silenciosamente |
| Nível 01/02 (numérico) | ❌ Falha total, nenhuma linha reconhecida |
| "Interstício de X%" em vez de "Percentual entre classes = X%" | ❌ Falha total |
| Progressão não uniforme (5%,5%,10%,10%), tabela correta | ⚠️ 2 falsos "erros de estrutura" reportados |
| Acréscimo vertical fixo em R$, tabela correta | ⚠️ 1 falso "erro de estrutura" reportado |

### Por que isso confirma a preocupação do usuário

`docs/16_regras_salariais_v0.4.md` já é honesto sobre isso — o modo `truncar` diz explicitamente "Reproduz os 36 valores do anexo de Cafezal do Sul" e a docstring de `analisar_tabela_salarial` diz "reproduzindo a lógica observada no anexo de Cafezal do Sul". Ou seja, a equipe sabia que modelou em cima de um único município. O problema é que **nenhum teste automatizado (`tests/test_salarios.py`) usa outra estrutura** — todos os 5 testes desse arquivo usam a mesma amostra de Cafezal do Sul. Então nada detecta esses bugs hoje.

---

## Recomendações priorizadas

1. **(Alto) Corrigir o regex de código de nível** para aceitar romanos multi-caractere e números (`[A-Z]+|\d+`), e — mais importante — **fazer o importador avisar/falhar quando uma linha com "Nível" não for reconhecida**, em vez de descartar silenciosamente. Perda silenciosa de dados é o pior tipo de bug aqui.
2. **(Alto) Rodar o teste real de TCE em pelo menos 2 municípios** fora de Curitiba (peço que você rode com sua rede, já que meu sandbox não acessa o domínio) e registrar a evidência como já foi feito para Curitiba.
3. **(Médio) Permitir progressão não uniforme** entre classes (lista de percentuais em vez de um número único), ou pelo menos deixar claro no relatório que "inconsistências de estrutura" pressupõem progressão uniforme declarada pelo usuário — hoje o aviso não deixa isso claro.
4. **(Médio) Suportar acréscimo vertical em valor fixo (R$)**, não só percentual.
5. **(Baixo) Parametrizar `scripts/testar_tce.py`** para aceitar `--municipio-id` e `--entidade-id`, facilitando testar qualquer prefeitura.
