# Desafio de Cadastro de Produtos

*Desafio proposto pelo usuário *[Laxus]* no servidor de discord [*Jornada Dev*](https://discord.gg/Wgzapdp6qE).*

Você foi contratado para desenvolver um programa em Python para um pequeno negócio local. O objetivo do programa é permitir que o usuário cadastre itens e seus respectivos preços em um dicionário e, em seguida, seja capaz de visualizar todos os itens cadastrados com seus preços. 

## Requisitos do Programa 

* Ao iniciar o programa, o usuário deve ser apresentado a um menu com as seguintes opções: 
    * [1] Cadastrar item 
    * [2] Mostrar Itens com Preços
    * [3] Sair do programa 
* Se o usuário escolher a opção [1] Cadastrar Item, ele deve ser solicitado a inserir o nome do item e seu preço. Os itens e preços devem ser armazenados em um dicionário. 
* Se o usuário escolher a opção [2] Mostrar itens com preços, o programa deve exibir na tela todos os itens cadastrados juntamente com seus preços, formatados de maneira clara e legível. 
* Se o usuário escolher a opção [3] Sair do Programa, o programa deve encerrar a execução.
* Após cadastrar um item, o usuário deve ter a opção de retornar ao menu principal para realizar outras operações ou sair do programa. 


# Solução Proposta - Jornada Dev Store 

O código para solução proposta possui duas funções simples, `menu_principal` e `sair` que dão retorno textual às escolhas realizadas pelo usuário. 

A execução do algoritmo ocorre dentro de um loop `while` vinculada a uma variável booleana `encerrar_programa` que é inicializada com o valor `False`. 

Dentro desse loop há uma variável denominada `selecao` que funciona como controle de fluxo, considerando as opções do menu principal. Variáveis semelhantes são utilizadas nas seções de cadastro de novo item e exibição dos itens. 

Os itens são armazenados como **chaves** no dicionário `itens` e os valores são recebidos como `float`. 

