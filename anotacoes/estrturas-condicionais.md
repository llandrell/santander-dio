
# 🧠 Estruturas Condicionais e de Repetição em Python

Este documento contém anotações, exemplos práticos e resumos teóricos sobre o uso de estruturas de controle de fluxo em Python, como **condicionais (`if`, `elif`, `else`)** e **laços de repetição (`for`, `while`)**.

---

## ✅ Conteúdo Estudado

- Identação e blocos de código
- Estruturas condicionais com `if`, `elif`, `else`
- Operadores relacionais e lógicos
- Condições aninhadas
- Comando `pass`
- Estruturas de repetição com `for` e `while`
- Funções `range()`, `enumerate()` e `input()`
- Interrupções de loop: `break` e `continue`
- Boas práticas com loops

---

## 🔤 Identação e Blocos

Em Python, a identação define os blocos de código. Não são usados `{}` como em outras linguagens.
Atraves da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina

```python
if True:
    print("Este bloco está corretamente identado")
    print("Faz parte do mesmo bloco")
```

**Importante:** O uso incorreto da identação gera erro de sintaxe.

---

## 🔁 Estruturas de Repetição

### Laço `for`

Itera sobre elementos de uma sequência (como listas, strings ou ranges):

```python
for i in range(3):
    print("Repetição:", i)
```

### Laço `while`

Executa um bloco enquanto a condição for verdadeira:

```python
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```

### `break` e `continue`

```python
for i in range(5):
    if i == 3:
        break  # encerra o loop
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue  # pula os pares
    print(i)
```

---

## 🔀 Estruturas Condicionais

### Condicional simples

```python
idade = 20
if idade >= 18:
    print("Maior de idade")
```

### Condicional com `else`

```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

### Condicional com `elif`

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

### Condicional aninhada

```python
x = 10
if x > 0:
    if x % 2 == 0:
        print("Número positivo e par")
```

---



## 🔗 Voltar

[⬅ Voltar para anotações principais](../README.md)
