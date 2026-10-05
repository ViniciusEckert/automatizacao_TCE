# Leitor geral de tabelas salariais — v0.9.0

## Resultado

A importação agora reconhece estruturas de tabela, sem exigir uma regra nova para cada município. Mantém os cálculos, as rotas, os perfis existentes e a organização do Excel do projeto. A leitura de Araucária passou para o motor geral; os adaptadores especializados existentes continuam como apoio a documentos complexos.

O fluxo é: selecionar documento, escolher uma tabela quando houver várias, completar apenas informações não identificadas, escolher a referência e gerar o Excel. Se a estrutura não for reconhecida, a revisão detalhada permite montar/corrigir a grade sem editar código. Isso exige transcrição manual nessa situação; não equivale a extração automática bem-sucedida.

## Formatos e estruturas

- PDF com texto e tabelas; PDF escaneado com OCR opcional.
- DOCX com tabelas; DOC antigo com conversor opcional.
- XLS e XLSX; CSV e TSV; tabelas HTML; JSON no contrato já existente do projeto.
- PNG, JPG e JPEG por OCR opcional.
- Matrizes com níveis nas linhas e classes nas colunas, matrizes transpostas, registros nível/classe/valor, listas de cargo/vencimento e vários blocos de uma mesma planilha.

O leitor usa aliases de cabeçalho, interpreta valores monetários e rejeita blocos incompletos ou ambíguos. Valores ausentes não são substituídos por zero. Nas listas com um vencimento por cargo, “Único” e “Inicial” são apenas rótulos de apresentação; não afirmam uma estrutura legal de carreira.

## Evidências de validação

155 testes passaram no ambiente Linux/Python 3.12, incluindo CSV/TSV, XLS/XLSX, DOCX, HTML, PDF textual, PDF em imagem com Tesseract e o DOC real enviado pelo professor. PNG/JPG têm suporte implementado, mas não receberam teste específico de arquivo nesta entrega.

Araucária: três blocos e 340 vencimentos reconhecidos pelo motor geral. As três exportações foram geradas pelas rotas reais da aplicação e recalculadas no LibreOffice: 651, 542 e 651 fórmulas, respectivamente, sem erros de célula ou caches ausentes. A referência de +5% e a jornada de 20 horas usadas nesse teste são cenários de teste, não afirmações jurídicas sobre o documento.

Curitiba: 68 candidatos; a leitura geral acrescentou a tabela da parte especial GM1 da página 48 que antes não era estruturada. Londrina e os demais formatos existentes continuam cobertos pelas regressões. A sintaxe JavaScript foi validada.

Fontes preservadas no pacote: documento salarial de Araucária recebido pelo usuário; PDF de Curitiba; PDF de Londrina; HTML de Ponta Grossa; Anexo A da LC 064/2026 de Cafezal recebido do professor; planilha e relatório de referência do professor. Essas fontes documentais não tornam todas as carreiras automaticamente validadas. Nenhum novo vídeo foi usado como evidência nesta implementação.

Não houve validação desta versão em Windows, Microsoft Excel, navegador real ou consulta ao vivo ao TCE. O módulo fiscal foi preservado; este trabalho não altera a disponibilidade externa do TCE nem torna os dados publicados instantâneos.

## Limitações reais

1. Não existe garantia de reconhecer qualquer documento arbitrário. Células mescladas, cabeçalhos incomuns, múltiplas colunas sem separação, tabelas giradas e paginação complexa podem exigir revisão ou transcrição. Blocos de páginas diferentes não são automaticamente unidos como uma única carreira.
2. OCR pode confundir dígitos e separadores. Resultados de OCR exigem conferência das células. Imagens borradas, baixa resolução e tabelas muito densas podem não funcionar. O leitor não usa uma IA externa para adivinhar valores.
3. OCR depende de Tesseract instalado e disponível no PATH. Usa português quando disponível, ou inglês como alternativa. Sem ele, o sistema informa a pendência; PDFs textuais e planilhas continuam funcionando. Instalar requirements.txt não instala Tesseract.
4. DOC antigo depende de LibreOffice ou da alternativa antiword. A conversão pode perder a grade; nesses casos será necessária revisão. DOCX com tabela nativa é preferível.
5. Município, cargo, vigência, jornada e referência salarial só podem ser preenchidos quando identificados. O documento pode não contê-los ou conter informações conflitantes. A seleção e a comparação não substituem a interpretação da legislação.
6. Nenhum piso universal é atribuído a todas as profissões. A referência precisa ser pertinente ao cargo e período; reajustes simulados permanecem identificados como simulação.
7. Fórmulas de planilhas sem valor calculado em cache não são avaliadas pelo importador. Recalcule/salve no Excel ou LibreOffice antes de importar. Arquivos protegidos/corrompidos e formatos não listados podem precisar de conversão.
8. Limites de processamento incluem arquivo de 16 MB, PDF de até 300 páginas, OCR de até 10 páginas por leitura e imagem de até 20 milhões de pixels. Há limites e tempos de espera adicionais para conversores e grades. Arquivos muito grandes precisam ser separados.
9. A aquisição automática de todas as tabelas municipais não foi implementada. Upload e preparações salvas continuam sendo o caminho deste módulo.

A entrega fecha um MVP de importação geral com revisão assistida. “Universal” descreve a abordagem por estruturas e formatos; não é uma promessa de acerto integral em qualquer arquivo.

## Uso

Extraia o ZIP e abra Iniciar.bat no Windows. Alternativamente, na pasta do projeto:

```bash
python -m pip install -r requirements.txt
python app.py
```

Abra http://127.0.0.1:5000. Para atualizar, preserve separadamente suas preparações e dados locais; o pacote não inclui dados enviados durante os testes.
