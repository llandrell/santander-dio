#Declaração  das funções

def deposito(valor, saldo, extrato):
    """
        Realiza um depósito na conta, atualiza o saldo e registra no extrato.

        Parâmetros:
        - valor (float): valor a ser depositado.
        - saldo (float): saldo atual da conta.
        - extrato (str): string contendo o extrato anterior.

        Retorna:
        - saldo (float): novo saldo atualizado.
        - extrato (str): extrato atualizado com a transação.
    """
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito R$: {valor:.2f}\n")
        print(f"✅ Depósito de R$: {valor:.2f} realizado com sucesso.")
    else:
        print("❌ Valor inválido. O depósito deve ser maior que zero.")

    return saldo, extrato

def saque(valor, saldo, extrato, numero_saque, LIMITE_SAQUES):
    """
        Realiza um saque na conta, atualiza o saldo e registra no extrato.

        Parâmetros:
        - valor (float): valor a ser depositado.
        - saldo (float): saldo atual da conta.
        - extrato (str): string contendo o extrato anterior.

        Retorna:
        - saldo (float): novo saldo atualizado.
        - extrato (str): extrato atualizado com a transação.
    """

    if numero_saque >= LIMITE_SAQUES:
        print("Numero de saque excedido o limte")

    elif valor <= 0:
        print("❌ Valor inválido. O saque deve ser maior que zero.")

    
    elif valor > saldo:
        print("❌ Saldo insuficiente para saque.")

    else:
        saldo -= valor
        extrato.append(f"Saque R$: {valor:.2f}\n")
        print(f"✅ Saque de R$: {valor:.2f} realizado com sucesso.")
        numero_saque += 1


    return saldo, extrato, numero_saque

def impExtrato(extrato, saldo):
    print("\n📄 Extrato:")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")


# Criamos uma variável chamada `menu` com uma string que será usada para exibir as opções disponíveis para o usuário.
menu = """
[d] Deposito
[s] Sacar
[e] Extrato
[q] sair

=> """

#declarações das variaveis 

saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu).strip().lower()  # <- tratamento da entrada do usuário
    if opcao == "d":
        print("Depósito selecionado.")
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)
    elif opcao == "s":
        print("Saque selecionado.")
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saque = saque(valor, saldo, extrato, numero_saque, LIMITE_SAQUES)

    elif opcao == "e":
        print("Extrato selecionado.")
        impExtrato(extrato, saldo)
    elif opcao == "q":
        print("Saindo do sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


