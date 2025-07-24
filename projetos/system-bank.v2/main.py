users= []



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


# função para cadastrar usuarios
def cadastrar_user(users):
    # Entrada de dados do usuário
    cpf = input("Informe o CPF (apenas os 11 dígitos): ").strip()
    # Validação básica do CPF (verifica se tem 11 caracteres numéricos)
    if not (cpf.isdigit() and len(cpf) == 11): # .isdigit() é usado para verificar se todos os caracteres de uma string são dígitos numéricos  e len(cpf) pega o tamanho e verifica se tem 11
        print("❌ CPF inválido! Deve conter exatamente 11 números.")
        return  # Sai da função para evitar cadastro inválido
    
   
    # Verificar se o CPF já está cadastrado
    for user in users:
        if user["cpf"] == cpf:
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





# while para verificar as opções do menu
while True:
    option = int(menu().strip())
    if option == 1:
        print("Cadastrar de novos Clientes selecionado.")
        cadastrar_user(users)
    elif option == 5:
        print("Encerrando o programa...")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
