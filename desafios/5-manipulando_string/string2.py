mensagem = "Python é incrível"

# 🟢 Pega o primeiro caractere (índice 0)
print(mensagem[0])       
# Saída: P

# 🟢 Pega os caracteres do índice 0 até o 5 (o índice 6 não é incluído)
print(mensagem[0:6])     
# Saída: Python

# 🟢 Pega os caracteres do índice 7 até o final
print(mensagem[7:])      
# Saída: é incrível

# 🟢 Pega os caracteres do início até o índice 6 (ou seja, até antes do índice 7)
print(mensagem[:7])      
# Saída: Python 

# 🟢 Pega o último caractere da string
print(mensagem[-1])      
# Saída: l

# 🟢 Pega os caracteres do índice 2 ao 7 (excluindo o 8), pulando de 2 em 2
print(mensagem[2:8:2])      
# Saída: toh
# Explicação: índices 2 a 7 → ['t', 'h', 'o', 'n', ' '] → com passo 2 → ['t', 'o', 'h']

# 🟢 Inverte a string
print(mensagem[::-1])      
# Saída: levícni é nohtyP