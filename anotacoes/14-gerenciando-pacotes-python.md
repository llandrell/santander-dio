# Gerenciamento de Pacotes, Convenções e Boas Práticas em Python

## 📦 O que são pacotes?

Pacotes em Python são coleções de módulos organizados em pastas com um
arquivo `__init__.py`, que permitem reutilizar código e organizar melhor
os projetos.

------------------------------------------------------------------------

## 🐍 Papel do pip

O **pip** é o gerenciador de pacotes padrão do Python. Ele permite
instalar, atualizar e remover bibliotecas externas.

### Principais comandos pip:

``` bash
pip install nome-pacote       # Instalar pacote
pip uninstall nome-pacote     # Remover pacote
pip list                      # Listar pacotes instalados
pip freeze > requirements.txt # Exportar dependências
pip install -r requirements.txt # Instalar dependências
```

------------------------------------------------------------------------

## 🌐 Ambientes Virtuais

Ambientes virtuais permitem isolar as dependências de cada projeto,
evitando conflitos entre versões de bibliotecas.

### Criando um ambiente virtual:

``` bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
deactivate                 # Sair do ambiente virtual
```

------------------------------------------------------------------------

## 📂 Gerenciando dependências com Pipenv

O **Pipenv** facilita o gerenciamento de dependências e ambientes
virtuais.

### Principais comandos Pipenv:

``` bash
pipenv install pacote       # Instalar pacote
pipenv uninstall pacote     # Remover pacote
pipenv shell                # Ativar ambiente virtual
pipenv lock                 # Gerar Pipfile.lock
pipenv install --dev pacote # Instalar dependência de desenvolvimento
```

------------------------------------------------------------------------

## 📜 Poetry

O **Poetry** é um gerenciador moderno para dependências e empacotamento
de projetos Python.

### Principais comandos Poetry:

``` bash
poetry init           # Criar novo projeto
poetry add pacote     # Adicionar dependência
poetry remove pacote  # Remover dependência
poetry install        # Instalar dependências
poetry shell          # Ativar ambiente virtual
```

------------------------------------------------------------------------

## 🤔 Qual gerenciador utilizar?

-   **pip + venv** → Simples e padrão do Python.
-   **Pipenv** → Bom para gerenciamento mais automatizado de
    dependências.
-   **Poetry** → Mais moderno, recomendado para projetos maiores e
    publicação de pacotes.

------------------------------------------------------------------------

## ✅ Boas práticas com gerenciamento de pacotes

-   Sempre utilize **ambientes virtuais**.
-   Mantenha um arquivo `requirements.txt` ou `Pipfile` atualizado.
-   Prefira ferramentas automáticas como **Poetry** em projetos grandes.

------------------------------------------------------------------------

# 📝 Convenções e Boas Práticas

## PEP 8

A PEP 8 define convenções de estilo para Python: - Nomes de variáveis em
`snake_case` - Classes em `CamelCase` - Linhas com no máximo **79
caracteres** - 4 espaços para indentação

------------------------------------------------------------------------

## Flake8

Ferramenta de linting que ajuda a identificar violações da PEP 8.

``` bash
pip install flake8
flake8 nome_arquivo.py
```

------------------------------------------------------------------------

## Black - Formatação Automática

Black aplica um formato único para todo o código.

``` bash
pip install black
black nome_arquivo.py
```

------------------------------------------------------------------------

## isort - Organização de Imports

isort organiza automaticamente os imports.

``` bash
pip install isort
isort nome_arquivo.py
```

------------------------------------------------------------------------

## 🌍 Ativando e Desativando Ambiente Virtual

``` bash
# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate

# Desativar
deactivate
```