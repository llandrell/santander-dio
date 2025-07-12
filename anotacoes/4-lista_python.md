
# 📚 Trabalhando com Listas em Python

Este módulo aborda os principais conceitos relacionados às **listas em Python**, uma das estruturas de dados mais versáteis e utilizadas na linguagem.

Embora o módulo discuta estruturas de dados como **listas, conjuntos e dicionários**, este documento foca exclusivamente no **trabalho com listas**.

---

## ✅ Objetivos de Aprendizagem

- Compreender o que são listas e como utilizá-las.
- Declarar, acessar, modificar e remover elementos de uma lista.
- Utilizar os principais métodos de listas:  
  `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `index()`, `sort()`, entre outros.
- Iterar sobre listas com `for`, `while` e `enumerate()`.
- Trabalhar com listas aninhadas (listas de listas).
- Utilizar list comprehension para gerar listas de forma concisa.

---



## 🧠 Tópicos Abordados

- Criação e manipulação de listas
- Acesso por índice e fatiamento (slicing)
- Métodos úteis de listas
- Iterações com `for` e `while`
- Listas aninhadas
- Compreensão de listas (list comprehension)

---

## 🧪 Observações Importantes

- Em Python, **tudo é um objeto**, inclusive listas.
- Listas podem armazenar **qualquer tipo de objeto**, inclusive outros objetos mutáveis.
- Podemos criar listas de duas formas:
  - Utilizando colchetes: `[]`
  - Utilizando o construtor `list()`
- Listas são **mutáveis**: seus elementos podem ser modificados após a criação.

---

## 📚 Metodos
1. append() → Adiciona um item no final da lista
📘 Exemplo:
```python
    frutas = ['maçã', 'banana']
    frutas.append('laranja')
    print(frutas)

    Resultado: ['maçã', 'banana', 'laranja']
```
    ✅ Como lembrar: append = adicionar ao fim


2. extend() → Junta outra lista (ou vários itens) à lista atual
📘 Exemplo:
```python
    frutas = ['maçã', 'banana']
    frutas.extend(['abacaxi', 'uva'])
    print(frutas)

    Resultado: ['maçã', 'banana', 'abacaxi', 'uva']
```
    ✅ Usa-se para adicionar vários itens de uma vez

3. insert(posição, item) → Insere um item na posição que você quiser
📘 Exemplo:
```python
    frutas = ['maçã', 'banana']
    frutas.insert(1, 'kiwi')
    print(frutas)

    Resultado: ['maçã', 'kiwi', 'banana']
```python
    ✅ Primeiro argumento é a posição (índice), o segundo é o valor

4. remove(item) → Remove a primeira ocorrência de um item
📘 Exemplo:
```python
    frutas = ['maçã', 'banana', 'banana']
    frutas.remove('banana')
    print(frutas)

    Resultado: ['maçã', 'banana']
```
    ⚠️ Se não encontrar o item, dá erro!


5. pop(posição) → Remove e retorna um item. Se não passar nada, remove o último
📘 Exemplo 1 (remover o último):

```python
    frutas = ['maçã', 'banana']
    removido = frutas.pop()
    print(removido)  # banana
    print(frutas)    # ['maçã']
```

📘 Exemplo 2 (remover na posição 0):
```python
    frutas = ['maçã', 'banana']
    frutas.pop(0)
    print(frutas)    # ['banana']
```
    ✅ Muito usado quando queremos usar e remover ao mesmo tempo

6. index(item) → Retorna o índice da primeira vez que um item aparece
📘 Exemplo:
```python
    frutas = ['maçã', 'banana', 'laranja']
    pos = frutas.index('banana')
    print(pos)
```
📌 Resultado: 1

    ⚠️ Se o item não existir, dá erro!


7. sort() → Ordena a lista em ordem crescente (alfabética ou numérica)
📘 Exemplo:
```python
    numeros = [5, 2, 8, 1]
    numeros.sort()
    print(numeros)
```
📌 Resultado: [1, 2, 5, 8]
🔁 Para ordem decrescente:
```python
    numeros.sort(reverse=True)
    print(numeros)
```
📌 Resultado: [8, 5, 2, 1]

    ✅ Altera a lista original. Para manter original, use sorted(lista)


8. reverse() → Inverte a ordem dos elementos (não confundir com sort!)
📘 Exemplo:
```python
    frutas = ['maçã', 'banana', 'laranja']
    frutas.reverse()
    print(frutas)
```
📌 Resultado: ['laranja', 'banana', 'maçã']


9. count(item) → Conta quantas vezes um item aparece na lista
📘 Exemplo:
```python
    frutas = ['banana', 'banana', 'maçã']
    print(frutas.count('banana'))
```
📌 Resultado: 2


10. clear() → Limpa toda a lista (remove todos os itens)
📘 Exemplo:
```python
    frutas = ['maçã', 'banana']
    frutas.clear()
    print(frutas)
```
📌 Resultado: [] (lista vazia)


11. copy() → Cria uma cópia independente da lista
📘 Exemplo:
```python
    numeros = [1, 2, 3]
    copia = numeros.copy()

    copia.append(4)

    print("Original:", numeros)  # [1, 2, 3]
    print("Cópia:   ", copia)    # [1, 2, 3, 4]
