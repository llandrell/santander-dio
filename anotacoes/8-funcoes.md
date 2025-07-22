# 📘 Funções em Python – Anotações de Aula

Este README é uma coletânea de anotações para aprendendo sobre **funções em Python**. Aqui, organizo tudo com exemplos, explicações e comentários no código.

---

## 🧠 O que é uma função?

Uma **função** é um **bloco de código reutilizável**, identificado por um **nome**, que pode receber uma **lista de parâmetros** (ou não) e retornar um valor (ou não).

> ✅ Programar com funções é programar de forma **estruturada**, um dos paradigmas de programação (junto com o orientado a objetos, funcional, entre outros).

---

## 🧱 Estrutura básica de uma função

```python
def nome_da_funcao(parâmetros_opcionais):
    """Docstring explicando a função (opcional)"""
    # bloco de código
    return valor_opcional
```

---

## 📝 Criando a primeira função

```python
def exibir_mensagem():  # declaração da função sem parâmetros
    print("Olá, mundo!")  # o que a função faz
```

Chamando a função:

```python
exibir_mensagem()  # saída: Olá, mundo!
```

---

## 🧾 Funções com parâmetros

```python
def exibir_mensagem(nome):  # função com um parâmetro
    print(f"Olá, {nome}!")  # usa o parâmetro recebido
```

Chamando a função:

```python
exibir_mensagem("Antonio")  # saída: Olá, Antonio!
```

---

## 🧾 Funções com parâmetros com valor padrão

### Funções com parâmetros com valor padrão são aquelas que já definem um valor para um ou mais parâmetros na declaração da função. Isso significa que, se nenhum valor for passado ao chamar a função, o Python irá automaticamente usar o valor definido como padrão.
 - Tornar o código mais flexível.

 - Evitar a necessidade de sempre informar todos os argumentos.

 - Criar funções com comportamento opcional.

 - Melhorar a legibilidade e manutenção do código.

```python
def exibir_mensagem(nome="André"):  # parâmetro com valor padrão
    print(f"Olá, {nome}!")
```

Chamadas:


```python
exibir_mensagem()  # saída: Olá, André!
exibir_mensagem("Maria")  # saída: Olá, Maria!
```

---

## 🎯 Retorno de valores com `return`

### Em Python, toda função retorna algum valor quando é chamada.
Se você não usar explicitamente a palavra-chave return, o Python automaticamente retorna o valor especial None.
 - None é um tipo especial em Python que representa a ausência de valor.

 - Ele não é zero, não é uma string vazia, não é falso — é simplesmente "nada".

 - O tipo de None é NoneType:

####⚠️ Cuidado:
Mesmo que a função faça algo visualmente (como imprimir), isso não significa que ela retornou algum valor:
#### ✅ Dica prática
Se a função só precisa executar uma ação (efeito colateral), como mostrar algo ou salvar em um arquivo, return pode não ser necessário.

Mas se você precisa reutilizar valores, sempre use return:
```python
def soma(a, b):
    return a + b
```

Chamando:

```python
resultado = soma(5, 3)
print(resultado)  # saída: 8
```

---

## 🔄 Retornando múltiplos valores

Em Python, uma função pode retornar **vários valores** ao mesmo tempo usando uma estrutura chamada **tupla**.

### 🧱 O que é uma tupla?

- Uma **tupla** é uma coleção ordenada de elementos.
- Diferente de listas, **tuplas são imutáveis**, ou seja, **não podem ser alteradas** depois de criadas.
- São definidas com **parênteses `()`**, mas também podem ser criadas sem eles (por inferência).
- Permitem **agrupar valores** de diferentes tipos em um único retorno de função.

---

### ✅ Exemplo: função que retorna múltiplos valores

