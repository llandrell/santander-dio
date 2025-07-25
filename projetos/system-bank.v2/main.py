users= []
contas = []
num_conta = 1


#função com o texto do menu
def menu():
    text_menu = """
    Escolha uma OPÇÃO:
    [1] Cadastrar novo Cliente
    [2] Criar conta Bancária
    [3] Acessar Menu da conta
    [4] Área do Gerente
    [5] Sair
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

# função para cadastrar usuarios
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
    agencia = "0001"


    conta = {
        "num_conta": num_conta,
        "agencia": agencia,
        "user_conta": user_conta
    }
    contas.append(conta)
    print("✅ conta cadastrado com sucesso!")
    print("✅ Conta cadastrada com sucesso!")
    print(f"Número da Conta: {num_conta}")
    print(f"Agência: {agencia}")
    return num_conta + 1 # Retorna o próximo número de conta


# while para verificar as opções do menu
while True:
    option = int(menu().strip())
    if option == 1:
        print("Cadastrar de novos Clientes selecionado.")
        cadastrar_user(users)
    elif option == 2:
        print("Cadastrar de conta selecionado.")
        num_conta = criar_conta_corrente(users, contas, num_conta)
    
    elif option == 5:
        print("Encerrando o programa...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
