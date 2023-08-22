menu = """
============== Seja bem vindo! ================
========== Escolha a opção desejada ===========\n
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito efetuado: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        saques_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif limite_excedido:
            print("Operação falhou! O valor do saque excede o limite.")

        elif saques_excedido:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "0":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")