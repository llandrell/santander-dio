# 🧵 Manipulando Strings em Python

Manipulação de textos com Python — fatiamento, concatenação, métodos de string e boas práticas.

---

## 🔤 O que é uma string?

Em Python, uma **string** é uma sequência de caracteres, utilizada para representar textos.  
Você pode criá-las usando aspas simples (`'`), duplas (`"`) ou triplas (`'''` ou `"""`) para textos multi-linha.

```python
nome = "André"
mensagem = 'Olá, mundo!'
texto_longo = """Este é
um texto
com várias linhas."""
```

---
## 🧰 Métodos Úteis de Strings em Python

A linguagem Python oferece diversos métodos nativos para manipulação e formatação de strings. Abaixo, listamos os principais e mais utilizados:

| Método                 | Descrição                                                                 |
|------------------------|--------------------------------------------------------------------------|
| `lower()`              | Converte todos os caracteres da string para minúsculas                   |
| `upper()`              | Converte todos os caracteres da string para maiúsculas                   |
| `capitalize()`         | Deixa apenas a primeira letra em maiúscula e o restante em minúsculo     |
| `title()`              | Converte a primeira letra de cada palavra para maiúscula                 |
| `strip()`              | Remove os espaços em branco do início e do fim da string                 |
| `lstrip()`             | Remove os espaços em branco somente do lado esquerdo (início)            |
| `rstrip()`             | Remove os espaços em branco somente do lado direito (fim)                |
| `center(tam, "simbolo")` | Centraliza o texto com um determinado tamanho, preenchido com o símbolo|
| `replace(a, b)`        | Substitui todas as ocorrências do trecho `a` pelo valor `b`              |
| `split()`              | Divide a string em uma lista, separando pelo espaço ou caractere definido|
| `join(lista)`          | Junta os elementos de uma lista em uma única string                      |
| `find()` / `index()`   | Retorna o índice da primeira ocorrência de um caractere ou substring     |

---

### 🔎 Exemplos de Uso

```python
frase = "  Python é divertido  "

print(frase.strip())                     # "Python é divertido"
print(frase.upper())                     # "  PYTHON É DIVERTIDO  "
print(frase.lower())                     # "  python é divertido  "
print(frase.capitalize())               # "  python é divertido  "
print(frase.title())                     # "  Python É Divertido  "
print(frase.replace("divertido", "poderoso"))  # "  Python é poderoso  "
print(frase.center(30, "-"))             # "---  Python é divertido  ----"
```

> 🔹 Dica: A manipulação de strings é essencial para a entrada e saída de dados, validações, formatação de mensagens e muito mais!

---
## 🔠 Interpolação de variáveis (Formatando Strings)

### Usando `f-strings` (Python 3.6+)

#### Também conhecida como formatação de strings — que é a forma de inserir valores de variáveis dentro de textos (strings) no Python.

```python
nome = "André"
idade = 30
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

---


## ✂️ Fatiamento (Slicing)

Permite acessar partes específicas de uma string por índice.

```python
mensagem = "Python é incrível"

print(mensagem[0])       # P (pega a primeira letra)
print(mensagem[0:6])     # Python (pega a primeira letra e até o ind 6)
print(mensagem[7:])      # é incrível (pega a 7 letras apenas)
print(mensagem[-1])      # l (último caractere)
print(mensagem[7:6:2])      # v (último caractere)
print(mensagem[::-1])      # v (último caractere)
```

---

## ➕ Concatenação

Usa-se o operador `+` para juntar strings.

```python
nome = "André"
saudacao = "Olá, " + nome + "!"
print(saudacao)  # Olá, André!
```

---

## 🔁 Repetição

É possível repetir uma string usando o operador `*`.

```python
print("ha" * 3)  # hahaha
```

---



## 🔍 Verificações com `in`

```python
frase = "Olá, mundo!"
print("Olá" in frase)       # True
print("Python" not in frase)  # True
```

---

## 🔠 Formatando Strings

### Usando `f-strings` (Python 3.6+)

```python
nome = "André"
idade = 30
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
```

### Usando `.format()`

```python
print("Olá, {0}. Você tem {1} anos.".format("Maria", 28))
```

---

## 🧪 Exemplos práticos

### Contar caracteres

```python
frase = "banana"
print(len(frase))  # 6
```

### Separar palavras

```python
mensagem = "Python é incrível"
palavras = mensagem.split()
print(palavras)  # ['Python', 'é', 'incrível']
```

---
## Strings de múltiplas linhas

-são definidas informando 3 aspas simples '''texto''' ou duplas """texto"""
--podem ser ocupadas por várias linhas
--todos os esáçoes em branco são incluídos na string final

---
## 🛠️ Boas práticas

- Sempre use métodos como `.strip()` para limpar entradas do usuário.
- Utilize `lower()` ou `upper()` para fazer comparações seguras, ignorando letras maiúsculas/minúsculas.
- Prefira `f-strings` para legibilidade e eficiência.

---

## 🔗 Voltar

[⬅ Voltar para anotações principais](../README.md)
