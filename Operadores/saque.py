saldo = float(input("Informe o Saldo inicial: "))
valor_saque = float(input("Informe o valor que a ser sacado: "))

if saldo >= valor_saque:
    saldo -= valor_saque
    print(f"Você conseguiu sacar: {valor_saque:.2f}, com sucesso!! ")
    print(f"Seu saldo atual e de {saldo:.2f}")
else: print(f"Saldo insuficiente. Saldo Atual: R$: {saldo:.2f}")