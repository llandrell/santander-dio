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

###⚠️ Cuidado:
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

# 🧠 Funções em Python — Parâmetros Especiais e Objetos de Primeira Classe

## 🔹 Argumentos em Python

Quando chamamos uma função em Python, podemos passar argumentos de **duas formas**:

1. **Por posição** (ordem importa)  
2. **Por nome** (explicitando o nome do parâmetro)

### Exemplo básico:

```python
def saudacao(nome, mensagem):
    print(f"{mensagem}, {nome}!")

saudacao("André", "Olá")                 # por posição
saudacao(nome="André", mensagem="Olá")   # por nome
```

---

## 🎯 Por que restringir a forma de passar argumentos?

Em funções complexas, para deixar o código **mais claro e seguro**, podemos **especificar se os argumentos devem ser passados por posição ou nome**.

Python permite isso com os **parâmetros especiais**:

```python
def f(pos1, pos2, /, por_or_key, *, kwd1, kwd2):
    pass
```

### 📌 Significado da assinatura:

| Símbolo | Significado |
|--------|-------------|
| `/`    | Tudo antes deve ser passado por **posição** |
| `*`    | Tudo depois deve ser passado por **nome** (keyword only) |
| Entre os dois | Pode ser por posição ou por nome |

---

## ✅ Exemplos válidos:

```python
def f(a, b, /, c, *, d, e):
    print(a, b, c, d, e)

f(1, 2, 3, d=4, e=5)           # ✔️ OK
f(1, 2, c=3, d=4, e=5)         # ✔️ OK
```

## ❌ Exemplos inválidos:

```python
f(a=1, b=2, c=3, d=4, e=5)     # ❌ Erro: a e b devem ser passados por posição
f(1, 2, 3, 4, e=5)             # ❌ Erro: 'd' deve ser nomeado
```

---

## 🧪 Exemplos com os três tipos

```python
def exemplo(x, y, /, z, *, w):
    print(f"x={x}, y={y}, z={z}, w={w}")

# Correto:
exemplo(10, 20, 30, w=40)         # x=10, y=20, z=30, w=40

# Inválido:
# exemplo(x=10, y=20, z=30, w=40)  # ❌ 'x' e 'y' devem ser passados por posição
```

---

# 🧩 Funções como Objetos de Primeira Classe

Em Python, **funções são objetos de primeira classe**, ou seja, podem ser:

✅ Atribuídas a variáveis  
✅ Passadas como argumentos  
✅ Retornadas de outras funções (closures)  
✅ Armazenadas em estruturas de dados (listas, dicionários, etc.)

---

## 🎓 O que são Objetos de Primeira Classe?

Objetos que:
- Podem ser criados em tempo de execução
- Podem ser atribuídos a variáveis
- Podem ser passados como argumento
- Podem ser retornados por outras funções

---

## 🔹 1. Atribuindo uma função a uma variável

```python
def somar(a, b):
    return a + b

# Atribuindo a função a outra variável
operacao = somar
print(operacao(3, 4))  # 7
```

---

## 🔹 2. Passando uma função como argumento

```python
def aplicar(funcao, x, y):
    return funcao(x, y)

def multiplicar(a, b):
    return a * b

print(aplicar(multiplicar, 5, 6))  # 30
```

---

## 🔹 3. Usando em estruturas de dados

```python
def saudacao():
    return "Olá"

def despedida():
    return "Tchau"

acoes = {
    "inicio": saudacao,
    "fim": despedida
}

print(acoes["inicio"]())  # Olá
```

---

## 🔹 4. Retornando funções (Closures)

```python
def criar_saudacao(nome):
    def saudacao():
        return f"Olá, {nome}!"
    return saudacao

mensagem = criar_saudacao("André")
print(mensagem())  # Olá, André!
```

💡 Aqui `mensagem` é uma **função personalizada**, gerada com base no nome.

---

## 📦 Quais são os Objetos de Primeira Classe em Python?

Além de funções, os seguintes objetos também são de primeira classe em Python:

| Tipo de Objeto      | É de Primeira Classe? |
|---------------------|------------------------|
| Números             | ✅ Sim |
| Strings             | ✅ Sim |
| Listas              | ✅ Sim |
| Tuplas              | ✅ Sim |
| Dicionários         | ✅ Sim |
| Funções             | ✅ Sim |
| Classes e Objetos   | ✅ Sim |

---

## ✅ Conclusão

