# Front-end — HTML, CSS e JavaScript puro

## Conteúdo
- Estado atual
- Regras
- Padrões de código do projeto
- Identidade visual atual
- Linguagem e microcopy
- Acessibilidade e responsividade
- Como testar
- Direção de design (para a IA)

## Estado atual

Duas interfaces coexistem: **`templates/inicio.html` + `static/js/simples.js` + `static/css/simples.css`** (tela simples v0.8: escolher e baixar o Excel) e **`templates/index.html` + `static/js/app.js` (764 linhas) + `salarios_editor.js` + `static/css/style.css`** (tela detalhada em `/avancado`). Sem framework, sem bundler, sem Node em produção (DEC-008: Flask + JS puro; React não é obrigatório, DEC-030).

## Regras

1. **O front não calcula** RCL, FUNDEB, defasagem, PSPN nem classificação. Pede ao back e mostra.
2. **Nunca `innerHTML` com dado vindo da API**; use `textContent`/`createElement` (o código atual já faz isso). Evita XSS vindo de nomes de município/documentos.
3. Toda ação assíncrona: estado ocupado (botão desabilitado + `aria-busy`), mensagem de status em região `aria-live`, e recuperação de falha (botão "Tentar novamente").
4. Erros da API: mostrar `dados.erro`; o contrato JSON está em `backend-flask.md`. Nunca mostrar traceback nem mensagem técnica crua.
5. Avisos e premissas devolvidos pelo back (jornada, modo de centavos, progressão inferida) **precisam ser visíveis**; nunca esconder `avisos[]`.
6. Exemplo offline (Curitiba, Cafezal) é **identificado como exemplo** na tela e não substitui resultado de consulta real.
7. Não introduzir dependência de CDN: o app roda local e pode estar sem internet (fora a consulta ao TCE).

## Padrões de código do projeto

```js
const el = id => document.getElementById(id);
async function api(url, opcoes = {}) {            // lança Error com status e dados.erro
  const resposta = await fetch(url, opcoes);
  const dados = await resposta.json().catch(() => ({}));
  if (!resposta.ok) { const e = new Error(dados.erro || 'Não foi possível concluir agora. Tente novamente.'); e.status = resposta.status; throw e; }
  return dados;
}
const enviar = (url, dados) => api(url, {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(dados)});
```

- `ocupar(area, bool)` desabilita todos os campos do formulário guardando o estado anterior em `dataset.desabilitadoAntes`.
- Download: Excel chega em `arquivo.conteudo_base64`; `baixar()` monta `Blob` + `<a download>` e revoga a URL depois.
- Normalização de busca de município: `normalize('NFD')` + remover diacríticos + minúsculas.
- Abas: `role="tablist"/"tab"/"tabpanel"` com `aria-selected` e `hidden`.

## Identidade visual atual (resumo; arquivo completo em `assets/DESIGN.md`)

Tokens em `simples.css`: `--verde:#195a45`, `--escuro:#153b31`, `--papel:#f5f3ee`, `--linha:#dddcd4`, `--texto:#1d3930`, `--suave:#617269`, `--lima:#d0e09e`. Títulos em Georgia (serif), corpo em Arial. Cartão branco com borda `--linha` e raio 22 px; botão principal verde, largura total. Erros em `#8f442d`; confirmações em `#fff4de`. Reutilize os tokens; **não** introduza paleta nova sem decisão da equipe.

## Linguagem e microcopy

- Português do Brasil, frases curtas, sentence case, verbos claros: "Gerar Excel", "Baixar Excel novamente", "Tentar novamente".
- Descreva o que acontece, não como o sistema funciona: "Ainda não encontramos os dados necessários para esse município".
- Erro = o que houve + o que fazer; sem pedir desculpas, sem jargão (evite "postback", "payload", "endpoint").
- Mantenha o mesmo nome para a mesma ação em todo o fluxo.
- Valores monetários e percentuais no formato brasileiro (`R$ 5.130,63`, `37,85%`), formatados por `Intl.NumberFormat('pt-BR')` ou texto vindo do back.

## Acessibilidade e responsividade (piso de qualidade)

Foco visível (`:focus-visible`, já definido), `<label for>` em todo campo, `aria-live="polite"` em mensagens/resultados, `prefers-reduced-motion` respeitado, contraste AA, alvos de toque >= 44 px, tabelas largas dentro de contêiner com `overflow:auto`, layout de 1 coluna abaixo de ~580 px. Teclado: toda ação alcançável por Tab/Enter.

## Como testar

`scripts/testar_interface.cjs` roda a interface em **jsdom** com `fetch` e download simulados, usando respostas geradas pelas rotas reais (`scripts.preparar_qa_interface`). Cobre validação de campos, clique único, download automático, recuperação de falha e reuso da preparação. Ao mudar JS, atualize/estenda esse script. DOM simulado não substitui olhar a tela num navegador real.

## Direção de design (quando a tarefa pedir melhorar a aparência)

Combine com a skill `frontend-design`. Fluxo recomendado: (1) ler `assets/DESIGN.md`; (2) propor um plano curto (cor, tipografia, layout) coerente com um **sistema técnico e institucional para analista público** — legibilidade e confiança antes de ornamento; (3) mudar só o que o pedido exige; (4) evitar os "vícios de IA": cards idênticos com a mesma sombra, rótulos em caixa alta com espaçamento em todo título, gradientes decorativos, animações de entrada em tudo; (5) unificar as duas interfaces é meta de médio prazo — não crie uma terceira.
