
# 🔗 Trabalhando com Tuplas em Python

Este documento reúne **anotações essenciais sobre tuplas** em Python. Tuplas são estruturas de dados similares às listas, porém **imutáveis**.

---

## ✅ Principais Conceitos

- Tupla é **imutável**: após criada, não pode ser alterada.
- Criada usando **parênteses** `( )` ou o construtor `tuple()`.
- Elementos são **indexados** e podem ser de tipos variados.

```python
tupla1 = (1, 2, 3)
tupla2 = "a", "b", "c"    # Parênteses opcionais
tupla_vazia = tuple()
```

---

## 🆚 Tupla x Lista

| Característica | Lista (`list`) | Tupla (`tuple`) |
|----------------|----------------|-----------------|
| Mutável        | ✅ Sim         | ❌ Não          |
| Sintaxe        | Colchetes `[]` | Parênteses `()` |
| Uso típico     | Dados que mudam| Dados fixos     |

- **Quando usar tupla?** Dados constantes: coordenadas, meses do ano, cores fixas.
- **Quando usar lista?** Dados que irão sofrer alterações (adicionar/remover).

---

## 🛠️ Como Criar

```python
tupla = (10, 20, 30)
apenas_um = (42,)  # vírgula obrigatória
sem_parenteses = 1, 2, 3
tupla_from_list = tuple([4, 5, 6])
```

> ⚠️ `(42)` é **int**, não tupla. Sempre coloque a vírgula para 1 item!

---

## 🔍 Acessando Dados

```python
cores = ("red", "green", "blue")

print(cores[0])   # red
print(cores[-1])  # blue
```

### Fatiamento

```python
linguagens = ("Python", "Java", "C", "Go", "Rust")
print(linguagens[1:4])   # ('Java', 'C', 'Go')
print(linguagens[::-1])  # ('Rust', 'Go', 'C', 'Java', 'Python')
```

---

## 📄 Métodos da Tupla

| Método       | Descrição                                  |
|--------------|--------------------------------------------|
| `count(x)`   | Conta ocorrências do valor `x`             |
| `index(x)`   | Retorna o índice da primeira ocorrência de `x` |

```python
dias = ("seg", "ter", "qua", "seg")
print(dias.count("seg"))  # 2
print(dias.index("qua"))  # 2
```

---

## 🧩 Tupla Bidimensional

```python
matriz = (
    (1, 0),
    (0, 1)
)
print(matriz[0][1])  # 0
```

---

## ✂️ Fatiamento com Tuplas

Funciona igual à lista:

```python
t = (0, 1, 2, 3, 4, 5)
print(t[2:])     # (2, 3, 4, 5)
print(t[:3])     # (0, 1, 2)
print(t[::2])    # (0, 2, 4)
```

---

## ⚠️ Precedência e Vírgula Extra

- `(1)` → inteiro 1  
- `(1,)` → tupla de um elemento  
- Em expressões, a vírgula indica **tupla** mais do que os parênteses.

```python
x = (1 + 2) * 3     # precedência aritmética
tupla_num = (1 + 2, 3)  # tupla (3, 3)
```

---

## 📝 Exemplos Práticos

```python
# Desempacotamento
ponto = (3.5, 4.0)
x, y = ponto
print(f"x={x}, y={y}")

# Conversão lista -> tupla
lista_frutas = ["maçã", "banana"]
tupla_frutas = tuple(lista_frutas)

# Iterando
for item in ("a", "b", "c"):
    print(item)
```

---

📁 **Local:** `/anotacoes/5-tuplas_python.md`  
✍️ Autor: [Andre Almeida](https://github.com/llandrell)
