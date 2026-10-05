## O que muda
<!-- Uma frase: o comportamento novo ou corrigido -->

## Por quê
<!-- Decisão (DEC-xxx), requisito ou bug que motiva -->

## Evidência
- [ ] Valores conferidos no bruto / fonte: <!-- município, ano, relatório, arquivo -->
- [ ] Testes adicionados ou atualizados; suíte completa passou (`python -m unittest discover -s tests -v`)
- [ ] Nenhum dado inventado; premissas aparecem como parâmetro/aviso

## Checklist
- [ ] Cálculo está em `src/`, não na rota nem no JS
- [ ] Bruto não foi alterado; falha de um ano não apaga os demais
- [ ] Excel/PDF mostram parâmetros e avisos (se tocou exportação)
- [ ] Sem dado sigiloso/pessoal no Git; uploads validados (se tocou entrada de arquivos)
- [ ] Docs, dicionário de dados e CHANGELOG atualizados
- [ ] Revisão cruzada solicitada (coleta: outro back; interface: outro front)

## Não verificado
<!-- Ex.: Windows real, navegador real, município X -->
