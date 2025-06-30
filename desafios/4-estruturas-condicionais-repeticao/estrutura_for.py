# Solicita que o usuário digite um texto e armazena na variável 'texto'
texto = input("Informe um texto: ")

# Define uma string contendo as vogais maiúsculas para facilitar a comparação
VOGAIS = "AEIOU"

# Para cada(for) letra presente(in) na variável 'texto', faça o seguinte:
for letra in texto:
    # Se (para cada) letra Transforme em maiúscula e verifiqye se ela está dentro da string VOGAIS
    if letra.upper() in VOGAIS:
        # Se for vogal, imprime essa letra na tela sem pular linha
        print(letra, end="")

# Após terminar o laço, imprime uma linha em branco para organizar a saída no terminal
print()