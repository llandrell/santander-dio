nome = "  jUliAna   "
profissao = "DesEnVoLveDoRa De SoFtWaRe"
senha = "  senha Secreta "
mensagem = "Olá, Juliana! Seja bem-vinda à plataforma de desenvolvedores."

#Remover os espaços excedentes do nome e da senha.
nome = nome.replace(" ", "") 
senha = senha.replace(" ", "" )
print(nome, senha)

#Converta o nome para Title Case (primeira letra de cada palavra maiúscula).

print(nome.capitalize())

#Converta a profissão toda para minúsculas e exiba com a primeira letra de cada palavra em maiúscula.

profissao = profissao.upper()

print(profissao)

print(profissao.title())

#Exiba a profissão centralizada em um campo de 40 caracteres, preenchido com *.

print(profissao.center(40, "*"))

#Substitua "desenvolvedores" por "profissionais de tecnologia" na mensagem.

print(mensagem.replace("desenvolvedores", "profissionais de tecnologia"))

#Junte o nome e profissão com hífen - e exiba.

lista1 = [nome, profissao]

print('-'.join(lista1))

#Verifique se a palavra "senha" está presente na senha.

if "senha" in senha:
    print("a palavra senha está dentro de  senha, texto de senha: " + senha)


#Exiba apenas a palavra "Juliana" da mensagem (usando find() ou index() e slicing).

inicio_nome = mensagem.find("Juliana") #Aqui, o código procura a posição (índice) em que a palavra "Juliana" começa dentro da string mensagem.
print(inicio_nome) #ou sejá J está na posição 5
fim_nome = inicio_nome + len("Juliana") #Calcula a posição final do nome, somando ao índice inicial o número de caracteres da palavra "Juliana", len("Juliana") retorna 7, então o nome vai da posição 5 até 12 (mas lembrando que o final no slicing não é incluído).
print(fim_nome)

nome_extraido = mensagem[inicio_nome:fim_nome]

print(nome_extraido)

#Aqui é feito o fatiamento da string (slicing), ou seja, extração de uma parte da string.Ele extrai os caracteres entre os índices inicio_nome e fim_nome, sem incluir o último índice.