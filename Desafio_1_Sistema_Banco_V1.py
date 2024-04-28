menu = '''
 ======MENU======

[1] Depositar
[2] Sacar
[3] Extrato
[4] Transferencia
[8] Sair

================
                    
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
limite_transferencia = 1000

while True:

    opcao = input(menu)

    if opcao == "1":
       valor = float(input("Informe o valor do deposito:  "))

       if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor: .2f}\n"

       else:
            print("Operacao falhou! O valor informado é invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        excedeu_saques = numero_saques > limite_saques

        if exedeu_saldo:
            print("Operacao falhou!, nao tem saldo suficiente")

        elif exedeu_limite:
            print("Operacao falhou!, O valor do saque superou o limite diario permitido")

        elif excedeu_saques:
            print("Operacao falhou!, numero de saques superou o limite diario")

        elif valor > 0:

            saldo -= valor 
            extrato += f"saque: R$ {valor: .2f}\n"
            numero_saques += 1

        else:
            print("Operacao Falhou!, O valor informado é invalido")

    elif opcao == "3":
        print("\n === Extrato ===")
        print("")
        print("no fueron realizados movimientos." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo: .2f}")
        print("================")

    elif opcao == "3":
        print("extrato")

    elif opcao == "4":
        valor = float(input("Informe o valor a transferir: "))

        exedeu_saldo = valor > saldo

        exedeu_limite_transferencia = valor > limite_transferencia

        if exedeu_saldo:
            print("Operacao falhou!, nao tem saldo suficiente para realizar a transferencia solicitada")

        elif exedeu_limite_transferencia:
            print("Operacao falhou!, O valor a transferir superou o limite permitido")


        elif valor > 0:

            saldo -= valor 
            extrato += f"Transferencia: R$ {valor: .2f}\n"

        else:
            print("Operacao Falhou!, O valor informado é invalido")

    elif opcao == "8":
        break

    else:
        print("operacao inválida, por favor seleccione nuevamente a operación desejada")

