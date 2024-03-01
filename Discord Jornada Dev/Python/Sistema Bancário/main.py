# Sistema Bancário - Exercício Jornada Dev

# Menu principal
print("Bem vindo ao Jornada Dev Bank, o banco onde você pode depositar a sua esperança!")

finalizar_programa = False # variável de controle de fluxo

lista_clientes = {} # Dicionário vazio que irá armazenar o nome dos clientes e seu saldo atual.

def menu_principal():
    print("------ Jornada Dev Bank ------")
    print("1- Cadastrar Cliente\n""2- Consultar Clientes\n"  
      "3- Depósito\n" "4- Saque\n"
      "5- Sair\n")
    print("Informe a opção desejada:")

def sair():
    print("Agradecemos sua preferência")
    print("Jornada Dev Bank - Deposite a sua esperança :)")
    
    

while finalizar_programa == False:

    menu_principal()
    selecao = int(input())

    # Cadastro de cliente
    
    if selecao == 1:
        cadastro_cliente = True

        while cadastro_cliente == True:

            selecao_cadastro = 0 #variavel do controle de fluxo de cadastro
            
            nome = input("Informe o nome do cliente: ")
            
            lista_clientes[nome] = 0 # Acrescenta o cliente informado na lista de clientes com um saldo 0.
            
            print(f"Cliente {nome} criado com sucesso!\nSaldo Atual: R$", lista_clientes[nome])
            
            print("Para cadastrar novo cliente, aperte 1.\n"
                "Para sair do programa, aperte 2.\n"
                "Para retornar ao menu principal, aperte 0")
                
            selecao_cadastro = int(input())
            
            if selecao_cadastro == 0:
                cadastro_cliente = False
                
            if selecao_cadastro == 1:
                continue
            elif selecao_cadastro == 2:
                sair()
                cadastro_cliente = False
                finalizar_programa = True
            
                


    # Consulta de Clientes

    if selecao == 2:
        consulta_clientes = True
        while consulta_clientes == True:
            print("Imprimindo relação de clientes")
            print(list(lista_clientes.keys()))
            cliente = input("Informe o nome do cliente para consulta de saldo: ")
            print(f"O saldo do(a) cliente {cliente} é R$:",lista_clientes[cliente])
            
            selecao_cliente = 0

            print("Para nova consulta, digite 1.\n"
                  "Para sair do programa, digite 2. \n"
                  "Para voltar ao menu principal, digite 0: ")
            
            selecao_cliente = int(input())
            
            if selecao_cliente == 1:
                continue
            if selecao_cliente == 2:
                sair()
                finalizar_programa = True
            if selecao_cliente == 0:
                consulta_clientes = False
                break


    # Depósitos
        
    if selecao == 3:

        depositos = True

        while depositos == True:
            cliente = (input("Informe o nome do(a) cliente: "))
            valor_deposito = int(input(("Informe o valor a depositar: ")))
            lista_clientes[cliente] += valor_deposito
            print("Depósito procesado com sucesso. Saldo atual: R$", lista_clientes[cliente])

            print("Para realizar novo deposito, digite 1.\n"
                  "Para sair do programa, digite 2.\n"
                  "Para retornar ao menu principal, digite 0: ")
            
            selecao_deposito = int(input())

            if selecao_deposito == 1:
                continue
            if selecao_deposito == 2:
                depositos = False
                sair()
                finalizar_programa = True
            if selecao_deposito == 0:
                depositos = False
                break


    # Saques
        
    if selecao == 4:

        saques = True

        while saques == True:
            cliente = input("Informe o cliente que deseja efetuar o saque: ")
            valor_saque = int(input("Informe o valor a ser sacado em R$: "))

            if valor_saque > lista_clientes[cliente]:
                print("Saldo em conta insuficiente. Transação não autorizada")
                continue
            else: 
                lista_clientes[cliente] -= valor_saque
                print("Transação realizada com sucesso")
                print(f"Cliente: {cliente}\nSaldo Atualizado: R$", lista_clientes[cliente])
                print("Para realizar novo saque, digite 1.\n"
                      "Para sair do programa, digite 2.\n"
                      "Para retornar ao menu principal digite 0.")
                selecao_saque  = int(input())

                if selecao_saque == 1:
                    continue
                if selecao_saque == 2:
                    saques = False
                    sair()
                    finalizar_programa = True
                if selecao_saque == 0:
                    saques = False
                    break


        
    
    if selecao == 5:
        sair()
        finalizar_programa = True

    
    