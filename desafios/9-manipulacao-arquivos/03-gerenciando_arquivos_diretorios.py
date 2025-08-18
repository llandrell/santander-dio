import os
import shutil 
from pathlib import Path

ROOT_PATH = Path(__file__).parent
print(ROOT_PATH.parent)

# os.mkdir(ROOT_PATH 
# / "novo-diretorio")

# arquivo = open(ROOT_PATH / "novo-arquivo.txt", "w")
# arquivo.close()

# os.rename(ROOT_PATH / "novo-arquivo.txt", ROOT_PATH / "novo-arquivo2.txt")

# os.remove(ROOT_PATH / "novo-arquivo2.txt")

# shutil.move(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "nova_pasta" / "novo_arquivo.txt")