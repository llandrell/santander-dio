saldo = float(input("Informe o saldo inicial: "))
valor_saque = float(input("Informe o valor a ser sacado: "))
limite = float(input("Informe o limite da conta: "))
conta_especial = True

if saldo >= valor_saque:
    saldo -= valor_saque
    print(f"Você conseguiu sacar: R$ {valor_saque:.2f} com sucesso!")
    print(f"Seu saldo atual é de R$ {saldo:.2f}")

elif conta_especial and (saldo + limite) >= valor_saque:
    # Usa o cheque especial
    valor_utilizado_limite = valor_saque - saldo
    saldo = 0
    limite -= valor_utilizado_limite
    print(f"Você conseguiu sacar: R$ {valor_saque:.2f}, usando o limite do cheque especial.")
    print(f"Seu saldo atual é de R$ {saldo:.2f}")
    print(f"Limite restante: R$ {limite:.2f}")

else:
    print(f"Saldo insuficiente. Saldo atual: R$ {saldo:.2f}, limite: R$ {limite:.2f}")