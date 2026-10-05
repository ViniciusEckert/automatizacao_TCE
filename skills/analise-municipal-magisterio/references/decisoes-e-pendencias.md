# Decisões vigentes e pendências

Consulte antes de assumir qualquer regra. Fonte: `docs/09_decisoes.md`. Mudar uma decisão exige PR documentado.

## Conteúdo
- Arquitetura e processo
- Coleta e financeiro
- Salarial
- Escopo e interface
- Pendências (não assumir)

## Arquitetura e processo
- DEC-001 módulos financeiro e salarial no mesmo sistema.
- DEC-003 Python no back-end; DEC-008 Flask e JS puro no MVP (equipe iniciante).
- DEC-005 separar coleta, extração, cálculo, persistência e interface.
- DEC-004 não inventar fórmulas.
- DEC-035 `tzdata` como dependência (Windows).

## Coleta e financeiro
- DEC-009 CSV oficial em vez de automação de cliques.
- DEC-010 relatórios em sequência (paralelismo gera erro 500).
- DEC-011 relatório 15/MDE, período 32, para o FUNDEB.
- DEC-012 extrair por rótulo, não por linha.
- DEC-013 falha isolada por exercício; DEC-014 falha do FUNDEB é aviso.
- DEC-016 histórico limitado a 10 exercícios.
- DEC-022 não automatizar narrativa MDE/margem fiscal.
- DEC-026 scripts manuais do TCE parametrizados.

## Salarial
- DEC-015 inspetores de PDF/XLSX antes das regras.
- DEC-017 jornada, PSPN e centavos são parâmetros.
- DEC-018 truncar e arredondar disponíveis.
- DEC-019 primeiro nível é a base.
- DEC-020 DOC legado via LibreOffice opcional.
- DEC-023 nunca descartar linha salarial com valores silenciosamente.
- DEC-024 cada transição horizontal separada; DEC-025 regra vertical por tipo/valor/nível de referência.
- DEC-031 Cafezal é layout de saída, não esquema universal.
- DEC-032 dossiê antes da extração; DEC-033 não baixar URL automaticamente; DEC-034 originais com SHA-256 e manifesto.

## Escopo e interface
- DEC-021 não copiar link externo da planilha-modelo.
- DEC-027 Curitiba 2019–2025 é demonstração offline, não limite funcional.
- DEC-028 catálogo falhou → bloquear consulta ao vivo (sem fallback silencioso).
- DEC-029 modo anual carrega qualquer ano preservado de Curitiba.
- DEC-030 banco, ML, React, FastAPI não são obrigatórios sem necessidade validada.

## Pendências — NÃO assumir; tratar como parâmetro e avisar
1. OCR para documentos sem texto (só se amostras reais justificarem).
2. Jornada de Cafezal do Sul (20 h é premissa sinalizada) e regra oficial de centavos.
3. Fórmula de defasagem e denominador da margem fiscal.
4. Equivalência para carreiras que não partem do primeiro nível.
5. Persistência em banco e autenticação (só se o uso exigir).
6. Quatro dos seis dossiês-piloto municipais seguem sem validação completa; não declarar "seis dossiês completos".

## Hierarquia de fontes quando houver conflito
1. APS atualizada e arquivos do professor/consultoria.
2. `referencias/Contexto_Mestre_Original.md`.
3. Conversa do grupo (hipóteses).
4. Decisões técnicas e QA do desenvolvimento.
