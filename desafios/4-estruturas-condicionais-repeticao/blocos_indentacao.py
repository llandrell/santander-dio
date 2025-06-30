saldo = float(input("Informe o saldo inicial: "))
valor_saque = float(input("Informe o valor a ser sacado: "))
limite = float(input("Informe o limite da conta: "))
conta_especial = True

def sacar(saldo):
    if saldo >= valor_saque:
       saldo -= valor_saque
       print(f"Você conseguiu sacar: R$ {valor_saque:.2f} com sucesso!")
       print(f"Seu saldo atual é de R$ {saldo:.2f}")

sacar(saldo)