```python
def operacoes(a, b):
    # Retorna uma tupla com dois valores: soma e produto
    return a + b, a * b

# A função retorna dois valores que podemos armazenar separadamente
soma, produto = operacoes(2, 4)
print(soma)     # Saída: 6
print(produto)  # Saída: 8
```
### 🎯 Desempacotamento de valores retornados
Em Python, podemos desempacotar os valores retornados de uma tupla diretamente em variáveis distintas:
```python
def operacoes(a, b):
    return a + b, a - b

# Desempacotando os dois valores da tupla retornada
soma, subtracao = operacoes(10, 5)
print(soma)       # Saída: 15
print(subtracao)  # Saída: 5
```
###📝 Dica: A ordem das variáveis importa! Os valores retornados serão atribuídos na mesma ordem em que foram definidos na tupla.
---


### 🧠 Curiosidade
Você também pode retornar explicitamente uma tupla usando parênteses:

```python
def valores():
    return (1, 2, 3)  # Também é uma tupla

x, y, z = valores()
print(x, y, z)
#Mas os parênteses são opcionais na hora de retornar múltiplos valores — o Python já entende que são uma tupla.

```

## 🔢 Tipos de parâmetros

1. **Obrigatórios**  
2. **Com valor padrão**
3. **`*args`** (lista de argumentos variáveis)
4. **`**kwargs`** (dicionário de argumentos nomeados)

---

## 🧪 Usando `*args`

```python
def somar_todos(*numeros):
    return sum(numeros)

print(somar_todos(1, 2, 3, 4))  # saída: 10
```

---

## 🧪 Usando `**kwargs`
`*args` permite que uma função **receba um número variável de argumentos posicionais**.

- A palavra `args` é apenas um nome por convenção (você pode usar qualquer outro nome), mas o `*` é obrigatório.
- Os argumentos são armazenados em uma **tupla**, o que significa que você pode iterar sobre eles, mas **não pode modificá-los diretamente**.

```python
def somar_tudo(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(somar_tudo(1, 2, 3))          # Saída: 6
print(somar_tudo(5, 10, 15, 20))    # Saída: 50
```
Nesse exemplo acima:
A função aceita quantos argumentos você quiser.
Todos os argumentos passados são reunidos em uma tupla chamada args.

```python
def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Ana", idade=30)
# saída:
# nome: Ana
# idade: 30
```
### 🎒 Por que usar *args?
 - Quando você não sabe quantos argumentos a função receberá.

 - Para permitir que o usuário passe vários valores, como em funções de soma, concatenação, ou exibição dinâmica.
---

## 📛 Argumentos nomeados vs posicionais

```python
def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")

# Posicional:
saudacao("Carlos", "Bom dia")

# Nomeado:
saudacao(nome="Carlos", mensagem="Boa tarde")
```

> 🔹 Boas práticas: use nomeados para clareza, principalmente quando houver muitos argumentos.

---

## 🧠 `def` – palavra reservada

- `def` significa "define".
- É usada para declarar uma nova função.

```python
def minha_funcao():
    print("Função criada com def!")
```

---

## 📚 Exemplos práticos comentados

```python
def calcular_area(base, altura):
    """Função que calcula a área de um retângulo"""
    area = base * altura
    return area

# Chamando e imprimindo
print(calcular_area(5, 2))  # saída: 10
```

---

## 🔄 Passando dicionário com `**`

```python
def apresentar_pessoa(nome, idade):
    print(f"{nome} tem {idade} anos.")

dados = {"nome": "João", "idade": 40}
apresentar_pessoa(**dados)  # desempacotando o dicionário
```

---

## 🔚 Conclusão

- Funções são **fundamentais** na programação estruturada.
- Evitam repetição de código.
- Deixam o código **modular** e **mais fácil de manter**.
- Podem aceitar e retornar valores de diversas formas.
- Os parâmetros podem ser simples, nomeados, opcionais ou variáveis (`*args`, `**kwargs`).

---

## 🧠 Dica extra: funções como objetos

Funções em Python são **objetos de primeira classe**. Podemos passá-las como argumento, retorná-las de outras funções, etc.

```python
def saudacao():
    return "Olá!"

def executar(funcao):
    print(funcao())

executar(saudacao)  # saída: Olá!
```

---
