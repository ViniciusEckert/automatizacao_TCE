# DESIGN.md — Análise Municipal (interface atual, v0.8)

Extraído de `static/css/simples.css` e `templates/inicio.html`. Use como ponto de partida; mudanças de identidade visual devem ser decisão da equipe.

## Propósito e público
Ferramenta técnica e institucional para **analista de finanças/RH público**. Prioridades: clareza, confiança, poucos passos ("escolher e baixar o Excel"). Tom: sóbrio, em português do Brasil, frases curtas.

## Cores (tokens)
| Token | Valor | Uso |
|---|---|---|
| `--verde` | `#195a45` | ação principal, links, estado selecionado |
| `--escuro` | `#153b31` | hover do botão principal |
| `--papel` | `#f5f3ee` | fundo da página |
| `--linha` | `#dddcd4` | bordas e divisórias |
| `--texto` | `#1d3930` | texto principal |
| `--suave` | `#617269` | texto de apoio, notas |
| `--lima` | `#d0e09e` | destaque de referência (barra lateral) |
| erro | `#8f442d` | mensagens de erro |
| aviso | `#fff4de` | confirmações/premissas |
| resultado | `#f0f6e6` / borda `#c8d9bb` | caixa de resultado pronto |

No Excel/PDF salarial a paleta é outra e **vem do modelo do professor**: atual = verde, referência = roxo, não conformidade = vermelho/rosa. Não misture.

## Tipografia
- Títulos (`h1`, `h2`): Georgia, serif, peso normal; `h1` com `clamp(38px, 7vw, 56px)` e espaçamento negativo leve.
- Corpo, rótulos, botões: Arial/Helvetica 16 px; notas 12–14 px; linha 1,6.
- Comprimento de linha confortável (< 80 caracteres); coluna principal de ~690 px.

## Layout e componentes
- Coluna única centralizada (`main`: `min(690px, 100% - 32px)`), cabeçalho com marca "AM".
- Abas em "pílula" (`role=tablist`), cartão branco (`.cartao`, raio 22 px, borda `--linha`, sombra muito suave).
- Campos: altura mín. 48 px, raio 9 px; rótulos 14 px negrito.
- Botão principal verde, largura total, estado ocupado com *spinner* (`data-ocupado`).
- Caixa de resultado, `details/summary` para observações, tabela com rolagem interna (`.rolagem`).
- Responsivo: abaixo de 580 px, uma coluna e menos padding.

## Princípios
1. Uma ação por tela; o caminho comum não exige entender etapas internas.
2. Premissas e avisos sempre visíveis; exemplo offline sempre identificado.
3. Erro diz o que houve e o que fazer.
4. Acessibilidade como piso: foco visível, `aria-live`, `prefers-reduced-motion`, contraste AA.
5. Sem decoração que não sirva à leitura; evitar cartões idênticos em excesso, gradientes e animações de entrada.

## Evolução sugerida
Unificar `inicio.html` e `index.html` (`/avancado`) sobre os mesmos tokens e componentes; extrair tokens para um único `tokens.css`.
