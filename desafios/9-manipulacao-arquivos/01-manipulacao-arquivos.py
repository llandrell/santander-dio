
arquivo = open("desafios/9-manipulacao-arquivos/lorem.txt", "r")
#print(arquivo.read())
#print(arquivo.readline())

for linha in arquivo.readlines():
    print(linha)



while len(linha := arquivo.readline()):  # Enquanto o tamanho da string lida for > 0...
    print(linha)                         # imprime a linha (com \n no final)

#Explicando cada parte:

#     while ...: → inicia um laço que repete enquanto a condição for verdadeira.

#     linha := arquivo.readline() → usa o operador walrus (:=, Python 3.8+) para:

#         ler a próxima linha do arquivo com readline() (retorna uma str com o \n no fim; retorna '' quando chega ao EOF),

#         e ao mesmo tempo atribuir esse valor à variável linha.

#     len(...) → pega o comprimento da string lida; quando chegar ao EOF, readline() devolve '' (comprimento 0), então o while para.

#     print(linha) → imprime a linha já contendo \n; como print também adiciona um \n, você verá uma linha em branco extra entre as linhas.

# Sugestões (mais “pythônico” e evitando linha em branco extra):

for linha in arquivo:          # itera diretamente pelas linhas do arquivo
    print(linha, end='')       # não adiciona outro \n

# ou, mantendo o while com walrus e sem len() (que é desnecessário):

while (linha := arquivo.readline()):
    print(linha, end='')





arquivo.close()