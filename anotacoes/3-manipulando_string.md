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

## ✂️ Fatiamento (Slicing)

Permite acessar partes específicas de uma string por índice.

```python
mensagem = "Python é incrível"

print(mensagem[0])       # P
print(mensagem[0:6])     # Python
print(mensagem[7:])      # é incrível
print(mensagem[-1])      # l (último caractere)
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

## 🧰 Métodos úteis de string

| Método             | Descrição                                      |
|--------------------|-----------------------------------------------|
| `lower()`          | Converte para minúsculas                      |
| `upper()`          | Converte para maiúsculas                      |
| `capitalize()`     | Primeira letra maiúscula                      |
| `title()`          | Primeira letra de cada palavra em maiúscula  |
| `strip()`          | Remove espaços no início e fim               |
| `replace(a, b)`    | Substitui `a` por `b`                         |
| `split()`          | Divide string em lista                        |
| `join(lista)`      | Junta elementos de uma lista em uma string    |
| `find()` / `index()` | Retorna o índice de um caractere/texto     |

### Exemplos:

```python
frase = "  Python é divertido  "

print(frase.strip())        # "Python é divertido"
print(frase.upper())        # "  PYTHON É DIVERTIDO  "
print(frase.lower())        # "  python é divertido  "
print(frase.replace("divertido", "poderoso"))  # "  Python é poderoso  "
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

## 🛠️ Boas práticas

- Sempre use métodos como `.strip()` para limpar entradas do usuário.
- Utilize `lower()` ou `upper()` para fazer comparações seguras, ignorando letras maiúsculas/minúsculas.
- Prefira `f-strings` para legibilidade e eficiência.

---

## 🔗 Voltar

[⬅ Voltar para anotações principais](../README.md)
