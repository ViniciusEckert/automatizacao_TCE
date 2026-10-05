# Correção Araucária — 0.8.4

A 0.8.3 devolvia zero candidatos para o PDF enviado pelo usuário, apesar do texto legível. Acrescentado adaptador para a matriz do magistério de Araucária: três blocos separados (classes de enquadramento I, II e III), referências A–T e níveis verticais. São 6, 5 e 6 níveis respectivamente: 340 valores preservados. Matrizes incompletas são rejeitadas; não se usa a leitura antiga como fallback após rejeição desse layout.

Município, magistério e ano extraídos do cabeçalho. Jornada não informada: preenchimento obrigatório pelo usuário com base no plano de carreira. O cargo preciso e enquadramento precisam de confirmação; nenhuma titulação foi inventada. O reajuste de 4,11% não foi tratado como progressão horizontal; os incrementos são inferidos dos valores e requerem revisão legal. Valores atuais preservados, inclusive diferenças de centavos. O documento declara elaboração DIEESE/ER-PR, fonte Prefeitura Municipal de Araucária e competência junho de 2026; sua origem e vigência não foram verificadas na web.

Cache da leitura atualizado para 0.8.4. Mesmas rotas e formatos. Testes novos verificam dimensões, quantidade, extremos, ausência de jornada e rejeição de linha incompleta. Verificação de geração usa jornada de 20 horas somente como cenário sintético de teste, sem afirmá-la como jornada oficial.
