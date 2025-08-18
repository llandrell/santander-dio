file = open('desafios/9-manipulacao-arquivos/lorem.txt1', 'w')

file.write("olá, word")

file.writelines(["\n", "olá, mundo2", "\n", "olá, mundo3", "\n", "olá, mundo4"])
file.close()

file = open('desafios/9-manipulacao-arquivos/lorem.txt1', 'r')
print(file.read())

file.close()
