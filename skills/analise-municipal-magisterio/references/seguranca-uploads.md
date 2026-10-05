# Segurança — uploads, arquivos e fonte externa

O sistema roda **localmente**, em `127.0.0.1`, e processa dados públicos. Mesmo assim recebe arquivos de terceiros (PDF, DOCX, DOC, XLSX, HTML, CSV) e consulta um portal externo. O modelo de ameaça é: documento malformado ou malicioso, caminho de arquivo manipulado, conteúdo inesperado indo para a tela, e dado sensível versionado por engano.

## Conteúdo
- Já implementado (manter)
- Regras para novo código
- Subprocessos (LibreOffice)
- Dados e privacidade
- Itens a considerar
- Checklist de PR

## Já implementado (não regredir)

- Limite total de upload 48 MB (413 tratado) e **15 MB por arquivo** no dossiê/PDF; extensões aceitas explícitas (`.pdf .docx .doc .xlsx .xls .csv .html .htm`).
- Nome de arquivo com `secure_filename`; segmentos de caminho sanitizados (`_segmento`: só `[a-zA-Z0-9_-]`) em `ArquivoBrutoStore` e `DossieSalarialStore`, rejeitando vazio.
- **Não baixa URL informada** (DEC-033): a URL é metadado; evita SSRF e conteúdo arbitrário.
- Originais preservados com **SHA-256** e manifesto (DEC-034).
- XLSX inspecionado **sem executar macros**, em cópia (R14).
- Servidor sem debug e sem reloader; bind em `127.0.0.1` com porta livre (`iniciar.py`).
- Erros 500 não vazam traceback ao cliente.
- Front usa `textContent`, não `innerHTML`, com dados externos.

## Regras para novo código

1. **Nunca confiar em nome, tipo MIME ou extensão** do upload: valide pelo conteúdo quando importar (abrir como PDF/DOCX falha de forma controlada).
2. Todo caminho no disco é construído por segmentos sanitizados; nunca concatenar texto do usuário em caminho. Verifique que o destino resolvido fica dentro do diretório base.
3. Gravação **atômica** (arquivo temporário + `os.replace`) para preparações e manifestos.
4. Limite de tamanho e de tempo em toda leitura de documento; documentos "bomba" (zip aninhado, PDF gigante) devem falhar com mensagem, não travar.
5. Sem `eval`, `exec`, `pickle.loads` de dado externo; JSON apenas.
6. Parsing de HTML com `HTMLParser`/biblioteca segura; não renderizar HTML recebido.
7. Registros de log sem dados pessoais desnecessários.
8. Dependências com versão limitada no `requirements.txt` e atualizadas por Dependabot.

## Subprocessos (LibreOffice / antiword)

- Chame com **lista de argumentos** (`subprocess.run([...], timeout=...)`), nunca `shell=True`, nunca montando comando com texto do usuário.
- Arquivo de entrada em diretório temporário com nome fixo gerado pelo sistema (não o nome enviado).
- Defina `timeout` e capture saída; trate ausência do binário com mensagem clara (R16).
- Descarte o temporário em `finally`.

## Dados e privacidade

- Apenas **dados públicos** e amostras autorizadas no repositório (R11). Não versionar `data/raw/*`, documentos sigilosos nem dados pessoais.
- `.gitignore` já exclui `.env*`, `data/raw/*`, `output/*`. Antes de commit, confira `git status`.
- Documentos enviados não são mandados a serviço externo de interpretação (afirmado no README); preserve essa garantia ao integrar qualquer IA/OCR.

## Itens a considerar (não implementados)

- Autenticação não é necessária enquanto o app for local e de usuário único (DEC-030); se for hospedado, passa a ser obrigatória, junto com HTTPS e CSRF.
- Verificação de assinatura/legitimidade do ZIP distribuído.
- Limite de requisições ao portal TCE (já sequencial; considerar espera entre consultas).

## Checklist de PR (segurança)

- [ ] Novo upload valida tamanho, extensão e conteúdo
- [ ] Caminhos por segmentos sanitizados; sem path traversal
- [ ] Sem `shell=True`; subprocesso com timeout
- [ ] Nenhum dado de usuário em `innerHTML`
- [ ] Nada sigiloso entrou no Git
- [ ] Mensagens de erro sem detalhes internos
