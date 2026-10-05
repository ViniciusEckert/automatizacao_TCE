# Validação de entidades e estabilidade local — v0.7.2

Data da revisão: 08/09/2026 (UTC).

## Evidência recebida e diagnóstico

O log do usuário registra sucesso na página, nos arquivos estáticos e em parte dos catálogos. O traceback NotFound termina em `GET /favicon.ico` com status 500: o ícone não existia e o tratamento antigo convertia o 404 em 500.

Também há falhas 502 em consultas fiscais e um reinício do watchdog após um evento em `encodings/utf_8_sig.py`. O log não demonstra a causa desse evento no arquivo do Python; confirma que o reloader reiniciou a aplicação.

A investigação do catálogo oficial identificou:

| Município/entidade | Resultado observado |
|---|---|
| Apucarana, 284 / 14731 — Autarquia dos Serviços Funerários | Seletor de relatórios presente, com a opção vazia "Nenhum relatório encontrado" |
| Cruzeiro do Sul, 1467 / 9777 — Câmara Municipal | Oferece relatórios 20, 25, 52, 31 e 26; não oferece RCL, código 10 |
| Cruzeiro do Sul, 1467 / 12266 — Município | Entidade municipal disponível; exercícios fechados 2019–2025 retornados na verificação |

Na consulta antiga à autarquia, abertura da página e seleções de tipo, município e entidade retornaram 200. O postback que solicitava o relatório de pessoal retornou 500. O cliente não verificava se esse relatório estava no catálogo.

O código da interface preferia explicitamente a entidade municipal apenas em Curitiba. Nos demais municípios selecionava a primeira opção disponível. Essa combinação explica a seleção inicial de Câmara/autarquia e a tentativa de solicitar relatórios ausentes. O corpo do POST histórico original não foi fornecido; sua associação à Câmara é consistente com a última seleção exibida no log e com o comportamento da interface, não uma leitura direta do corpo enviado.

## Correções

1. A API prioriza Município/Prefeitura no catálogo, sem remover as outras entidades.
2. Os fluxos de anos, períodos e CSV validam o relatório no catálogo da entidade antes de enviar o postback.
3. Ausência confirmada de relatório retorna 422 com orientação. Resposta sem o catálogo esperado continua sendo falha de consulta/leitura, evitando interpretar uma página inesperada como prova de indisponibilidade.
4. O histórico não repete os demais anos quando um relatório obrigatório está ausente do catálogo da entidade.
5. Quando todos os anos falham por outros motivos, a mensagem preserva a causa por exercício.
6. Logs de consulta/coleta incluem método, caminho e motivo.
7. O favicon responde 200. A execução por `python app.py` usa `debug=False, use_reloader=False`.

## Validação

- 80 testes automatizados aprovados, incluindo os 72 anteriores e oito casos novos.
- Verificados bloqueio de relatório ausente, continuação quando disponível, resposta inesperada sem catálogo, prioridade da prefeitura com preservação das demais entidades, resposta 422, interrupção do histórico incompatível, causas por ano e diagnóstico de 502.
- Verificação direta: `/favicon.ico`, `/static/favicon.svg` e `/` retornaram 200.
- Execução do ponto de entrada com chamada de servidor interceptada confirmou debug e reloader desativados.
- Teste real: `/api/entidades/1467` retornou primeiro `12266 — MUNICÍPIO DE CRUZEIRO DO SUL`.
- Teste real: consulta de anos da autarquia retornou 422 com orientação, sem enviar o postback inválido do relatório.
- Teste real: consulta de anos do Município retornou 2019–2025.
- Teste real: análise anual de Cruzeiro do Sul/2025, entidade 12266, com RCL e pessoal, retornou 200. FUNDEB foi desativado nesse teste para delimitar a verificação aos dois relatórios obrigatórios.

## Limites

Não foi refeita a consulta de todos os municípios nem todo o histórico de 2019–2025 nesta correção. Os testes reais comprovam os caminhos descritos acima. Outras indisponibilidades ou mudanças no portal podem ocorrer; agora suas causas ficam mais claras. A mudança não altera fórmulas ou o layout do Excel.

Fontes: [portal SIM-AM/TCE-PR](https://simam.tce.pr.gov.br/Paginas/Rel_LRF.aspx?relTipo=1), [Werkzeug — reloader](https://werkzeug.palletsprojects.com/en/stable/serving/#reloader).