```
📌 Resultado:

Original: [1, 2, 3]  
Cópia:    [1, 2, 3, 4]

    ✅ A lista copia é independente da numeros.
    ✅ Modificar a cópia não altera a original.

⚠️ Sem copy() (erro comum):

```python
    lista1 = [10, 20]
    lista2 = lista1     # Isso não copia, só liga os dois nomes à mesma lista

    lista2.append(30)
    print(lista1)  # [10, 20, 30] → também foi alterada!
```
    ⚠️ Neste caso, as duas variáveis apontam para a mesma lista na memória.

✅ Dica: copiar com copy() ou [:] (fatiamento)

Ambos funcionam bem:
```python
    copia1 = lista.copy()   # Forma clara
    copia2 = lista[:]       # Atalho com fatiamento

```


## 💡 Exemplos

```python
# Criando listas
frutas = ["maçã", "banana", "uva"]         # Forma mais comum
letras = list("python")                    # Com construtor e iterável
numeros = list(range(10))                  # De 0 a 9
carro = ["Ferrari", "F8", 190, True]       # Tipos mistos

# Adicionando elementos
frutas.append("laranja")

# Acessando elementos por índice
print(frutas[0])        # "maçã"

# Acesso com índices negativos
print(frutas[-1])       # "laranja" (último)
print(frutas[-3])       # "banana"
print(frutas[-4])       # "maçã"

# Listas aninhadas (ex: matriz)
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "C"]
]

print(matriz[0])        # [1, "a", 2] lista compelta
print(matriz[0][0])     # 1 pirmeiro indice da primeira linha
print(matriz[0][-1])    # 2 primeira linha ultimo indice
print(matriz[-1][-1])   # "C" ultima linha e ultimo indice
```

---

## ✂️ Exemplo de Fatiamento (Slicing)

O fatiamento permite acessar subconjuntos de elementos de uma lista (ou string) utilizando a notação `lista[início:fim:passo]`.

Além de acessar elementos individualmente por seus índices, também podemos **extrair subconjuntos** de uma sequência (como listas ou strings).  
Para isso, utilizamos a sintaxe `sequência[início:fim:passo]`, onde:

- `início`: índice inicial da fatia (inclusivo)
- `fim`: índice final da fatia (exclusivo)
- `passo`: de quantas em quantas posições o cursor deve pular (opcional)
- Os índices começam no 0

Essa técnica é útil para manipular partes específicas de listas de forma simples e poderosa.

### Exemplo de Fatiamento

```python
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]         # ['t', 'h', 'o', 'n']
# Começa no índice 2 (letra 't') até o final da lista.

lista[:2]         # ['p', 'y']
# Vai do início [0] até o índice 2 (exclui o elemento do índice 2).

lista[1:3]        # ['y', 't']
# Começa no índice 1 (letra 'y') até o índice 3 (exclui o índice 3).

lista[0:3:2]      # ['p', 't']
# Vai do índice 0 ao 3 (sem incluir o 3), pulando de 2 em 2 elementos. [step]

lista[::]         # ['p', 'y', 't', 'h', 'o', 'n']
# Copia a lista inteira (sem definir início, fim ou passo).

lista[::-1]       # ['n', 'o', 'h', 't', 'y', 'p']
# Retorna a lista invertida (passo -1).
```

---

## 🔁 Percorrendo os dados de uma lista

```python
carros = ["gol", "celta", "palio"]

for carro in carros:  # faz a leitura de todos os elementos, "carro" representa cada item dentro de "carros"
    print(carro)

# Às vezes é necessário saber qual o índice do objeto dentro do laço for. Para isso usamos a função enumerate.
for indice, carro in enumerate(carros):
    print(f"{indice} de {carro}")
```

---

## 🧩 Compreensão de Lista

A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

### Exemplos

```python
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

# Forma comum
for numero in numeros:
    if numero % 2 == 0:  # Se o número for par (divisível por 2), se o resto da divisão for 0 
        pares.append(numero)  # Adiciona o número à lista "pares"

# Forma comprimida (compreensão de lista)
pares = [numero for numero in numeros if numero % 2 == 0] # primeira parte é o retorno, a segunda parte é a iteração ou sejá o for , a 3 parte é o filtro o if

# Modificando valores (quadrado dos números)
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)  # no for a gente ta pegando todos os itens de numeros e colocando em numero e adicionando a variavel quadrado vezes 2 

# Forma comprimida
quadrado = [numero ** 2 for numero in numeros]  # a terceira parte da forma comprimida e opcional, não precisa do filtro, dessa forma esta sendo feito um for de numero in numeros e antes de retornar elevando ele ao quadrado.
```

---

## 📌 Observações Finais

- Não necessariamente a lista precisa ter valores para ser criada.
- O índice -1 sempre pega o último item da lista, independente do tamanho.
- Listas são ideais para armazenar coleções ordenadas de itens.
- Caso você precise de coleções imutáveis, prefira utilizar tuplas.
- Se quiser armazenar apenas itens únicos e não ordenados, use conjuntos (set).

---

## 📂 Estrutura

Este diretório conterá arquivos de exemplos, anotações e exercícios resolvidos.

---

📁 **Local:** `/anotacoes/4-lista_python.md`

✍️ Autor: [Andre Almeida](https://github.com/llandrell)