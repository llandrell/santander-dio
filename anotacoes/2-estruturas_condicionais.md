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
Através da indentação, o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

```python
if True:
    print("Este bloco está corretamente identado")
    print("Faz parte do mesmo bloco")
```

**Importante:** O uso incorreto da identação gera erro de sintaxe.

---

## 🔁 Estruturas de Repetição

Estruturas de repetição (ou laços de repetição) são comandos usados em programação para executar um bloco de código várias vezes, de forma automática, até que uma condição seja satisfeita ou deixada de ser verdadeira.

### Laço `for`

Itera sobre elementos de uma sequência (como listas, strings ou ranges).  
É ideal quando sabemos antecipadamente quantas vezes o laço deve repetir.



```python
# Estrutura básica do for
for variável in sequência:
    # bloco de código

 Operadores de Associação em Python

## ✅ O que são?

Os **operadores de associação** são utilizados para verificar se **um valor está ou não presente** dentro de uma coleção (como listas, strings, dicionários, tuplas, conjuntos, etc.).

---

## ✅ Operadores

| Operador  | Significado                               |
|-----------|-------------------------------------------|
| `in`      | Retorna `True` se o valor **está presente** |
| `not in`  | Retorna `True` se o valor **não está presente** |

---

## 📌 Exemplos Práticos

### 🔹 Em listas:
```python
frutas = ["maçã", "banana", "laranja"]

print("banana" in frutas)        # True
print("melancia" not in frutas)  # True
```

### 🔹 Em strings:
```python
mensagem = "Bem-vindo ao Python!"

print("Python" in mensagem)     # True
print("Java" not in mensagem)   # True
```

### 🔹 Em dicionários (verifica **chaves**, não valores):
```python
usuario = {"nome": "André", "idade": 30}

print("nome" in usuario)    # True
print("André" in usuario)   # False
```

---

## 🛠️ Uso no Dia a Dia

### ✅ 1. Validação de entrada do usuário
```python
opcoes_validas = ["s", "n"]

entrada = input("Deseja continuar? (s/n): ").lower()
if entrada in opcoes_validas:
    print("Entrada aceita!")
else:
    print("Opção inválida.")
```

### ✅ 2. Verificar se usuário tem permissão
```python
usuarios_autorizados = ["joao", "maria", "ana"]

nome = input("Digite seu nome de usuário: ")
if nome.lower() in usuarios_autorizados:
    print("Acesso liberado")
else:
    print("Usuário não autorizado")
```

### ✅ 3. Verificar espaços em senha
```python
senha = input("Digite sua senha: ")

if " " in senha:
    print("A senha não pode conter espaços.")
```

### ✅ 4. Conferir se chave existe em dicionário
```python
dados = {"nome": "Lucas", "idade": 25}

if "idade" in dados:
    print(f"Idade: {dados['idade']}")
```

---

## ⚠️ Observação

- O operador `in` é **sensível à capitalização (MAIUSCULO e menusculo)**:
```python
print("A" in "abacaxi")  # False
print("a" in "abacaxi")  # True
```

---

## ✅ Resumo Prático

| Situação                              | Usa `in` ou `not in`? |
|---------------------------------------|------------------------|
| Verificar se valor está em lista      | `in`                  |
| Verificar se valor **não** está em lista | `not in`           |
| Verificar se caractere está em string | `in`                  |
| Verificar se chave está em dicionário | `in`                  |


## 🔤 range

range é uma função embutida em Python que gera uma sequência de números inteiros, que pode ser usada especialmente em loops for para iterar um número específico de vezes.
Como funciona?

A função range() pode ser usada de três formas principais:

    range(fim)
    Gera números de 0 até fim - 1.

# Exemplo 1: usando range()
for i in range(3):
    print("Repetição:", i)

# Exemplo 2: percorrendo uma lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print("Eu gosto de", fruta)
```

- A função `range()` gera uma sequência de números que o `for` pode percorrer.  
- `range()` pode receber até três argumentos:

  - **início**: valor inicial da sequência (inclusivo)  
  - **fim**: valor final da sequência (exclusivo)  
  - **passo**: o incremento a cada iteração (pode ser positivo ou negativo)  

```python
for i in range(2, 10, 2):  # começa em 2, vai até 9, pulando de 2 em 2
    print(i)
```

- Se não passar nenhum argumento, `range()` começa do zero e vai até o número passado (exclusivo):

```python
for i in range(5):  # 0 até 4
    print(i)
```

- Combine com `enumerate()` para obter o índice e o valor simultaneamente.

Quando você percorre uma sequência (como uma lista), às vezes precisa do índice (posição) e do valor ao mesmo tempo. O `enumerate()` permite isso, retornando uma tupla `(índice, valor)` em cada iteração.

```python
frutas = ["maçã", "banana", "uva"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")
```

**Saída:**

```
0: maçã
1: banana
2: uva
```

---

### Laço `while` (enquanto)

Executa um bloco enquanto a condição for verdadeira:

```python
contador = 0
while contador < 3: #enquanto contador menor 3
    print("Contador:", contador)
    contador += 1
```

---

### `break` e `continue`

Controlam o fluxo do loop:

```python
for i in range(5):
    if i == 3:
        break  # encerra o loop
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue  # pula os números pares
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
