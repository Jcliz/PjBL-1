#CÓDIGOS PARA ACESSO ÀS CONTAS#
login = 654321
senha = 1234
codigo_adm = 123456
acesso = True

#VALOR INICIAL E DA PASSAGEM#
valor_passagem = 6.00
valor_atual = 0.00

#MENU#
while acesso == True:
    menu_inicio = int(input("Qual opção você deseja acessar?\n"
                            "[1] Acesso ao usuário\n"
                            "[2] Acesso ao administrador\n"
                            "[3] Fechar sistema\n"
                            "Selecione sua opção: \n"))

#LOGIN E SENHA#
    if menu_inicio == 1:
        print("Você selecionou a opção do usuário.\n")
        login = int(input("Digite seu login de seis números: \n"))
        senha = int(input("Digite a senha com 4 números: \n"))

        if login == 654321 and senha == 1234:
            print("Você entrou na sua conta de usuário!\n")

#MENU DO USUÁRIO#
            menu_usuario = True
            menu_usuario = int(input("[1] Recarregar cartão\n"
                                 "[2] Usar cartão\n"
                                 "[3] Voltar\n"
                                 "Escolha uma opção: \n"))
            if menu_usuario == 1:
                print("Leve em consideração que se caso o administrador não tenha trocado valor, R$6.00 será o padrão.\n")
                print(f"O seu saldo atual é de {valor_atual}\n")

                cartao = float(input("Valor para recarregar: \n"))
                valor_atual += cartao
                print("Você recarregou seu cartão.\n")

            elif menu_usuario == 2:
                if valor_atual < valor_passagem:
                    print("Você não possui crédito suficientes para realizar essa transação.\n"
                    "Recarregue-os.\n")
                      
                
                elif valor_atual >= valor_passagem:
                    print("Boa viagem!\n")
                    valor_atual -= valor_passagem

                    print(f"Saldo restante = {valor_atual}\n")

            elif menu_usuario == 3:
                menu_usuario = False
        
        else:
            print("Senha incorreta.\n")

#MENU ADMINISTRADOR#
    elif menu_inicio == 2:
        codigo_adm = int(input("Código do administrador: \n"))

        if codigo_adm == 123456:
            menu_adm = True
            menu_adm = int(input("[1] Alterar valor da passagem.\n"
                                 "[2] Visualizar créditos no cartão.\n"
                                 "[3] Voltar.\n"
                                 "Selecione uma opção: \n"))
                      
            if menu_adm == 1:
                valor_passagem = float(input("Nos informe o valor desejado para a passagem: \n"))

                print("Você alterou o valor das passagens da URBS.\n")

        
            elif menu_adm == 2:
                print("O seus créditos atuais presentes em seu cartão: \n", valor_atual)

            elif menu_adm == 3:
                menu_adm = False

        else:    
            print("Código incorreto. Tente novamente.\n")

    elif menu_inicio == 3:
        print("Obrigado pelo acesso!")
        acesso = False
