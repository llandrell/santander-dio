
# Dicionários em Python 🐍📘

Os **dicionários** são estruturas de dados em Python que armazenam pares de **chave-valor**. Eles são mutáveis, dinâmicos e não permitem chaves duplicadas.

---

## 📚 Para que servem?

Dicionários são ideais para armazenar dados que precisam ser acessados por uma chave identificadora. Por exemplo:
- Cadastro de usuários (nome, idade, email)
- Contagem de palavras
- Dados estruturados (como JSON)

---

## 🧱 Estrutura básica

```python
meu_dicionario = {
    "chave1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3"
}
```

---

## 🛠️ Como criar um dicionário?

### 1. Usando chaves:
```python
usuario = {
    "nome": "João",
    "idade": 30,
    "email": "joao@email.com"
}
```


### ✍️ Alterando e Adicionando valores
```python
carro["ano"] = 2021  # Altera o valor
carro["cor"] = "Prata"  # Adiciona nova chave
```


### 2. Usando a função `dict()`:
```python

dados = dict(nome="André", idade=28, cidade="Recife")
print(dados)
produto = dict(nome="Notebook", preco=3500.00)
```
#### Importante: ao usar dict() com essa sintaxe, as chaves devem ser strings válidas como nomes de variáveis (sem espaços, não podem começar com número, etc).
---

## 🔍 Acessando dados

```python
print(usuario["nome"])  # João
print(produto.get("preco"))  # 3500.00
```



### 🔍Evitando erro ao acessar chave inexistente
```python

print(carro.get("cor", "Cor não especificada"))  # Cor não especificada
```
---

## ✏️ Modificando valores

```python
usuario["idade"] = 31
usuario["cidade"] = "São Paulo"  # adicionando nova chave
```

---

## ❌ Removendo itens

```python
del usuario["email"]  # Remove a chave 'email'
usuario.pop("idade")
usuario.clear()  # remove todos os itens
```

---

## 🔁 Iterando sobre um dicionário

```python
for chave in usuario:
    print(chave, usuario[chave])

for chave, valor in usuario.items():
    print(f"{chave} => {valor}")
```

---

## 🧪 Métodos úteis

| Método           | Descrição                                 |
|------------------|-------------------------------------------|
| `.get(chave)`    | Retorna o valor da chave                  |
| `.keys()`        | Retorna todas as chaves                   |
| `.values()`      | Retorna todos os valores                  |
| `.items()`       | Retorna todos os pares (chave, valor)     |
| `.update()`      | Atualiza o dicionário com outro dicionário|
| `.pop(chave)`    | Remove uma chave específica               |
| `.clear()`       | Limpa o dicionário                        |

---



### 1. dict.keys()

Retorna uma lista com todas as chaves do dicionário.

```python
print(pessoa.keys())  # dict_keys(['nome', 'idade', 'cidade'])
```
🔎 Dica: Use para iterar pelas chaves do dicionário.

### 2. dict.values()
Retorna uma lista com todos os valores do dicionário.

```python
print(pessoa.values())  # dict_values(['André', 25, 'Fortaleza'])

```

### 3. dict.items()

Retorna uma lista de tuplas (chave, valor).
✨ Vantagens do .items():

    Ideal para loop com chave e valor ao mesmo tempo

    Mais elegante e legível do que acessar manualmente com dict[chave]

    Muito usado com estruturas como if, for, ou mesmo com dict comprehension
```python
for chave, valor in pessoa.items():
    print(f"{chave} → {valor}")

```

### 4. dict.get(chave, valor_padrao)

Retorna o valor da chave. Se ela não existir, retorna None ou um valor padrão.


```python
print(pessoa.get("idade"))          # 25
print(pessoa.get("email", "vazio")) # vazio

```

### 5. dict.update(dicionario_novo)

Atualiza um dicionário com os pares de outro dicionário.

```python
pessoa.update({"email": "andre@email.com"})
print(pessoa)


```

### 6. dict.pop(chave)

Remove e retorna o valor da chave informada.


```python

idade = pessoa.pop("idade")
print(idade)      # 25
print(pessoa)     # idade foi removido


```

### 7. dict.popitem()

Remove o último item inserido no dicionário (Python 3.7+).


```python

ultimo = pessoa.popitem()
print(ultimo)  # ('email', 'andre@email.com')

```


### 8. dict.clear()

Remove todos os itens do dicionário.



```python

pessoa.clear()
print(pessoa)  # {}

```

### 9. dict.copy()

Cria uma cópia rasa (shallow copy) do dicionário.
Ou seja, ele cria um novo dicionário independente, com os mesmos pares chave:valor do original.
    - Isso é útil quando você quer preservar o original e trabalhar em uma cópia isolada.


