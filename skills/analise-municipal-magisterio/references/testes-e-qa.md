# Testes e QA

## Conteúdo
- Como rodar
- Princípios
- O que cobrir por módulo
- Evidências
- Rumo sugerido (pytest/CI)

## Como rodar

```powershell
python -m unittest discover -s tests -v
```

93 testes na v0.8.0. Os testes Python **não acessam a internet**; use dublês do `TCEClient`. A consulta real fica registrada à parte (`docs/evidencias/consulta_automatica_v0.8.0.json`).

Interface (opcional, requer Node + `jsdom`):

```text
python -m scripts.preparar_qa_interface respostas.json
node scripts/testar_interface.cjs respostas.json
```

DOM simulado não substitui inspeção visual; o `.bat` ainda não foi executado em Windows real.

## Princípios

- Valor numérico testado deve ter **origem conferida no bruto** (recalcular DTP / RCL ajustada à mão).
- Todo bug corrigido ganha teste de regressão com o caso que o gerou.
- Teste adversarial é parte normal da suíte: documentos malformados, notas, revogações, regras duplicadas.
- Não inventar dados de teste que pareçam oficiais; fixture sintética deve ser identificada como tal.
- Excel: gerar de verdade e **recalcular com LibreOffice**, comparando com o valor do Python.

## O que cobrir por módulo

**Financeiro**: percentual (e RCL ajustada <= 0), classificação nas fronteiras exatas dos limites, variação com base zero/`None`, rótulo FUNDEB nas duas variações de layout, histórico com um ano falho (os demais sobrevivem), FUNDEB indisponível (aviso, não erro), catálogo indisponível (bloqueio, sem fallback), ausência de relatório (422).

**Salarial**: truncar x arredondar nos 36 valores de Cafezal, progressão uniforme x por transição, regra vertical percentual x fixa, códigos A/II/01, falha segura em linha ilegível, nota com percentual, regras conflitantes (interrompe), tolerância de R$ 0,01, jornada diferente de 40 h, PDF sem texto (`requer_ocr`).

**HTTP**: 404/405 preservam status (não viram 500), upload grande (413), erros com método e caminho.

**Persistência**: gravação atômica das preparações, identificador derivado do conteúdo, sobrevivência à troca da pasta do ZIP.

## Evidências

Registrar em `docs/evidencias/validacao_*.md` o que foi conferido, contra qual bruto e qual resultado. Relatórios de QA formais ficam em `referencias/qa/`.

## Rumo sugerido (se a equipe quiser evoluir)

- Migrar de `unittest` para `pytest` (fixtures, parametrização) mantendo os testes existentes rodando.
- Conjunto de referência: leis de vários municípios + tabela conferida à mão, executado em todo commit.
- GitHub Actions rodando a suíte a cada PR; Dependabot; template de PR com checklist de evidência da fonte.
