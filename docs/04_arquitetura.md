# Arquitetura da v0.6.1

## Estado

A arquitetura abaixo existe no código. Os módulos financeiro e salarial compartilham apenas a interface e as exportações; as regras permanecem separadas e testáveis.

## Fluxo

```text
Interface / API
├── financeiro → serviço → coleta TCE → extração → cálculos → JSON/Excel
└── salarial
    ├── catálogo → aquisição → documentos brutos + manifesto
    └── amostra ou documento selecionado → normalização → referência → JSON/Excel/PDF
```

## Componentes

| Caminho | Responsabilidade |
|---|---|
| `src/coleta/` | Sessão ASP.NET, opções do portal e download dos CSVs |
| `src/extracao/` | Conversão de números e extração por rótulos |
| `src/calculos/` | Percentuais, variações, pontos percentuais e classificação |
| `src/modelos/` | Estruturas anuais, históricas, FUNDEB, erros e resumos |
| `src/services/` | Orquestração sequencial, tolerância a falhas e consolidação |
| `src/persistencia/` | Armazenamento local dos CSVs públicos brutos |
| `src/persistencia/dossie_salarial.py` | Originais salariais, nomes seguros e manifesto auditável |
| `src/exportacao/excel.py` | Excel anual, histórico e painel financeiro |
| `src/exportacao/excel_salarial.py` | Excel salarial com parâmetros e fórmulas auditáveis |
| `src/exportacao/relatorio_pdf.py` | Relatório salarial PDF com fontes incorporadas |
| `src/salarial/analise_service.py` | PSPN proporcional, centavos, referência, diferenças e estrutura |
| `src/salarial/documento_service.py` | Extração de PDF, DOCX e DOC legado |
| `src/salarial/fontes_service.py` | Catálogo inicial de páginas municipais oficiais |
| `src/salarial/aquisicao_service.py` | Validação, inspeção e registro do dossiê antes da filtragem |
| `src/salarial/amostras.py` | Amostra preservada de Cafezal do Sul/2026 |
| `src/materiais/` | Inspeção da planilha original sem executar macros |
| `app.py` | API, uploads, validação e tratamento de erros |
| `templates/` e `static/` | Interface responsiva sem framework |

## Tecnologias adotadas

- Python, Flask, Requests, HTML, CSS e JavaScript puro.
- OpenPyXL para os arquivos Excel gerados pela aplicação.
- pypdf e python-docx para documentos com texto.
- ReportLab e fontes DejaVu incorporadas para o relatório PDF.
- LibreOffice opcional para converter o formato binário `.doc`.
- tzdata para disponibilizar `America/Sao_Paulo` também no Windows.

Pandas, banco de dados, React e FastAPI ainda não são necessários. OCR continua fora da v0.6.1: PDFs digitalizados recebem diagnóstico e devem ser convertidos antes da importação.

## Decisões de confiabilidade

- Relatórios 10, 20 e 15 são coletados em sequência porque o portal apresentou erro 500 com gerações simultâneas.
- A extração usa rótulos textuais, não números fixos de linha.
- Cada ano histórico é isolado: falhas são registradas e os demais anos continuam.
- Os dados brutos são preservados antes da interpretação.
- Documentos do dossiê são limitados a 15 MB cada; extensões e conteúdo são validados antes da gravação.
- URLs são metadados auditáveis; o servidor não busca automaticamente endereços arbitrários.
- A aquisição preserva DOC/XLS legados mesmo sem conversor, marcando-os para tratamento posterior.
- O tratamento dos centavos é parâmetro obrigatório no resultado, não comportamento oculto.
- O Excel salarial mantém entradas em aba própria e deriva a referência por fórmulas.
- O painel financeiro usa referências locais; o link externo quebrado do modelo recebido não foi reproduzido.
- Jornada não declarada gera aviso permanente no JSON, Excel, interface e PDF.

## Ordem preferida de integração

```text
API ou arquivo estruturado
→ requisição HTTP direta
→ parsing de HTML
→ automação de navegador
→ OCR, somente quando necessário
```
