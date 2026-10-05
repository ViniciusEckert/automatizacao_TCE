# Validação da automação 0.8.0

Data: 08/09/2026. Ambiente: Linux, Python e Node.js. O objetivo é conferir que a interface simplificada entrega o arquivo sem exigir as escolhas técnicas do fluxo anterior.

## Resultados

- **93 testes Python aprovados.** Incluem 13 novos testes de automação e as regressões de coleta, salários, importação, documentos e exportação.
- **Interação com DOM simulado aprovada.** O HTML renderizado pelo Flask e o JavaScript real foram executados com jsdom. Foram conferidos o pedido financeiro apenas com município/período, bloqueio enquanto processa, download automático, download repetido, falha recuperável, geração de uma tabela preparada, leitura ao selecionar arquivo, campos mínimos, seleção da preparação salva e confirmação de recortes ambíguos. Não houve erro JavaScript nesse fluxo. Respostas de rede e cliques de download foram simulados; não se trata de inspeção visual em navegador.
- **Consulta real completa aprovada.** A rota automática recebeu `1467` e `ultimo`, resolveu a prefeitura de Cruzeiro do Sul e entregou o Excel de 2025. A consulta levou 77,91 segundos, respondeu 200 e não retornou avisos. O arquivo foi reaberto pelo openpyxl. Evidências: `consulta_automatica_v0.8.0.json` e `v0.8/Cruzeiro_do_Sul_2025_Automatico.xlsx`.
- **Modelo salarial mantido.** As duas preparações geraram as quatro abas na ordem esperada. A comparação preservou os 36 vencimentos de Cafezal e os 184 de Curitiba, incluindo a última classe. Os testes anteriores de fórmulas, caches, arredondamento e truncamento permaneceram aprovados.
- **Reutilização aprovada.** Um CSV oficial preparado com cenário de 5% gerou referência inicial de R$ 2.289,46, foi salvo e pôde ser aberto por uma nova instância do aplicativo sem reenviar arquivo ou parâmetros. Original e hash foram mantidos.
- **Dados ausentes e ambiguidades tratados.** Matriz sem metadados pediu as informações ausentes; jornada completada continuou indicada como premissa. PDF com duas páginas não gerou comparação sem confirmar o recorte. PSPN para outra profissão e ano inválido foram recusados.
- **Abertura conferida por simulação.** O iniciador reservou uma porta do servidor, programou a abertura do endereço correspondente e fechou o servidor corretamente. O `.bat` foi revisado, mas não executado em Windows.

## Limites

A inspeção visual direta em navegador local está indisponível neste ambiente. A instalação por duplo clique precisa de conferência em um Windows real. A consulta TCE foi validada ao vivo para um município/ano nesta versão; isso não prova disponibilidade contínua de todas as publicações. As tabelas salariais de municípios ainda não preparados podem exigir documento, referência ou correção do recorte. A exportação mantém o modelo da versão 0.7; a interpretação final do professor permanece pendente.
