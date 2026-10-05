# Guia do código-base v0.6.1

## Finalidade

Esta versão é uma implementação de referência para executar, testar e reescrever em etapas. Ela não deve virar um bloco que ninguém da equipe entende.

## Ordem recomendada de estudo

### 1. Conversão e cálculos

- `src/extracao/relatorios.py`: `numero_brasileiro()`.
- `src/calculos/indicadores.py`: comprometimento, variação e classificação.
- Aprendizado: funções puras, entrada, retorno, exceções e testes.

### 2. Extração por rótulo

- `extrair_rcl_rreo()`, `extrair_resumo_pessoal()` e `extrair_resumo_fundeb()`.
- Compare o FUNDEB de 2019/2020 com 2021/2025.
- Aprendizado: não depender da posição fixa de uma linha.

### 3. Modelos

- `src/modelos/analise.py`.
- Aprendizado: `dataclass`, análise anual, FUNDEB, evolução, erros e histórico.

### 4. Serviço

- `src/services/analise_service.py`.
- Siga primeiro `analisar()` e depois `analisar_historico()`.
- Aprendizado: orquestração, relatório opcional, falha parcial e resumo.

### 5. Regras salariais

- `src/salarial/analise_service.py`.
- Compare `truncar` e `arredondar` na amostra Cafezal/2026.
- Aprendizado: `Decimal`, validação, tabela de referência e premissas explícitas.

### 6. Importação de documentos

- `src/salarial/documento_service.py`.
- Aprendizado: PDF, DOCX, conversão de DOC legado, regex e falhas seguras.

### 7. Persistência e exportações

- `src/persistencia/arquivos.py`, `src/exportacao/excel.py`, `excel_salarial.py` e `relatorio_pdf.py`.
- Aprendizado: bruto versus tratado, fórmulas auditáveis, gráfico e PDF.

### 8. Cliente TCE

- `src/coleta/tce_client.py`.
- Esta é a parte mais avançada: sessão, ASP.NET, `VIEWSTATE`, postback, cookies, retry e CSV.

### 9. API e rotas

- `app.py`, `src/salarial/pdf_service.py` e `src/materiais/planilha_service.py`.
- Aprendizado: JSON, upload, limites, códigos HTTP, download e injeção de serviço nos testes.

### 10. Interface

- `templates/index.html`, `static/css/style.css`, `static/js/app.js`.
- Aprendizado: formulários, `fetch`, anual/histórico, tabelas salariais, SVG, erro e download.

### 11. Testes

- Comece pelo arquivo ligado ao componente estudado.
- Altere um valor de propósito, veja o teste falhar, desfaça a alteração e execute novamente.

## Exercício de reescrita

1. Executar a aplicação e os 58 testes.
2. Escolher uma função pequena da própria frente.
3. Explicar sua entrada, saída e erros.
4. Criar uma branch e reescrever sem copiar linha por linha.
5. Manter ou melhorar os testes.
6. Comparar com a amostra histórica.
7. Abrir PR descrevendo o que foi aprendido.

## Partes prontas para estudar

- anual e histórico 2019–2025;
- RCL, Pessoal e FUNDEB;
- evolução, resumo e falha parcial;
- persistência bruta, interface, Excel e amostra;
- painel financeiro e extração opcional de MDE;
- importação salarial, comparação, Excel e PDF.

## Partes que dependem de informação externa

- OCR para documentos somente imagem;
- estruturas salariais muito diferentes da amostra;
- confirmação de jornada, centavos e fórmula de defasagem;
- interpretação das inconsistências do PDF-modelo;
- validação em outros municípios.

Banco de dados, autenticação e frameworks front-end não são tarefas atuais. Só devem entrar se um requisito concreto justificar a complexidade.
