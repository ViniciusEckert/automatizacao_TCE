# Interface e leitura — v0.8.3

## Revisão de usabilidade da tela simples (navegador real, desktop e celular)

| Ponto | Antes | Agora |
|---|---|---|
| Escolher entre 67 tabelas de Curitiba | Lista única com rótulos repetidos ("Curitiba · 40 h · curitiba.pdf, página 2, Anexo B1" aparecia duas vezes) | Lista agrupada por grupo, título distinto, porte e valor inicial; filtro por texto; descrição completa da tabela escolhida |
| Espera de 20 a 30 s | Só a mensagem "Lendo o documento…" | Barra, tempo decorrido e mensagens que mudam (15 s, 30 s, 2 min) |
| Segunda leitura do mesmo PDF | Repetia os 22 s | Menos de 1 s |
| Observações da leitura | Parágrafo único com termos técnicos | Lista curta (3 itens) e "Mais N observações" |
| Escolha da referência | Sem orientação | Texto de apoio: professores usam o piso nacional; outros cargos simulam reajuste ou informam valor |
| Abas no celular | Abaixo de 44 px de altura | 44 px |
| Campo de filtro | — | Com rótulo para leitor de tela |

Avaliação geral: o caminho principal ("escolher município, gerar Excel") é simples (um campo, um botão). O fluxo salarial com documento é o mais denso: arquivo, tabela, dados faltantes, referência, confirmação do recorte e conferência. Ele só aparece quando o usuário envia um documento; as tabelas preparadas seguem em um único campo.

## Teste de navegador real

```text
pip install -r requirements-dev.txt
playwright install chromium
python scripts/testar_navegador.py capturas/
```

Cobre: carga sem erro de console, ausência de rolagem horizontal, rótulos em todos os campos, alvos de 44 px, download do exemplo, erro do TCE em português claro, 5 tabelas de Londrina com rótulos distintos, 67 tabelas de Curitiba com filtro e grupos, segunda leitura rápida e geração do Excel a partir de uma tabela filtrada.

## Limites conhecidos
- A espera continua síncrona: a barra é indeterminada (não mostra porcentagem). Porcentagem real exigiria tarefa em segundo plano com consulta de status.
- O seletor de arquivo usa o texto do navegador (aparece em inglês em navegadores configurados em inglês).
- Consulta real ao TCE-PR e Windows real continuam sem teste.
