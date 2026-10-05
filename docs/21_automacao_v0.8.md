# Automação e decisões da versão 0.8.0

A orientação do usuário é minimizar o esforço de quem usa o sistema e manter o Excel no modelo exigido. A tela inicial agora termina uma ação completa, da escolha ao arquivo, sem exigir que o usuário opere as etapas internas.

## Financeiro

`POST /api/automacao/financeiro` recebe município e período. O servidor confirma o nome no catálogo oficial, localiza uma entidade Município/Prefeitura que ofereça RCL e Pessoal e consulta seus anos disponíveis. Nomes e entidades fornecidos pelo navegador não substituem essa resolução.

O modo `ultimo` analisa o último ano fechado publicado. `historico` usa o intervalo disponível, limitado a dez anos desde 2019. `intervalo` permite uma seleção explícita de anos. Lacunas são registradas, sem preencher números ou consultar anos ausentes do catálogo. FUNDEB permanece incluído; falhas nesse relatório seguem o aviso já existente do serviço.

Uma única resposta inclui o Excel e o resumo para a tela. O navegador solicita o download automaticamente e oferece um botão para baixar novamente. A demonstração é uma ação separada e identificada, sem substituir resultados de consulta real.

As consultas continuam sequenciais devido ao comportamento do portal TCE-PR. A automação reduz escolhas e cliques; ela não torna a fonte externa instantânea nem cria dados que a fonte não publicou.

## Salários

O caminho comum usa uma preparação com profissão, carreira, vencimentos, referência e premissas. O pedido contém somente o identificador dessa preparação. Cafezal e Curitiba Administrativo são exemplos incluídos; preparações adicionais são salvas após uma análise válida.

Ao escolher um documento novo, `/api/automacao/preparar-tabela` preserva o original, o hash e o resultado da extração. A tela mostra os candidatos e solicita apenas os metadados ausentes. A referência é informada quando o documento não a contém: cenário percentual, valor inicial fornecido ou PSPN conhecido para o magistério do ano preparado. O PSPN de 2026 não é estendido a outros anos ou profissões.

O valor do cenário percentual é aplicado à base inicial, e a tabela de referência é reconstruída com as regras da carreira. Ele não representa um ato de reajuste aprovado. Progressões inferidas e jornada presumida continuam sinalizadas. Informações complementadas pelo usuário não são rotuladas como encontradas no documento.

PDFs com várias páginas ou tabelas e arquivos com tabelas descartadas da extração precisam de conferência do recorte. A grade anterior permite corrigir e unir dados. A revisão detalhada é uma exceção, acessível por link. Não há conversão de uma tabela parcialmente reconhecida em carreira completa presumida.

As preparações são gravadas atomicamente por identificador derivado do conteúdo. O diretório fica nos dados locais do usuário, sobrevivendo à troca da pasta do ZIP. Os exemplos do projeto e as tabelas preparadas pelo usuário são identificados separadamente no catálogo. Não foi implementada nesta versão uma pesquisa e extração universal nos sites municipais; quatro dos seis dossiês-piloto continuam sem validação completa, conforme a documentação anterior.

## Excel e regras

Os exportadores financeiro e salarial não foram alterados. A tela simplificada chama as mesmas regras e o mesmo modelo de tabelas. A exportação salarial recalcula a entrada no servidor, mantém fórmulas e caches, todas as classes, as cores e a organização das páginas 9–11 do material do professor. A planilha de referência de Curitiba continua identificada como cenário didático.

O padrão de novas tabelas é arredondamento comercial por etapa. Cafezal preserva truncamento por etapa. A referência, a jornada e as regras podem ser revistas na tela detalhada e nos parâmetros do Excel. Essas escolhas foram autorizadas pelo usuário enquanto aguarda o professor.

## Execução local

`Iniciar.bat` localiza Python 3.11 ou superior, cria `.venv` e instala `requirements.txt` quando necessário. `iniciar.py` reserva uma porta livre em localhost e abre o navegador nesse endereço. Isso impede que outra versão ligada na porta 5000 seja confundida com a nova. O servidor inicia sem debug e sem watchdog; `python app.py` permanece disponível na porta 5000.

O navegador pode bloquear downloads automáticos conforme suas configurações; o botão de baixar novamente permanece visível. O teste automatizado verifica a criação do download em DOM simulado. A execução do `.bat` e a aparência em um Windows real não foram verificadas neste ambiente Linux.
