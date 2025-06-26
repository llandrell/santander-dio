nome = input("Informe seu nome: ")#atribuindo o valor do imput  a variavel nome
idade = int(input("Informe sua idade: "))#atribuindo e convertendo para int atraveis do imput a variavel idade

print(f"Nome: {nome}, Idade: {idade}")#formatando e imprimindo as variaveis

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="*", end="$$$")