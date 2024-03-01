def menu_principal():
    print("Bem vindo, selecione a opção desejada:\n"
          "[1] Cadastrar Item\n"
          "[2] Mostrar Itens e Preços\n"
          "[3] Sair do Programa\n")

def sair():
    print("\n *** Jornada Dev Store - Seu Sonho Está Aqui! ***")

encerrar_programa = False

itens = {}

while encerrar_programa == False:

    menu_principal()
    selecao = int(input())

    if selecao == 1:
        produto = input("Informe o nome do produto: ")
        valor = float(input("Informe o valor do produto: "))
        itens[produto] = valor

        selecao_cadastro = 0

        print("[1] Menu Principal\n"
              "[2] Sair do programa")
        selecao_cadastro = int(input())

        if selecao_cadastro == 1:
            continue
        elif selecao_cadastro == 2:
            sair()
            encerrar_programa = True
            break
        else:
            print("Opção inválida, retornando ao menu principal")
            continue

    
    elif selecao == 2:

        print("Itens cadastrados: ")

        for item in itens: 
            print(f"** {item} ** ----> R$: {itens[item]:.2f}")
        
        selecao_exibir = 0

        print("[1] Menu Principal\n"
              "[2] Sair do programa")
        
        selecao_exibir = int(input())

        if selecao_exibir == 1:
            continue

        elif selecao_exibir == 2:
            sair()
            encerrar_programa == True
            break
        
        else:
            print("Opção inválida, retornando ao menu principal")
            continue


    elif selecao == 3:
        sair()
        encerrar_programa == True
        break

    else:
        print("Opção inválida, retornando ao menu principal")
        continue






