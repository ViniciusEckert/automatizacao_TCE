# Validação da correção HTTP — v0.7.1

Data: 08/09/2026 (UTC).

## Problema confirmado

O handler `@app.errorhandler(Exception)` da versão 0.7.0 interceptava também `werkzeug.exceptions.NotFound`, imprimia "Erro inesperado" e devolvia status 500. Isso convertia uma URL não encontrada (404) em um aparente erro interno. O mesmo acontecia com outros erros HTTP sem handler específico, incluindo o método não permitido (405).

O traceback enviado não informa a URL solicitada. A origem específica da requisição no computador do usuário continua pendente da linha de acesso do terminal com método e caminho. Não se presume que tenha sido favicon, uma API específica ou um arquivo estático.

## Correção

Foi registrado um handler mais específico para `HTTPException`, preservando a resposta original, seu status e seus cabeçalhos. O corpo JSON informa código, método e caminho. O tratamento específico de uploads grandes continua ativo. Falhas internas reais continuam retornando 500 e gerando traceback, agora com o método e caminho no log.

A correção não cria URLs ausentes. Se uma ação da interface solicitar um caminho inexistente, é necessário identificar esse caminho para corrigir seu chamador ou verificar se há arquivos de versões diferentes em execução.

## Verificação

- 72 testes da suíte aprovados (68 existentes e quatro novos), em 2,882 segundos.
- URL de página, API inexistente e favicon retornam 404 sem log de erro interno.
- GET em uma rota exclusivamente POST retorna 405 e mantém o cabeçalho Allow.
- Upload acima do limite continua retornando 413 com a mensagem específica.
- Uma exceção interna real continua retornando 500, sem expor o detalhe na resposta, e aparece no log com o caminho correto.
- Revisado o diff de app.py: importação de HTTPException, novo handler e contexto adicional do log.

Referência técnica: [Flask — Generic Exception Handlers](https://flask.palletsprojects.com/en/stable/errorhandling/#generic-exception-handlers).

A atualização não modifica os cálculos financeiros, salariais ou o layout do Excel. Os relatórios de validação anteriores são preservados como histórico.
