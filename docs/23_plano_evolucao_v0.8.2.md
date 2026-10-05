# Plano de evolução v0.8.2

Base conferida: v0.8.1, 108 testes aprovados com pypdf 6.10.0. Três Excel de referência preservados pelas rotas Flask.

1. Priorizar fidelidade do painel ao Exemplo_Painel.xlsx, com fórmulas acumuladas e anuais, médias parametrizadas, limites oficiais, avisos e gráficos de barras.
2. Corrigir impressão salarial e generalizar PDF sem remover rotas ou campos existentes.
3. Avaliar extração por coordenadas dos PDFs reais, com revisão e fonte por página; manter erro claro nas páginas que não contêm tabela.
4. Preservar coletas versionadas sem retirar o caminho legado; não migrar formatos de perfis nesta entrega.
5. Testar regressão, contratos, recálculo e impressão; registrar mudanças e pontos não verificados.

## Perguntas agrupadas e padrões reversíveis

As perguntas completas estão no arquivo recebido 03_PERGUNTAS_AO_PROFESSOR.md. Não reenviar o e-mail já enviado.

- Cálculos: defasagem referência/atual-1, diferença atual-referência; arredondamento por etapa; jornada Cafezal permanece premissa. Padrões existentes preservados.
- Painel: média aritmética acumulada/número de exercícios como modelo, parametrizável por intervalos ou geométrica; RCL ajustada proveniente RGF explicitada; MDE sem interpretação automática; semestre não coletado.
- Fontes e apresentação: confirmar layout final e quantos municípios precisam de dossiê completo; vídeo não recuperado, sem requisito visual atribuído à gravação.
- Arquitetura: banco, API estruturada, lote e Next.js ficam apenas propostos; nenhuma implementação nesta versão.

As decisões já autorizadas pelo usuário permitem evoluir sem aguardar professor. Contratos e perfis antigos devem permanecer compatíveis. Um contorno não será anunciado como solução completa sem evidência.
