# Persistência e banco de dados

## Conteúdo
- Situação atual
- Regras de persistência
- Quando adotar banco
- Modelo proposto (SQLite/SQLAlchemy)
- Caminho de migração

## Situação atual (decisão vigente: sem banco)

| O quê | Onde | Formato |
|---|---|---|
| CSV bruto do TCE | `data/raw/tce/<mun>/<ent>/<ano>/relatorio-<id>.csv` | texto |
| Dossiês salariais | `data/raw/salarios/<mun-uf>/<ano>/<dossie>/` + `manifesto.json` | originais + hashes |
| Amostras offline | `data/processed/*.json` (Curitiba 2019–2025, Cafezal 2026, Curitiba Administrativo 2026) | JSON versionado |
| Preparações salariais do usuário | `%LOCALAPPDATA%/AnaliseMunicipal/tabelas_salariais` (Windows) ou `~/.local/share/AnaliseMunicipal/tabelas_salariais` | JSON por identificador derivado do conteúdo, gravação atômica |

Banco, ML, React e FastAPI **não são obrigação do MVP** (DEC-030); persistência em banco e autenticação só "se o uso exigir" (pendência registrada).

## Regras de persistência (valem com ou sem banco)

1. **Bruto é imutável**; correção só na camada tratada.
2. Identificadores derivados do conteúdo/hash, não de nomes enviados.
3. Gravação atômica (temp + `os.replace`).
4. Dados do usuário fora da pasta do projeto, para sobreviver à troca do ZIP.
5. Amostras versionadas são públicas e autorizadas; listadas no `.gitignore` como exceção.
6. Toda estrutura persistida tem versão de esquema (`esquema_versao`) para migração futura.

## Quando adotar banco

Proponha banco **apenas** com sintoma concreto, por exemplo: precisar consultar séries de muitos municípios sem recoletar do portal; comparar versões de tabelas salariais ao longo do tempo; múltiplos usuários simultâneos; auditoria centralizada. Sem isso, arquivos bastam. Cite o sintoma no PR.

## Modelo proposto (se for adotado)

Para app local de um usuário, **SQLite com SQLAlchemy + Alembic** (arquivo único, sem servidor). PostgreSQL só se o sistema for hospedado.

```text
municipio(id_tce, nome, uf)
entidade(id_tce, municipio_id -> municipio, nome)
coleta(id, entidade_id, ano, relatorio_id, periodo, coletado_em, caminho_bruto, sha256)
indicador(id, coleta_id, codigo, valor_bruto, valor_tratado, unidade)        -- RCL, RCL_AJ, DTP, FUNDEB...
dossie(id, municipio_id, ano_ref, status, fonte_url, registrado_em)
documento(id, dossie_id, categoria, nome_original, sha256, requer_ocr, requer_conversao)
tabela_salarial(id, dossie_id, profissao, jornada, modo_centavos, origem_progressao, esquema_versao)
nivel(id, tabela_id, codigo, descricao, regra_tipo, regra_valor, nivel_ref)
vencimento(id, nivel_id, classe_idx, valor NUMERIC(14,2))
```

Valores monetários em `NUMERIC`/`Decimal`; guardar também `valor_bruto` (texto) para auditoria; chave única (`entidade_id, ano, relatorio_id, periodo`) para evitar duplicata.

## Caminho de migração

1. Introduzir uma interface (`RepositorioColetas`, `RepositorioTabelas`) com a implementação atual em arquivos.
2. Criar a implementação SQLite atrás da mesma interface; testes rodam nas duas.
3. Importar o que já existe (JSON/CSV) por script idempotente.
4. Manter os arquivos brutos em disco como evidência; o banco guarda ponteiro + hash.
5. Só então remover o caminho antigo, em PR separado e documentado em `docs/09_decisoes.md`.
