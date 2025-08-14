
# Iteradores e Geradores em Python

Iteradores e geradores são conceitos poderosos em Python para trabalhar com sequências de maneira eficiente.

---

## Iteradores

Um **iterador** é um objeto que contém um número contável de valores que podem ser iterados.  
Eles implementam o **protocolo do iterador**, que consiste em dois métodos especiais:

- `__iter__()` → retorna o próprio iterador.
- `__next__()` → retorna o próximo valor da sequência, e levanta `StopIteration` quando os valores acabam.

### Exemplo de iterador manual
```python
class Contador:
    def __init__(self, inicio, fim):
        self.atual = inicio
        self.fim = fim

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual > self.fim:
            raise StopIteration
        valor = self.atual
        self.atual += 1
        return valor

for numero in Contador(1, 5):
    print(numero)
```
Saída:
```
1
2
3
4
5
```

### Quando usar um iterador?
- Quando precisamos **controlar manualmente** o processo de iteração.
- Ao criar estruturas de dados personalizadas que precisam ser percorridas.
- Quando queremos **economizar memória** processando um item por vez.

**Exemplo prático**: leitura linha a linha de um arquivo sem carregar tudo na memória.
```python
with open("arquivo.txt", "r") as f:
    for linha in f:
        print(linha.strip())
```

---

## Geradores

Um **gerador** é um tipo especial de iterador. Ao contrário das listas ou outros iteráveis, eles **não armazenam todos os valores na memória**.  
Eles são definidos usando funções normais, mas em vez de `return`, usam `yield` para retornar valores **sob demanda**.

Quando a função é chamada, ela retorna um objeto gerador, que pode ser percorrido com `for` ou `next()`.

### Exemplo de gerador simples
```python
def contador(inicio, fim):
    atual = inicio
    while atual <= fim:
        yield atual
        atual += 1

for numero in contador(1, 5):
    print(numero)
```
Saída:
```
1
2
3
4
5
```

### Quando usar um gerador?
- Quando trabalhamos com **grandes quantidades de dados** que não cabem na memória.
- Para gerar **fluxos infinitos** ou dados sob demanda.
- Para **pipelines de processamento**, onde cada etapa processa e passa adiante.

**Exemplo prático**: gerar números pares infinitos
```python
def numeros_pares():
    num = 0
    while True:
        yield num
        num += 2

pares = numeros_pares()
for _ in range(5):
    print(next(pares))
```
Saída:
```
0
2
4
6
8
```

---

## Diferença entre iteradores e geradores
| Característica | Iterador | Gerador |
|----------------|----------|---------|
| Criação        | Classe com `__iter__` e `__next__` | Função com `yield` |
| Memória        | Pode armazenar todos os dados | Produz valores sob demanda |
| Complexidade   | Mais código para implementar | Mais simples de criar |
| Uso comum      | Estruturas personalizadas, controle total | Processamento sob demanda, grandes dados |

---

**Resumo**: Use iteradores quando precisar de controle total sobre o processo de iteração ou estruturas personalizadas.  
Use geradores quando quiser simplicidade, eficiência e processamento sob demanda.