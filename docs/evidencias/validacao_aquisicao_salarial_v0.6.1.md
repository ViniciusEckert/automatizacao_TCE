# Validação da aquisição salarial — MVP 0.6.1

Data: 31/08/2026

## Resultado

- 58 de 58 testes automatizados aprovados.
- JavaScript validado sintaticamente com `node --check`.
- Módulos Python compilados sem erro.
- `requirements.txt` instalado em ambiente virtual limpo.
- `tzdata` instalado e `America/Sao_Paulo` carregado com deslocamento `-03:00`.
- Página inicial e novas rotas exercitadas pelos testes de integração Flask.

## Casos adicionados

1. catálogo possui seis fontes oficiais sem IDs duplicados;
2. endpoint não limita o módulo a Cafezal do Sul;
3. PDF sem texto é preservado e marcado como provável OCR;
4. DOCX textual fica pronto para triagem;
5. DOC legado é preservado sem exigir LibreOffice na aquisição;
6. dossiê salva original, manifesto, SHA-256 e itens ausentes;
7. dossiê sem tabela vigente é rejeitado;
8. rota de aquisição retorna manifesto e não executa a comparação.

## Separação confirmada

| Etapa | Faz na v0.6.1 | Não faz nesta etapa |
|---|---|---|
| Localização | orienta seis pontos oficiais e aceita outro município | não afirma que o primeiro arquivo esteja vigente |
| Aquisição | recebe tabela, plano e ato; preserva origem e hashes | não escolhe páginas/abas do magistério |
| Inspeção | detecta texto, provável OCR e conversão legada | não interpreta classe, nível ou salário |
| Comparação preservada | mantém o protótipo e a amostra Cafezal | não é acionada ao registrar o dossiê |

## Fontes verificadas

- [Cafezal do Sul — legislação](https://www.cafezaldosul.pr.gov.br/index.php?novo_cliente=12145&pagina=20&sessao=b054603368xsb0)
- [Curitiba — Gestão de Pessoal](https://www.transparencia.curitiba.pr.gov.br/conteudo/gestaodepessoal.aspx)
- [Londrina — PCCS do Magistério](https://portal.londrina.pr.gov.br/menu-oculto-recursos-humanos/legislacao-rh-portal-servidor/plano-de-cargos-carreiras-e-salarios-do-magisterio-publico-municipal-do-poder-executivo-do-municipio-de-londrina)
- [Maringá — Tabela Salarial](https://transparencia.maringa.pr.gov.br/portaltransparencia/1/publicacoes/4383)
- [Ponta Grossa — Estrutura Salarial](https://rh.pontagrossa.pr.gov.br/estatisticas/salarios)
- [Siqueira Campos — Estatuto do Magistério](https://siqueiracampos.pr.gov.br/pagina/37/educacao/sub-pagina/48/)

As páginas são pontos de partida. Vigência, jornada e ato legal ainda devem ser conferidos em cada dossiê.
