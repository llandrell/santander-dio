
# Operadores de Associação em Python

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

- O operador `in` é **sensível à capitalização**:
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
