users= []
contas = []
num_conta = 1
LIMITE_SAQUES = 3


#função com o texto do menu
def menu():
    text_menu = """
    Escolha uma OPÇÃO:
    [1] Cadastrar novo Cliente
    [2] Criar conta Bancária
    [3] Acessar Menu da conta
    [4] Lista contas
    [5] Sair
    """
    option = input(text_menu + "\nDigite a opção desejada: ")
    return option

def menu_conta():
    text_menu = """
    Escolha uma OPÇÃO do seu menu conta:

    [1] Saque
    [2] Depositar
    [3] Extrato
    [4] Sair
    """
    option = input(text_menu + "\nDigite a opção desejada: ")
    return option

def verificar_cpf(cpf, users):
        # Verificar se o CPF já está cadastrado
    for user in users:
        if user["cpf"] == cpf:
            return True
    return False

def buscar_usuario_por_cpf(cpf, users):

    for user in users:
        if user["cpf"] == cpf:
            return user  # Retorna o dicionário do usuário
    return None  # Caso não encontre

def buscar_conta_por_cpf(cpf, contas):
    for conta in contas:
        if conta["user_conta"]["cpf"] == cpf:
            return conta  # Retorna a conta inteira
    return None

def cadastrar_user(users):
    # Entrada de dados do usuário
    cpf = input("Informe o CPF (apenas os 11 dígitos): ").strip()
    # Validação básica do CPF (verifica se tem 11 caracteres numéricos)
    if not (cpf.isdigit() and len(cpf) == 11): # .isdigit() é usado para verificar se todos os caracteres de uma string são dígitos numéricos  e len(cpf) pega o tamanho e verifica se tem 11
        print("❌ CPF inválido! Deve conter exatamente 11 números.")
        return  # Sai da função para evitar cadastro inválido
    
   
    # Verificar se o CPF já está cadastrado
    if verificar_cpf(cpf, users):
     print("❌ Usuário já cadastrado com esse CPF.")
     return
        
    name = input("informe o nome completo do usuario: ").strip() # .strip() é usado para remover esposos em branco
    date_nasc = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()


    # Coletando endereço do usuário
    Address = {
        "logradouro": input("Informe o logradouro: ").strip(),
        "num_casa": input("Informe o número da casa: ").strip(),
        "bairro": input("Informe o bairro: ").strip(),
        "cidade_uf": input("Informe a cidade e a sigla do seu estado: ").strip()
    }

    #atribuindo os valores ao usuario
    user = {
        "nome": name,
        "data_nasc": date_nasc,
        "cpf": cpf,
        "endereco": Address
    }
        # Adiciona o usuário no dicionário de usuários com CPF como chave
    users.append(user)
    print("✅ Usuário cadastrado com sucesso!")

def criar_conta_corrente(users, contas, num_conta):
    # Solicita e valida CPF
    cpf = input("Informe o CPF (apenas os 11 dígitos): ").strip()

    if not (cpf.isdigit() and len(cpf) == 11): # .isdigit() é usado para verificar se todos os caracteres de uma string são dígitos numéricos  e len(cpf) pega o tamanho e verifica se tem 11
        print("❌ CPF inválido! Deve conter exatamente 11 números.")
        return  # Sai da função para evitar cadastro inválido
    
    # Verifica se o CPF está cadastrado
    if not verificar_cpf(cpf, users):
     print("❌ Usuário não cadastrado com esse CPF favor realizar o cadastro do cliente.")
     return num_conta
    # Busca os dados do usuário pelo CPF
    user_conta = buscar_usuario_por_cpf(cpf, users)   

    # Dados da fixo da conta
    AGENCIA= "0001"
    saldo = 0.0
    num_saques = 0
    extrato = []

    conta = {
        "num_conta": num_conta,
        "agencia": AGENCIA,
        "user_conta": user_conta,
        "saldo": saldo,
        "extrato": extrato,
        "num_saques": num_saques
    }
    contas.append(conta)
    print("✅ conta cadastrado com sucesso!")
    print(f"Número da Conta: {num_conta}")
    print(f"Agência: {AGENCIA}")
    return num_conta + 1 # Retorna o próximo número de conta

def deposito(valor, saldo, extrato, /,):

    if valor > 0:

        saldo += valor
        extrato.append(f"Depósito R$: {valor:.2f}\n")
        print(f"✅ Depósito de R$: {valor:.2f} realizado com sucesso.")
    else:
        print("❌ Valor inválido. O depósito deve ser maior que zero.")

    return saldo, extrato

def saque(*, valor, saldo, extrato, numero_saque, LIMITE_SAQUES):
        if numero_saque >= LIMITE_SAQUES:
         print("❌ Número de saques excedeu o limite.")

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
    print("\n===== 📄EXTRATO =====")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
    print("==========================\n")

def listar_contas(contas):
    for conta in contas:
        usuario = conta["user_conta"]
        print(f"""
        Agência: {conta['agencia']}  Conta: {conta['num_conta']}
        Titular: {usuario['nome']}  CPF: {usuario['cpf']}
        -----------------------------
        """)

# while para verificar as opções do menu
while True:
    try:
        option = int(menu().strip())
    except ValueError:
        print("❌ Digite apenas números!")
        continue
    if option == 1:
        print("Cadastrar de novos Clientes selecionado.")
        cadastrar_user(users)

    elif option == 2:
        print("Cadastrar de conta selecionado.")
        num_conta = criar_conta_corrente(users, contas, num_conta)

    elif option == 3:
        print("Menu conta Selecionado.")
         # Entrada de dados do usuário

        cpf = input("Informe o CPF (apenas os 11 dígitos): ").strip()
         # Validação básica do CPF (verifica se tem 11 caracteres numéricos)

        if not (cpf.isdigit() and len(cpf) == 11): # .isdigit() é usado para verificar se todos os caracteres de uma string são dígitos numéricos  e len(cpf) pega o tamanho e verifica se tem 11
           print("❌ CPF inválido! Deve conter exatamente 11 números.")
           continue  # Volta ao menu principal

        conta = buscar_conta_por_cpf(cpf, contas)

        if conta is None:
            print("❌ Conta não encontrado. Cadastre um cliente primeiro.")
            continue  # Volta para o menu principal

        else:
            while True:

                try:
                    option_conta = int(menu_conta().strip())
                except ValueError:
                    print("❌ Digite apenas números!")
                    continue

                if option_conta == 1:
                    print("Saque selecionado")
                    valor = float(input("Informe o valor a ser sacado: "))
                    conta["saldo"], conta["extrato"], conta["num_saques"] = saque( valor = valor,
                                                                                  saldo = conta["saldo"],
                                                                                  extrato = conta["extrato"],
                                                                                  numero_saque = conta["num_saques"],
                                                                                  LIMITE_SAQUES = LIMITE_SAQUES)

                elif option_conta == 2:
                    print("Deposito Selecionado.")
                    valor = float(input("Informe o valor do depósito: "))
                    conta["saldo"], conta["extrato"] = deposito(valor,
                                                conta["saldo"],
                                                conta["extrato"])

                elif option_conta == 3:
                    print("Extrato Selecionado")
                    impExtrato(conta["extrato"], conta["saldo"])

                elif option_conta == 4:
                    print("Saindo do menu conta...")
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")
      
    elif option == 4:
        listar_contas(contas)


    elif option == 5:
        print("Encerrando o programa...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
