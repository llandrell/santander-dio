from pathlib import Path   
ROOT_PATH = Path(__file__).parent 

# arquivo = open(ROOT_PATH / "lorem.txt", "r")

# print(arquivo.read())
# arquivo.close()

# with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
#     print(arquivo.read())

# print(arquivo.read())

# try:
#     with open(ROOT_PATH / "larem.txt", "r") as arquivo:
#         print(arquivo.read())
# except IOError as exc:
#     print(f"Erro na abertura do arquivo {exc}")

# try:
#     with open(ROOT_PATH / "lorem-utf-8.txt", "w", encoding='utf-8') as arquivo:
#         arquivo.write('Aprendendo a manipular arquivos utilizando Python.')
        
# except IOError as exc:
#     print(f"Erro na abertura do arquivo {exc}")

try:
    with open(ROOT_PATH / "lorem-utf-8.txt", "r", encoding='ascii') as arquivo:
        print(arquivo.read())
#vale tambem para gravação

except IOError as exc:
        print(f"Erro na abertura do arquivo {exc}")
except UnicodeDecodeError as exc:
        print(f"Erro na codificação do arquivo {exc}")
except Exception as exc:
        print(f"Erro desconhecido {exc}")