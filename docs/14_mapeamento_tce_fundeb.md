# Mapeamento TCE-PR e FUNDEB

## Fonte

Portal SIM-AM/TCE-PR: `https://simam.tce.pr.gov.br/Paginas/Rel_LRF.aspx?relTipo=1`

O portal utiliza ASP.NET Web Forms. A aplicação reproduz os postbacks, mantém cookies e baixa a exportação CSV oficial.

## Relatórios adotados

| ID | Relatório | Período usado | Campos principais |
|---:|---|---|---|
| 10 | RREO — Receita Corrente Líquida | Fechamento anual | RCL e controle de validação |
| 20 | RGF — Despesa com Pessoal | Fechamento anual | RCL ajustada, DTP, percentual e limites |
| 15 | RREO — Manutenção e Desenvolvimento do Ensino | 6º Bimestre, ID 32 | Receitas do FUNDEB e resultado líquido |

## Campos do formulário

| Conceito | Nome do campo ASP.NET |
|---|---|
| Município | `ctl00$ContentPlaceHolder1$ddlMunicipio` |
| Entidade | `ctl00$ContentPlaceHolder1$ddlEntidade` |
| Relatório | `ctl00$ContentPlaceHolder1$ddlRelatorio` |
| Ano | `ctl00$ContentPlaceHolder1$ddlAno` |
| Período | `ctl00$ContentPlaceHolder1$ddlPeriodo` |

## Mudança de layout do FUNDEB

- 2019–2020: rótulo observado `11- RECEITAS RECEBIDAS DO FUNDEB`.
- 2021–2025: rótulo observado `6 - RECEITAS RECEBIDAS DO FUNDEB`.
- A posição mudou, mas a expressão `RECEITAS RECEBIDAS DO FUNDEB` permaneceu.

Por isso a extração normaliza o texto e procura o rótulo. Não utiliza “linha 12” ou “linha 7” como regra.

## Compatibilidade observada

- O relatório MDE ofereceu exercícios de 2013 a 2026 durante o mapeamento.
- O período anual adotado para o FUNDEB foi o 6º bimestre.
- Curitiba/2019–2025 foi coletada sem falha nos três relatórios.
- Relatórios devem continuar sequenciais para evitar erro 500 do portal antigo.

## Como remapear

```powershell
python -m scripts.mapear_tce
```

Se um rótulo deixar de ser encontrado, preserve o CSV bruto, compare a estrutura, adicione uma variação explícita ao extrator e crie um teste antes de alterar a regra.
