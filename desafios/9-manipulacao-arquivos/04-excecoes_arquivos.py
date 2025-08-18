from pathlib import Path   # importa a classe Path da biblioteca pathlib para manipular caminhos de arquivos/diretórios de forma mais simples e segura

ROOT_PATH = Path(__file__).parent  # pega o diretório onde este script Python está salvo (arquivo atual) e guarda em ROOT_PATH

try: 
    # tenta abrir um arquivo para leitura
    arquivo = open(ROOT_PATH / "nova_pasta" / "novo_arquiv.txt", "r")  

except FileNotFoundError as exc:  # se o arquivo não existir
    print("Arquivo não encontrado")  # exibe mensagem amigável
    print(exc)                       # exibe a mensagem técnica da exceção

except IsADirectoryError as exc:  # se em vez de arquivo for um diretório
    print("É um diretório, não foi possivel abrir o arquivo")
    print(exc)

except IOError as exc:  # se ocorrer um erro de I/O (leitura/escrita em disco)
    print("Erro na abertura do arquivo")
    print(exc)

except Exception as exc:  # captura qualquer outro erro inesperado
    print("Erro desconhecido")
    print(exc)