```python

config_copia = config_original.copy()

```

### 10. dict.fromkeys(iterável, valor)
O método fromkeys() é usado para criar rapidamente um novo dicionário com um conjunto de chaves e um único valor padrão.
Cria um novo dicionário com chaves de um iterável e um único valor padrão.


```python


chaves = ['nome', 'idade', 'email']
novo = dict.fromkeys(chaves, "vazio")
print(novo)
# {'nome': 'vazio', 'idade': 'vazio', 'email': 'vazio'}

dict.fromkeys(iterável, valor_padrao)
# iterável: uma lista, tupla, string, ou qualquer objeto iterável com as chaves.

# valor_padrao: o valor atribuído a todas as chaves.


#🧪 Exemplo básico:

# Lista de chaves
campos = ["nome", "idade", "email"]

# Criando dicionário com valor padrão "vazio"
novo_dicionario = dict.fromkeys(campos, "vazio")

print(novo_dicionario) # {'nome': 'vazio', 'idade': 'vazio', 'email': 'vazio'}
```

### 11. in

Verifica se uma chave existe no dicionário.
```python

print("nome" in pessoa)  # True
print("cpf" in pessoa)   # False
```

### 12. dict.setdefault(chave, valor_padrao)

O método setdefault() é usado para:

    Buscar o valor de uma chave no dicionário.

    Se a chave não existir, ela será criada automaticamente com o valor fornecido.

    Se a chave já existir, o valor não é alterado.

📌 Esse método é útil para evitar KeyError e inicializar valores de forma dinâmica, como listas, contadores ou agrupamentos.


```python
usuario = {
    "nome": "André",
    "idade": 25
}

# Tenta acessar a chave "email". Se não existir, cria com valor padrão.
email = usuario.setdefault("email", "nao informado")

print(email)         # nao informado
print(usuario)       # {'nome': 'André', 'idade': 25, 'email': 'nao informado'}

#💡 Se a chave já existir, o valor não é sobrescrito:

usuario["email"] = "andre@email.com"
usuario.setdefault("email", "outro@email.com")

print(usuario["email"])  # andre@email.com

```

### 13. del – Removendo chaves ou dicionários inteiros

O del é uma instrução do Python usada para:

    Remover uma chave específica de um dicionário.

    Apagar o dicionário inteiro da memória, se necessário.

```python
#🔹 Removendo uma chave específica:

pessoa = {
    "nome": "André",
    "idade": 25,
    "cidade": "Fortaleza"
}

del pessoa["idade"]

print(pessoa) #{'nome': 'André', 'cidade': 'Fortaleza'}


#⚠️ Se a chave não existir, ocorre erro!

del pessoa["email"]  # ❌ KeyError: 'email'

#para evitar esse erro, verifique antes com "chave" in dicionario:

if "email" in pessoa:
    del pessoa["email"]


# 🔹 Apagando o dicionário inteiro:

dados = {"a": 1, "b": 2}
del dados

print(dados)  # ❌ NameError: name 'dados' is not defined
#💥 O dicionário deixou de existir na memória.


```


## 💡💡💡 Exemplos Reais de Uso

```python
Copiar
usuario = {
    "nome": "André",
    "idade": 30,
    "email": "andre@email.com",
    "cursos": ["Python", "JavaScript"]
}

produtos = {
    1001: {"nome": "Teclado", "preco": 120.00},
    1002: {"nome": "Mouse", "preco": 80.00},
    1003: {"nome": "Monitor", "preco": 750.00}
}

```
## 🔍 Como verificar se uma chave está no dicionário
✅ Usando o operador in

```python
pessoa = {
    "nome": "André",
    "idade": 25
}

# Verificar se a chave "nome" existe
if "nome" in pessoa:
    print("A chave 'nome' existe!")

# Verificar se "email" existe
if "email" not in pessoa:
    print("A chave 'email' NÃO existe.")

#🧾 Saída:

#A chave 'nome' existe!
#A chave 'email' NÃO existe.



```


## 📌 Observações

- As **chaves devem ser únicas e imutáveis** (ex: string, número, tupla).
- Os **valores podem ser de qualquer tipo**.
- É uma estrutura **sem ordem** até o Python 3.6 (a partir do 3.7 mantém ordem de inserção).

---

## 🔄 Semelhanças com outras estruturas

- Se assemelha a objetos JSON em JavaScript.
- Funciona como uma **tabela de dados** simples com colunas identificadas.

---

## ✅ Exemplo real

```python
carro = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2021
}

print(f"O carro é um {carro['modelo']} da {carro['marca']}")
```

---

## 🎓 Conclusão

Dicionários são poderosos, flexíveis e essenciais em projetos reais com Python. Use-os sempre que precisar organizar dados com identificadores claros.