- Parâmetros especiais (`/`, `*`) melhoram **legibilidade e clareza** das funções.
- Funções são **cidadãos de primeira classe** em Python — podem ser manipuladas como dados.
- Isso torna Python uma linguagem extremamente **flexível e poderosa** para programação funcional e estruturada.

---

# 📚 Blocos e Escopos em Python — Foco em Funções

## 🧱 O que são Blocos?

Um **bloco** é uma área de código que fica **delimitada por indentação** em Python. Toda função, estrutura de repetição (`for`, `while`), condição (`if`, `elif`, `else`) ou classe tem seu **próprio bloco**.

### Exemplo de bloco dentro de uma função:

```python
def saudacao(nome):
    mensagem = f"Olá, {nome}!"  # Bloco da função começa aqui
    print(mensagem)             # Ainda dentro do bloco da função
```

---

## 🧭 O que é Escopo?

O **escopo** define onde uma variável é **visível e acessível** no programa.  
Em Python, existem **quatro níveis principais de escopo**, conhecidos pela sigla **LEGB**:

| Sigla | Escopo         | Descrição                                        |
|-------|----------------|--------------------------------------------------|
| L     | Local          | Dentro da função onde a variável foi criada     |
| E     | Enclosing      | Funções aninhadas (escopo da função externa)    |
| G     | Global         | Variáveis definidas no nível principal do script|
| B     | Built-in       | Funções e nomes próprios do Python (`len`, `print`) |

---

## 🎯 Escopo Local

Variáveis declaradas **dentro de uma função** só podem ser usadas dentro daquela função.

```python
def exemplo():
    x = 10        # Escopo local
    print(x)

exemplo()        # 10
print(x)         # ❌ Erro: x não está definido fora da função
```

---

## 📦 Escopo Global

Variáveis declaradas **fora de qualquer função** podem ser acessadas dentro das funções, mas **não podem ser modificadas diretamente**, a menos que usemos a palavra-chave `global`.

```python
x = 5  # Variável global

def mostrar():
    print(x)  # Pode acessar, mas não modificar

mostrar()     # 5
```

---

## ⚠️ Modificando variáveis globais (com `global`)

```python
contador = 0

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
```

✅ Isso funciona, mas…

---

## ❌ Por que NÃO usar variáveis globais?

Usar `global` é geralmente **uma má prática**, porque:

- ❗ Dificulta o **entendimento e a manutenção** do código.
- 🧪 Torna o programa **menos previsível** e mais propenso a **erros difíceis de rastrear**.
- 🔁 Quebra o princípio do **encapsulamento** e da **modularidade**.
- 🧩 Funções devem ser **independentes** e não depender de variáveis externas.

---

## ✅ Boas práticas:

- Prefira **retornar valores** de funções e usar variáveis locais.
- Use `global` **apenas quando extremamente necessário**.
- Se precisar compartilhar estado entre funções, use **parâmetros** ou **objetos** (como dicionários ou classes).

---

## 🧪 Exemplo ruim com `global`:

```python
total = 0

def adicionar(valor):
    global total
    total += valor

adicionar(10)
adicionar(5)
print(total)  # 15
```

🧨 Problema: a função **muda o estado global**, o que pode causar **efeitos colaterais** inesperados.

---

## ✅ Exemplo com boas práticas:

```python
def adicionar(valor, total):
    return total + valor

total = 0
total = adicionar(10, total)
total = adicionar(5, total)
print(total)  # 15
```

👍 Mais seguro, mais previsível e fácil de testar!

---

## 🔄 Funções dentro de funções (Escopo Enclosing)

```python
def externa():
    mensagem = "Olá"

    def interna():
        print(mensagem)  # Usa variável do escopo da função externa

    interna()

externa()  # Olá
```

🧠 Isso é útil em **closures** e funções decoradoras.

---

## 📌 Resumo:

| Conceito       | Explicação breve |
|----------------|------------------|
| **Bloco**      | Área de código delimitada por indentação |
| **Escopo**     | Onde a variável é visível e utilizável |
| **Local**      | Dentro da função |
| **Global**     | Fora da função, acessível por todos |
| **Enclosing**  | Funções dentro de funções |
| **Built-in**   | Escopo das funções internas do Python |

---

## 🎓 Conclusão:

- Sempre **prefira variáveis locais**.
- Use `return` e **parâmetros bem definidos**.
- Evite `global`, a não ser que seja extremamente necessário.
- Entender escopos te ajuda a **organizar, testar e manter** seu código com mais clareza.

---
