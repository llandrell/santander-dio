lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]         # ['t', 'h', 'o', 'n']
# Começa no índice 2 (letra 't') até o final da lista.

lista[:2]         # ['p', 'y']
# Vai do início [0] até o índice 2 (exclui o elemento do índice 2).

lista[1:3]        # ['y', 't']
# Começa no índice 1 (letra 'y') até o índice 3 (exclui o índice 3).

lista[0:3:2]      # ['p', 't']
# Vai do índice 0 ao 3 (sem incluir o 3), pulando de 2 em 2 elementos. [step]

lista[::]         # ['p', 'y', 't', 'h', 'o', 'n']
# Copia a lista inteira (sem definir início, fim ou passo).

lista[::-1]       # ['n', 'o', 'h', 't', 'y', 'p']
# Retorna a lista invertida (passo -1).


#Criando listas
frutas = ["maçã", "banana", "uva"]         # Forma mais comum
letras = list("python")                    # Com construtor e iterável
numeros = list(range(10))                  # De 0 a 9
carro = ["Ferrari", "F8", 190, True]       # Tipos mistos

# Adicionando elementos
frutas.append("laranja")

# Acessando elementos por índice
print(frutas[0])        # "maçã"

# Acesso com índices negativos
print(frutas[-1])       # "laranja" (último)
print(frutas[-3])       # "banana"
print(frutas[-4])       # "maçã"

# Listas aninhadas (ex: matriz)
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "C"]
]