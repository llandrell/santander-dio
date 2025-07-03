
# 📘 Tipos e Operadores em Python

Este documento é um guia completo sobre os **tipos de dados** e **operadores** em Python.  
Foi elaborado com foco didático, como se fosse um caderno de anotações estruturado para facilitar o aprendizado e a revisão.

---

## 🧠 Sobre Tipagem em Python

Python é uma linguagem:

- **Fortemente tipada**: não permite operações entre tipos incompatíveis (ex: `int` com `str`), sem conversão explícita.
- **Dinamicamente tipada**: não é necessário declarar o tipo da variável, ele é inferido automaticamente em tempo de execução.

### Exemplos:

```python
idade = 30           # tipo: int
nome = "André"       # tipo: str
pi = 3.1415          # tipo: float
ativo = True         # tipo: bool
nulo = None          # tipo: NoneType
```

É possível sobrescrever variáveis com outro tipo:

```python
valor = 10       # int
valor = "dez"    # agora é uma string
```

---

## 🔢 Tipos Básicos de Dados

| Tipo       | Nome técnico   | Exemplo               | Observações                         |
|------------|----------------|------------------------|-------------------------------------|
| `int`      | Inteiro        | `10`, `-3`, `0`        | Números sem ponto decimal           |
| `float`    | Decimal        | `3.14`, `-0.001`       | Números com ponto decimal           |
| `str`      | Texto          | `"Olá"`, `'Python'`    | Sempre entre aspas simples ou duplas|
| `bool`     | Booleano       | `True`, `False`        | Lógico: verdadeiro ou falso         |
| `NoneType` | Valor nulo     | `None`                 | Representa ausência de valor        |

---

## ➕ Operadores Aritméticos

São usados para realizar **operações matemáticas**.

| Operador | Operação          | Exemplo     | Resultado | Observações                     |
|----------|-------------------|-------------|-----------|----------------------------------|
| `+`      | Adição            | `4 + 5`     | `9`       | Soma dois valores                |
| `-`      | Subtração         | `10 - 3`    | `7`       | Subtrai valores                  |
| `*`      | Multiplicação     | `3 * 2`     | `6`       | Multiplica valores               |
| `/`      | Divisão real      | `10 / 4`    | `2.5`     | Resultado sempre `float`         |
| `//`     | Divisão inteira   | `10 // 4`   | `2`       | Descarta o valor decimal         |
| `%`      | Módulo (resto)    | `10 % 3`    | `1`       | Retorna o resto da divisão       |
| `**`     | Potência          | `2 ** 3`    | `8`       | Exponenciação                    |

---

## ⚖️ Operadores Relacionais

Permitem comparar dois valores e retornam `True` ou `False`.

| Operador | Descrição           | Exemplo     | Resultado |
|----------|---------------------|-------------|-----------|
| `==`     | Igual a             | `3 == 3`    | `True`    |
| `!=`     | Diferente de        | `3 != 4`    | `True`    |
| `>`      | Maior que           | `5 > 2`     | `True`    |
| `<`      | Menor que           | `2 < 5`     | `True`    |
| `>=`     | Maior ou igual      | `5 >= 5`    | `True`    |
| `<=`     | Menor ou igual      | `4 <= 6`    | `True`    |

### Uso comum em condições:

```python
idade = 20
if idade >= 18:
    print("É maior de idade")
```

---

## 🔀 Operadores Lógicos

Usados para combinar **expressões booleanas**.

| Operador | Significado         | Exemplo              | Resultado |
|----------|---------------------|----------------------|-----------|
| `and`    | E (ambas verdadeiras)| `True and False`     | `False`   |
| `or`     | OU (uma ou ambas)    | `True or False`      | `True`    |
| `not`    | Negação lógica       | `not True`           | `False`   |

### Precedência (ordem de execução):

1. Parênteses `()`
2. `not`
3. `and`
4. `or`

---

## 🖊️ Operadores de Atribuição

| Operador | Descrição                    | Exemplo     | Equivalente a     |
|----------|------------------------------|-------------|-------------------|
| `=`      | Atribuição simples           | `x = 5`     | x recebe 5        |
| `+=`     | Soma e atribui               | `x += 2`    | `x = x + 2`       |
| `-=`     | Subtrai e atribui            | `x -= 1`    | `x = x - 1`       |
| `*=`     | Multiplica e atribui         | `x *= 3`    | `x = x * 3`       |
| `/=`     | Divide e atribui             | `x /= 2`    | `x = x / 2`       |
| `//=`    | Divisão inteira e atribui    | `x //= 2`   | `x = x // 2`      |
| `%=`     | Módulo e atribui             | `x %= 3`    | `x = x % 3`       |
| `**=`    | Potência e atribui           | `x **= 2`   | `x = x ** 2`      |

---

## 🔡 Operações com Strings

### Concatenação (juntar strings):

```python
nome = "André"
mensagem = "Olá, " + nome
print(mensagem)  # Olá, André
```

### Repetição:

```python
print("Python! " * 3)
# Resultado: Python! Python! Python!
```

---

## 📌 Observações Avançadas

- Tipos podem ser conferidos com `type()`  
- Conversões: `int("5")`, `str(10)`, `float("3.14")`  
- Operadores lógicos funcionam com estruturas como listas, dicionários e strings (ex: `if lista:` verifica se está vazia)

---

## 🧠 Exercício de Fixação

```python
a = 5
b = 3
print((a > b) and (b < 10))  # True
```

---

## 🔗 Voltar

[⬅ Voltar para anotações principais](../README.md)