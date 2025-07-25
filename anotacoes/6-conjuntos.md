# 🧩 Conjuntos em Python (set)

## ✅ O que é um Conjunto em Python?

Um **conjunto** em Python é uma coleção de objetso e uma estrutura de dados que armazena **elementos únicos e não ordenados**. Ou seja, **não permite valores duplicados** e **não garante a ordem** dos itens armazenados. Os conjuntos são baseados na teoria dos conjuntos da matemática.

---

## 🧱 Estrutura

- Os conjuntos em Python são implementados pela classe `set()`.
- Seus elementos precisam ser **imutáveis** (ex: números, strings, tuplas).
- Conjuntos em si **são mutáveis** — você pode adicionar e remover elementos.

---

## 🛠️ Como Criar um Conjunto

Existem duas formas principais de criar conjuntos:

### 1. Usando chaves `{}`:
```python
meu_conjunto = {1, 2, 3}
```

### 2. Usando a função `set()`:
```python
meu_conjunto = set([1, 2, 3])
```

###você pode usando o set eleinar elementos duplicados em uma lista passando como paremetro a lista na criação do conjunto 

### o set espera um iteravel na sua construção

### o set não garante a ordem de sequencia, ele pode desordenar o item

## acessando dadso em set
 1. é necessario converte para uma lista, exemplo:
```python
numeros = {1, 2, 3, 2, 1}

//print(numeros[0] ##erro no sistema

numeros = list(numeros)

print(numeros[0])

```
 
⚠️ Para criar um **conjunto vazio**, use `set()` e **não** `{}` (isso cria um dicionário).

---

## 💡 Exemplos Reais

### 🔹 Remover duplicatas de uma lista
```python
numeros = [1, 2, 2, 3, 4, 4, 5]
unicos = set(numeros)
print(unicos)  # {1, 2, 3, 4, 5}
```

### 🔹 Verificar se dois conjuntos têm algo em comum
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # {3} (interseção)
```

### 🔹 Diferença entre conjuntos
```python
print(a - b)  # {1, 2}
print(b - a)  # {4, 5}
```

---
metodos
.unions
.interssesaõ
.difference
.symetric
.issubset 
.issuperset
.isdisjoint 
.add
.clear
.copy
.discarT
.pop
.remove (diferença do discart)
.len
criar exemplos 


## ⚠️ Observações

- Conjuntos **não suportam indexação** (ex: `meu_conjunto[0]` gera erro).
- Elementos duplicados são automaticamente descartados.
- A ordem dos elementos pode mudar a cada execução.
- Muito úteis para testes de pertinência (verificar se um item está presente).
- Operações matemáticas entre conjuntos são simples e rápidas:
  - União: `a | b`
  - Interseção: `a & b`
  - Diferença: `a - b`
  - Diferença simétrica: `a ^ b`
- Conjuntos **não suportam elementos mutáveis** como listas ou dicionários.

---

✍️ Autor: [Andre Almeida](https://github.com/llandrell)
📁 Local: `/anotacoes/5-conjuntos_python.md`