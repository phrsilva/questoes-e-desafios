# Jornada Dev Bank

O script Jornada Dev Bank é uma proposta de solução do desafio posto na comunidade Jornada Dev do Discord.

O código simula um sistema bancário que possibilita ao usuário cadastrar clientes, consultar os clientes cadastrados e efetuar operações de depósito e saques para estes clientes.

A lógica principal de funcionamento é que o programa permaneça aberto até que o usuário decida encerrá-lo, possibilitando a execução de múltiplas operações na mesma sessão. Para isso, é utilizada uma condição ``` while ``` cujo encerramento está vinculado a um ``` input ``` do usuário. 

## Funções

Como o programa está em um ciclo continuo, criei duas funções simples para reproduzir a interface textual de um menu principal e uma mensagem de encerramento

### menu_principal 

Esta função retorna as quatro operações como opções a serem selecionadas pelo usuário e também permite que o usuário opte por encerrar o sistema. 

### sair 

Uma simples mensagem de despedida ao encerrar a execução do programa

## Variáveis

### finalizar_programa

Uma variável booleana com valor padrão `False` que permite a execução em loop do script

### lista_clientes

Um dicionário, inicializado vazio, que armazena o nome do cliente como chave e seu saldo como valor. 

### variáveis selecao 

Dentro dos módulos de cadastro, consulta, depósito e saque foram criados loops internos que permitem que o mesmo módulo possa ser executado várias vezes. Para controle desses loops foram criadas variáves boolenas específicas e variáveis input do tipo inteiro que pedem uma resposta do usuário para direcionar o fluxo do programa.

